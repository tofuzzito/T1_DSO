from classes.profissional_saude import ProfissionalSaude
from views.ProfissionalView import ProfissionalView


class ProfissionalController:

    def __init__(self):

        self.__profissionais = []
        self.__view = ProfissionalView()

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

        dados = self.__view.pega_dados_profissional()

        profissional = ProfissionalSaude(
            dados["nome"],
            dados["celular"],
            dados["cpf"],
            dados["especialidade"],
            dados["registro_profissional"]
        )

        if not profissional.validarCpf():

            self.__view.mostra_mensagem(
                "CPF inválido."
            )

            return

        self.__profissionais.append(profissional)

        self.__view.mostra_mensagem(
            "Profissional cadastrado com sucesso."
        )

    def alterar(self):

        cpf = self.__view.pega_cpf()

        profissional = self.busca_profissional(cpf)

        if profissional is None:

            self.__view.mostra_mensagem(
                "Profissional não encontrado."
            )

            return

        dados = self.__view.pega_dados_profissional()

        profissional.nome = dados["nome"]
        profissional.celular = dados["celular"]
        profissional.especialidade = dados["especialidade"]
        profissional.registro_profissional = dados["registro_profissional"]

        self.__view.mostra_mensagem(
            "Profissional alterado com sucesso."
        )

    def excluir(self):

        cpf = self.__view.pega_cpf()

        profissional = self.busca_profissional(cpf)

        if profissional is None:

            self.__view.mostra_mensagem(
                "Profissional não encontrado."
            )

            return

        self.__profissionais.remove(profissional)

        self.__view.mostra_mensagem(
            "Profissional removido."
        )

    def listar(self):

        if len(self.__profissionais) == 0:

            self.__view.mostra_mensagem(
                "Nenhum profissional cadastrado."
            )

            return

        for profissional in self.__profissionais:

            self.__view.mostra_profissional(
                profissional
            )

    def busca_profissional(self, cpf):

        for profissional in self.__profissionais:

            if profissional.cpf == cpf:
                return profissional

        return None

    def retornar(self):
        pass