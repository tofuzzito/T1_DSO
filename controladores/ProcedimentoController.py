from classes.procedimento import Procedimento
from views.ProcedimentoView import ProcedimentoView
from DAOs.ProcedimentoDAO import ProcedimentoDAO

class ProcedimentoController:
    def __init__(self, controlador_profissionais):
        self.__dao = ProcedimentoDAO()
        self.__view = ProcedimentoView()
        self.__c_profissionais = controlador_profissionais

    @property
    def procedimentos(self):
        return self.__dao.get_all()

    def abre_tela(self):
        lista_opcoes = {
            "1": self.incluir, "2": self.alterar, 
            "3": self.excluir, "4": self.listar, "0": self.retornar
        }
        while True:
            opcao = self.__view.mostra_menu()
            funcao = lista_opcoes.get(opcao)
            if funcao: funcao()
            if opcao == "0": break

    def incluir(self):
        dados = self.__view.pega_dados_procedimento()
        if not dados: return

        if self.busca_procedimento(dados["descricao"]):
            self.__view.mostra_mensagem("Procedimento já cadastrado.")
            return

        profissional = self.__c_profissionais.busca_profissional(dados["cpf_profissional"])
        if not profissional:
            self.__view.mostra_mensagem("Profissional não encontrado.")
            return

        procedimento = Procedimento(dados["descricao"], dados["custo"], profissional)
        self.__dao.add(procedimento.descricao, procedimento)
        self.__view.mostra_mensagem("Procedimento cadastrado.")

    def alterar(self):
        descricao = self.__view.pega_descricao()
        procedimento = self.busca_procedimento(descricao)

        if not procedimento:
            self.__view.mostra_mensagem("Procedimento não encontrado.")
            return

        dados = self.__view.pega_dados_procedimento()
        if not dados: return

        profissional = self.__c_profissionais.busca_profissional(dados["cpf_profissional"])
        if not profissional:
            self.__view.mostra_mensagem("Profissional não encontrado.")
            return

        if procedimento.descricao.lower() != dados["descricao"].lower():
            self.__dao.remove(procedimento.descricao)

        procedimento.descricao = dados["descricao"]
        procedimento.custo = dados["custo"]
        procedimento.profissional = profissional

        self.__dao.add(procedimento.descricao, procedimento)
        self.__view.mostra_mensagem("Procedimento alterado.")

    def excluir(self):
        descricao = self.__view.pega_descricao()
        if not self.busca_procedimento(descricao):
            self.__view.mostra_mensagem("Procedimento não encontrado.")
            return

        self.__dao.remove(descricao)
        self.__view.mostra_mensagem("Procedimento removido.")

    def listar(self):
        procedimentos = self.__dao.get_all()
        if not procedimentos:
            self.__view.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        for proc in procedimentos:
            self.__view.mostra_procedimento(proc)

    def busca_procedimento(self, descricao):
        return self.__dao.get(descricao)

    def retornar(self):
        pass