from classes.atendimento import TipoAtendimento
from views.TipoAtendimentoView import TipoAtendimentoView
from DAOs.DAO import DAO

class TipoAtendimentoController:
    def __init__(self):
        self.__dao = DAO("tipos_atendimento.pkl")
        self.__view = TipoAtendimentoView()

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
        dados = self.__view.pega_dados()
        if self.busca_tipo(dados["descricao"]):
            self.__view.mostra_mensagem("Esse tipo de atendimento já existe.")
            return

        novo_tipo = TipoAtendimento(dados["descricao"])
        self.__dao.add(novo_tipo.descricao, novo_tipo)
        self.__view.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")

    def alterar(self):
        desc = self.__view.pega_descricao()
        tipo = self.busca_tipo(desc)
        if not tipo:
            self.__view.mostra_mensagem("Tipo de atendimento não encontrado.")
            return

        dados = self.__view.pega_dados()
        self.__dao.remove(tipo.descricao)
        tipo.descricao = dados["descricao"]
        self.__dao.add(tipo.descricao, tipo)
        self.__view.mostra_mensagem("Tipo de atendimento alterado com sucesso!")

    def excluir(self):
        desc = self.__view.pega_descricao()
        if not self.busca_tipo(desc):
            self.__view.mostra_mensagem("Tipo de atendimento não encontrado.")
            return

        self.__dao.remove(desc)
        self.__view.mostra_mensagem("Tipo de atendimento removido com sucesso.")

    def listar(self):
        tipos = self.__dao.get_all()
        if not tipos:
            self.__view.mostra_mensagem("Nenhum tipo cadastrado.")
            return
        for t in tipos:
            self.__view.mostra_tipo(t)

    def busca_tipo(self, descricao):
        # A busca em DAOs genéricos diferencia maiúsculas, garantindo flexibilidade
        for t in self.__dao.get_all():
            if t.descricao.lower() == descricao.lower():
                return t
        return None

    def retornar(self):
        pass