from classes.clinica import Clinica
from views.ClinicaView import ClinicaView


class ClinicaController:

    def __init__(self):

        self.__clinicas = []
        self.__view = ClinicaView()

    def abre_tela(self):

        lista_opcoes = {
            "1": self.incluir,
            "2": self.alterar,
            "3": self.excluir,
            "4": self.listar,
            "0": self.retornar
        }

        while True:

            opcao = self.__view.mostra_menu()

            funcao = lista_opcoes.get(opcao)

            if funcao:
                funcao()

            if opcao == "0":
                break

    def incluir(self):

        dados = self.__view.pega_dados_clinica()

        if dados is None:
            return

        if self.busca_clinica(dados["nome"]):

            self.__view.mostra_mensagem(
                "Já existe uma clínica com esse nome."
            )

            return

        clinica = Clinica(
            dados["nome"],
            dados["cidade"],
            dados["descricao"],
            dados["horarioAbertura"],
            dados["horarioFechamento"]
        )

        self.__clinicas.append(clinica)

        self.__view.mostra_mensagem(
            "Clínica cadastrada com sucesso."
        )

    def alterar(self):

        nome = self.__view.pega_nome()

        clinica = self.busca_clinica(nome)

        if clinica is None:
            self.__view.mostra_mensagem(
                "Clínica não encontrada."
            )

            return

        dados = self.__view.pega_dados_clinica()

        if dados is None:
            return

        clinica.nome = dados["nome"]
        clinica.cidade = dados["cidade"]
        clinica.descricao = dados["descricao"]
        clinica.horarioAbertura = dados["horarioAbertura"]
        clinica.horarioFechamento = dados["horarioFechamento"]

        self.__view.mostra_mensagem(
            "Clínica alterada com sucesso."
        )

    def excluir(self):

        nome = self.__view.pega_nome()

        clinica = self.busca_clinica(nome)

        if clinica is None:

            self.__view.mostra_mensagem(
                "Clínica não encontrada."
            )

            return

        self.__clinicas.remove(clinica)

        self.__view.mostra_mensagem(
            "Clínica removida com sucesso."
        )

    def listar(self):

        if len(self.__clinicas) == 0:

            self.__view.mostra_mensagem(
                "Nenhuma clínica cadastrada."
            )

            return

        for clinica in self.__clinicas:

            self.__view.mostra_clinica(
                clinica
            )

    def busca_clinica(self, nome):

        for clinica in self.__clinicas:

            if clinica.nome.lower() == nome.lower():
                return clinica

        return None

    def retornar(self):
        pass