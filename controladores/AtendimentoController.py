from datetime import datetime
from classes.atendimento import Atendimento
from views.AtendimentoView import AtendimentoView
from controladores.PagamentoController import PagamentoController 
from DAOs.AtendimentoDAO import AtendimentoDAO

class AtendimentoController:
    def __init__(self, c_pacientes, c_clinicas, c_procedimentos, c_tipos):
        self.__dao = AtendimentoDAO()
        self.__view = AtendimentoView()
        self.__pagamento_controller = PagamentoController() 
        
        self.__c_pacientes = c_pacientes
        self.__c_clinicas = c_clinicas
        self.__c_procedimentos = c_procedimentos
        self.__c_tipos = c_tipos

    @property
    def atendimentos(self):
        return self.__dao.get_all()
    
    def __gerar_chave(self, atendimento):
        """Helper interno para garantir chave única no DAO"""
        return f"{atendimento.data}_{atendimento.horarioInicio}_{atendimento.paciente.cpf}"

    def abre_tela(self):
        lista_opcoes = {
            "1": self.incluir, "2": self.alterar, "3": self.excluir,
            "4": self.listar, "5": self.adicionar_procedimento, 
            "6": self.registrar_pagamento, "0": self.retornar
        }
        while True:
            opcao = self.__view.mostra_menu()
            funcao = lista_opcoes.get(opcao)
            if funcao: funcao()
            if opcao == "0": break

    def __validar_horario(self, h_inicio, h_fim, clinica) -> bool:
        try:
            ini = datetime.strptime(h_inicio, "%H:%M").time()
            fim = datetime.strptime(h_fim, "%H:%M").time()
            abertura = datetime.strptime(clinica.horarioAbertura, "%H:%M").time()
            fechamento = datetime.strptime(clinica.horarioFechamento, "%H:%M").time()
            return ini >= abertura and fim <= fechamento and ini < fim
        except: return False

    def calcular_valor_total(self, atendimento) -> float:
        total_procedimentos = sum(p.custo for p in atendimento.procedimentos)
        return atendimento.valor + total_procedimentos

    def calcular_saldo_restante(self, atendimento) -> float:
        total_devido = self.calcular_valor_total(atendimento)
        total_pago = sum(pag.valorPago for pag in atendimento.pagamentos)
        return max(0.0, total_devido - total_pago)

    def incluir(self):
        dados = self.__view.pega_dados_atendimento()

        paciente = self.__c_pacientes.busca_paciente(dados["cpf_paciente"])
        clinica = self.__c_clinicas.busca_clinica(dados["nome_clinica"])
        tipo = self.__c_tipos.busca_tipo(dados["desc_tipo"])

        if not paciente or not clinica or not tipo:
            self.__view.mostra_mensagem("Erro: Vínculo (Paciente/Clínica/Tipo) não encontrado.")
            return

        if not self.__validar_horario(dados["horarioInicio"], dados["horarioFim"], clinica):
            self.__view.mostra_mensagem("Erro: Horário inválido para esta clínica.")
            return

        try: data_formatada = datetime.strptime(dados["data"], "%Y-%m-%d").date()
        except: 
            self.__view.mostra_mensagem("Erro: Formato de data inválido.")
            return

        novo_atendimento = Atendimento(
            data_formatada, dados["horarioInicio"], dados["horarioFim"], 
            150.00, paciente, clinica, tipo
        )
        
        chave = self.__gerar_chave(novo_atendimento)
        self.__dao.add(chave, novo_atendimento)
        self.__view.mostra_mensagem("Atendimento agendado com sucesso!")

    def alterar(self):
        self.listar()
        lista = self.atendimentos
        if not lista: return
        
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = lista[idx]
        except:
            self.__view.mostra_mensagem("Atendimento inválido.")
            return

        dados = self.__view.pega_dados_alteracao()
        if self.__validar_horario(dados["horarioInicio"], dados["horarioFim"], atendimento.clinica):
            chave_antiga = self.__gerar_chave(atendimento)
            self.__dao.remove(chave_antiga)
            
            atendimento.horarioInicio = dados["horarioInicio"]
            atendimento.horarioFim = dados["horarioFim"]
            
            chave_nova = self.__gerar_chave(atendimento)
            self.__dao.add(chave_nova, atendimento)
            self.__view.mostra_mensagem("Horários alterados com sucesso!")
        else:
            self.__view.mostra_mensagem("Erro: Horários inconsistentes.")

    def excluir(self):
        self.listar()
        lista = self.atendimentos
        if not lista: return
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = lista[idx]
            chave = self.__gerar_chave(atendimento)
            self.__dao.remove(chave)
            self.__view.mostra_mensagem("Atendimento removido.")
        except:
            self.__view.mostra_mensagem("Atendimento inválido.")

    def listar(self):
        lista = self.atendimentos
        if not lista:
            self.__view.mostra_mensagem("Nenhum atendimento registrado.")
            return
        for i, at in enumerate(lista):
            tot = self.calcular_valor_total(at)
            rest = self.calcular_saldo_restante(at)
            self.__view.mostra_atendimento(i, at, tot, rest)

    def adicionar_procedimento(self):
        self.listar()
        lista = self.atendimentos
        if not lista: return
        
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = lista[idx]
        except:
            self.__view.mostra_mensagem("Atendimento inválido.")
            return

        desc_p = self.__view.pega_descricao_procedimento()
        procedimento = self.__c_procedimentos.busca_procedimento(desc_p)

        if not procedimento:
            self.__view.mostra_mensagem("Procedimento não encontrado.")
            return

        atendimento.adicionar_procedimento(procedimento)
        
        chave = self.__gerar_chave(atendimento)
        self.__dao.add(chave, atendimento)
        self.__view.mostra_mensagem(f"Procedimento adicionado!")

    def registrar_pagamento(self):
        self.listar()
        lista = self.atendimentos
        if not lista: return
        
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = lista[idx]
        except:
            self.__view.mostra_mensagem("Atendimento inválido.")
            return

        restante = self.calcular_saldo_restante(atendimento)
        if restante <= 0:
            self.__view.mostra_mensagem("Atendimento totalmente pago!")
            return

        pagamento = self.__pagamento_controller.processar_pagamento(restante)
        if not pagamento: return

        atendimento.adicionar_pagamento(pagamento)
        
        chave = self.__gerar_chave(atendimento)
        self.__dao.add(chave, atendimento)
        
        novo_restante = self.calcular_saldo_restante(atendimento)
        self.__view.mostra_mensagem(f"Pagamento efetuado! Restante: R$ {novo_restante:.2f}")

    def retornar(self):
        pass