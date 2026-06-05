from collections import Counter
from views.RelatorioView import RelatorioView

class RelatorioController:
    def __init__(self, controlador_atendimentos, controlador_procedimentos):
        self.__c_atendimentos = controlador_atendimentos
        self.__c_procedimentos = controlador_procedimentos
        self.__view = RelatorioView()

    def abre_tela(self):
        lista_opcoes = {
            "1": self.clinicas_com_mais_atendimentos,
            "2": self.atendimentos_extremos,
            "3": self.procedimentos_mais_realizados,
            "4": self.procedimentos_extremos,
            "0": self.retornar
        }
        while True:
            opcao = self.__view.mostra_menu()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            if opcao == "0":
                break

    def clinicas_com_mais_atendimentos(self):
        lista = self.__c_atendimentos.atendimentos
        if not lista:
            self.__view.mostra_mensagem("Dados insuficientes.")
            return
        
        # Mapeia e conta ocorrências de clínicas
        contagem = Counter(at.clinica.nome for at in lista)
        ranking = contagem.most_common()
        self.__view.mostra_ranking_clinicas(ranking)

    def atendimentos_extremos(self):
        lista = self.__c_atendimentos.atendimentos
        if not lista:
            self.__view.mostra_mensagem("Dados insuficientes.")
            return

        # Monta tuplas contendo (índice, valor_total)
        valores = []
        for idx, at in enumerate(lista):
            tot = self.__c_atendimentos.calcular_valor_total(at)
            valores.append((idx, tot))

        # Ordenação decrescente por valor total
        valores_ordenados = sorted(valores, key=lambda x: x[1], reverse=True)
        
        # Pega os 3 maiores e os 3 menores (ou o total disponível caso seja menor que 3)
        mais_caros = valores_ordenados[:3]
        mais_baratos = valores_ordenados[-3:]
        
        self.__view.mostra_extremos_atendimentos(mais_caros, mais_baratos)

    def procedimentos_mais_realizados(self):
        lista_at = self.__c_atendimentos.atendimentos
        if not lista_at:
            self.__view.mostra_mensagem("Dados insuficientes.")
            return

        todos_proc = []
        for at in lista_at:
            for proc in at.procedimentos:
                todos_proc.append(proc.descricao)

        if not todos_proc:
            self.__view.mostra_mensagem("Nenhum procedimento foi realizado em atendimentos ainda.")
            return

        contagem = Counter(todos_proc)
        self.__view.mostra_ranking_procedimentos(contagem.most_common())

    def procedimentos_extremos(self):
        # Aqui avaliamos o custo unitário estático do cadastro de procedimentos
        # Usamos uma função anônima lambda para ordenar de forma decrescente pelo custo do objeto
        todos_procedimentos = sorted(
            self.__c_procedimentos._ProcedimentoController__procedimentos, 
            key=lambda p: p.custo, 
            reverse=True
        )

        if not todos_procedimentos:
            self.__view.mostra_mensagem("Nenhum procedimento cadastrado no sistema.")
            return

        mais_caros = todos_procedimentos[:3]
        mais_baratos = todos_procedimentos[-3:]

        self.__view.mostra_extremos_procedimentos(mais_caros, mais_baratos)

    def retornar(self):
        pass