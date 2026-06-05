from datetime import datetime
from classes.atendimento import Atendimento
from classes.pagamento import PagamentoPix, PagamentoDinheiro, PagamentoCartao
from views.AtendimentoView import AtendimentoView
from views.PagamentoView import PagamentoView

class AtendimentoController:
    def __init__(self, c_pacientes, c_clinicas, c_procedimentos, c_tipos):
        self.__atendimentos = []
        self.__view = AtendimentoView()
        self.__view_pagamento = PagamentoView()
        
        # Injeção dos controladores necessários para as amarrações e validações
        self.__c_pacientes = c_pacientes
        self.__c_clinicas = c_clinicas
        self.__c_procedimentos = c_procedimentos
        self.__c_tipos = c_tipos

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abre_tela(self):
        lista_opcoes = {
            "1": self.incluir,
            "2": self.alterar,
            "3": self.excluir,
            "4": self.listar,
            "5": self.adicionar_procedimento,
            "6": self.registrar_pagamento,
            "0": self.retornar
        }
        while True:
            opcao = self.__view.mostra_menu()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            if opcao == "0":
                break

    def __validar_horario(self, h_inicio: str, h_fim: str, clinica) -> bool:
        """Validação obrigatória: Horário dentro do funcionamento da clínica."""
        try:
            formato = "%H:%M"
            ini = datetime.strptime(h_inicio, formato).time()
            fim = datetime.strptime(h_fim, formato).time()
            abertura = datetime.strptime(clinica.horarioAbertura, formato).time()
            fechamento = datetime.strptime(clinica.horarioFechamento, formato).time()
            
            if ini >= abertura and fim <= fechamento and ini < fim:
                return True
            return False
        except ValueError:
            return False

    def calcular_valor_total(self, atendimento) -> float:
        """Soma o valor base do atendimento + custos de todos os procedimentos vinculados."""
        total_procedimentos = sum(p.custo for p in atendimento.procedimentos)
        return atendimento.valor + total_procedimentos

    def calcular_saldo_restante(self, atendimento) -> float:
        """Calcula quanto falta pagar com base nos pagamentos parciais feitos."""
        total_devido = self.calcular_valor_total(atendimento)
        total_pago = sum(pag.valorPago for pag in atendimento.pagamentos)
        return max(0.0, total_devido - total_pago)

    def incluir(self):
        dados = self.__view.pega_dados_atendimento()

        paciente = self.__c_pacientes.busca_paciente(dados["cpf_paciente"])
        clinica = self.__c_clinicas.busca_clinica(dados["nome_clinica"])
        tipo = self.__c_tipos.busca_tipo(dados["desc_tipo"])

        if not paciente:
            self.__view.mostra_mensagem("Erro: Paciente não encontrado.")
            return
        if not clinica:
            self.__view.mostra_mensagem("Erro: Clínica não encontrada.")
            return
        if not tipo:
            self.__view.mostra_mensagem("Erro: Tipo de atendimento não encontrado.")
            return

        # Executa validação de horário de atendimento
        if not self.__validar_horario(dados["horarioInicio"], dados["horarioFim"], clinica):
            self.__view.mostra_mensagem("Erro: Horário fora do expediente da clínica ou inválido.")
            return

        try:
            data_formatada = datetime.strptime(dados["data"], "%Y-%m-%d").date()
        except ValueError:
            self.__view.mostra_mensagem("Erro: Formato de data inválido.")
            return

        # Definindo valor base padrão para o atendimento
        valor_base = 150.00

        novo_atendimento = Atendimento(
            data=data_formatada,
            horarioInicio=dados["horarioInicio"],
            horarioFim=dados["horarioFim"],
            valor=valor_base,
            paciente=paciente,
            clinica=clinica,
            tipoAtendimento=tipo
        )
        
        self.__atendimentos.append(novo_atendimento)
        self.__view.mostra_mensagem("Atendimento agendado com sucesso!")

    def alterar(self):
        self.listar()
        if not self.__atendimentos:
            return
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = self.__atendimentos[idx]
        except (ValueError, IndexError):
            self.__view.mostra_mensagem("Atendimento inválido.")
            return

        dados = self.__view.pega_dados_alteracao()
        if self.__validar_horario(dados["horarioInicio"], dados["horarioFim"], atendimento.clinica):
            atendimento.horarioInicio = dados["horarioInicio"]
            atendimento.horarioFim = dados["horarioFim"]
            self.__view.mostra_mensagem("Horários alterados com sucesso!")
        else:
            self.__view.mostra_mensagem("Erro: Horários inconsistentes com as regras da clínica.")

    def excluir(self):
        self.listar()
        if not self.__atendimentos:
            return
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = self.__atendimentos[idx]
            self.__atendimentos.remove(atendimento)
            self.__view.mostra_mensagem("Atendimento removido.")
        except (ValueError, IndexError):
            self.__view.mostra_mensagem("Atendimento inválido.")

    def listar(self):
        if not self.__atendimentos:
            self.__view.mostra_mensagem("Nenhum atendimento registrado.")
            return
        for i, at in enumerate(self.__atendimentos):
            tot = self.calcular_valor_total(at)
            rest = self.calcular_saldo_restante(at)
            self.__view.mostra_atendimento(i, at, tot, rest)

    def adicionar_procedimento(self):
        self.listar()
        if not self.__atendimentos:
            return
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = self.__atendimentos[idx]
        except (ValueError, IndexError):
            self.__view.mostra_mensagem("Atendimento inválido.")
            return

        desc_p = self.__view.pega_descricao_procedimento()
        procedimento = self.__c_procedimentos.busca_procedimento(desc_p)

        if not procedimento:
            self.__view.mostra_mensagem("Procedimento não encontrado.")
            return

        atendimento.adicionar_procedimento(procedimento)
        self.__view.mostra_mensagem(f"Procedimento '{procedimento.descricao}' adicionado ao atendimento!")

    def registrar_pagamento(self):
        """Lógica de Validações de Pagamento (Parciais, Restantes e Modalidades)"""
        self.listar()
        if not self.__atendimentos:
            return
        try:
            idx = self.__view.pega_id_atendimento()
            atendimento = self.__atendimentos[idx]
        except (ValueError, IndexError):
            self.__view.mostra_mensagem("Atendimento inválido.")
            return

        restante = self.calcular_saldo_restante(atendimento)
        if restante <= 0:
            self.__view.mostra_mensagem("Este atendimento já está totalmente pago!")
            return

        modalidade = self.__view_pagamento.escolhe_modalidade()
        if modalidade == "0" or modalidade not in ["1", "2", "3"]:
            return

        dados_comuns = self.__view_pagamento.pega_dados_comuns()
        try:
            data_pagm = datetime.strptime(dados_comuns["data"], "%Y-%m-%d").date()
        except ValueError:
            self.__view.mostra_mensagem("Data inválida.")
            return

        val_pago = dados_comuns["valorPago"]
        if val_pago <= 0:
            self.__view.mostra_mensagem("O valor pago deve ser maior que zero.")
            return
        if val_pago > restante:
            self.__view.mostra_mensagem(f"Aviso: O valor inserido supera o saldo devedor (R$ {restante:.2f}). Ajustando para o saldo restante.")
            val_pago = restante

        # Instanciação polimórfica baseada na modalidade escolhida
        pagamento = None
        if modalidade == "1":
            cpf = self.__view_pagamento.pega_dados_pix()
            pagamento = PagamentoPix(data_pagm, val_pago, cpf)
        elif modalidade == "2":
            pagamento = PagamentoDinheiro(data_pagm, val_pago)
        elif modalidade == "3":
            card = self.__view_pagamento.pega_dados_cartao()
            pagamento = PagamentoCartao(data_pagm, val_pago, card["numeroCartao"], card["bandeira"])

        if pagamento is None:
            self.__view.mostra_mensagem("Erro: modalidade de pagamento inválida.")
            return

        atendimento.adicionar_pagamento(pagamento)
        novo_restante = self.calcular_saldo_restante(atendimento)
        
        self.__view.mostra_mensagem(f"Pagamento de R$ {val_pago:.2f} processado!")
        if novo_restante == 0:
            self.__view.mostra_mensagem("Atendimento TOTALMENTE QUITADO!")
        else:
            self.__view.mostra_mensagem(f"Pagamento PARCIAL. Valor restante: R$ {novo_restante:.2f}")

    def retornar(self):
        pass