from classes.procedimento import Procedimento
from views.ProcedimentoView import ProcedimentoView


class ProcedimentoController:

    def __init__(self, controlador_profissionais):

        self.__procedimentos = []
        self.__view = ProcedimentoView()

        self.__controlador_profissionais = (
            controlador_profissionais
        )

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

        dados = self.__view.pega_dados_procedimento()

        if self.busca_procedimento(
                dados["descricao"]):

            self.__view.mostra_mensagem(
                "Procedimento já cadastrado."
            )

            return

        profissional = (
            self.__controlador_profissionais
            .busca_profissional(
                dados["cpf_profissional"]
            )
        )

        if profissional is None:

            self.__view.mostra_mensagem(
                "Profissional não encontrado."
            )

            return

        if dados["custo"] <= 0:

            self.__view.mostra_mensagem(
                "Custo inválido."
            )

            return

        procedimento = Procedimento(
            dados["descricao"],
            dados["custo"],
            profissional
        )

        self.__procedimentos.append(
            procedimento
        )

        self.__view.mostra_mensagem(
            "Procedimento cadastrado."
        )

    def alterar(self):

        descricao = (
            self.__view.pega_descricao()
        )

        procedimento = (
            self.busca_procedimento(
                descricao
            )
        )

        if procedimento is None:

            self.__view.mostra_mensagem(
                "Procedimento não encontrado."
            )

            return

        dados = (
            self.__view.pega_dados_procedimento()
        )

        profissional = (
            self.__controlador_profissionais
            .busca_profissional(
                dados["cpf_profissional"]
            )
        )

        if profissional is None:

            self.__view.mostra_mensagem(
                "Profissional não encontrado."
            )

            return

        procedimento.descricao = (
            dados["descricao"]
        )

        procedimento.custo = (
            dados["custo"]
        )

        procedimento.profissional = (
            profissional
        )

        self.__view.mostra_mensagem(
            "Procedimento alterado."
        )

    def excluir(self):

        descricao = (
            self.__view.pega_descricao()
        )

        procedimento = (
            self.busca_procedimento(
                descricao
            )
        )

        if procedimento is None:

            self.__view.mostra_mensagem(
                "Procedimento não encontrado."
            )

            return

        self.__procedimentos.remove(
            procedimento
        )

        self.__view.mostra_mensagem(
            "Procedimento removido."
        )

    def listar(self):

        if len(
            self.__procedimentos
        ) == 0:

            self.__view.mostra_mensagem(
                "Nenhum procedimento cadastrado."
            )

            return

        for procedimento in (
            self.__procedimentos
        ):

            self.__view.mostra_procedimento(
                procedimento
            )

    def busca_procedimento(
            self,
            descricao
    ):

        for procedimento in (
            self.__procedimentos
        ):

            if (
                procedimento.descricao
                .lower()
                ==
                descricao.lower()
            ):
                return procedimento

        return None

    def retornar(self):
        pass