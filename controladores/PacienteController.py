from datetime import datetime
from classes.paciente import Paciente
from views.PacienteView import PacienteView
from DAOs.PacienteDAO import PacienteDAO


class PacienteController:
    def __init__(self, controlador_sistema=None):
        self.__controlador_sistema = controlador_sistema
        self.__dao = PacienteDAO()
        self.__view = PacienteView.getInstance()

    def abre_tela(self):
        lista_opcoes = {
            "Incluir Paciente": self.incluir,
            "Alterar Paciente": self.alterar,
            "Excluir Paciente": self.excluir,
            "Listar Pacientes": self.listar
        }
        while True:
            opcao = self.__view.mostra_tela()

            if opcao in (None, "Voltar"):
                break

            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()

    def incluir(self):
        dados = self.__view.pega_dados_formulario()

        if not dados:
            return

        if self.busca_paciente(dados["cpf"]):
            self.__view.mostra_mensagem("Paciente com este CPF já cadastrado!")
            return

        try:
            data_nascimento = datetime.strptime(dados["data_nascimento"],
                                                "%Y-%m-%d").date()
        except ValueError:
            self.__view.mostra_mensagem("Data inválida. Use AAAA-MM-DD.")
            return

        paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"],
                            data_nascimento)

        if not paciente.validarCpf():
            self.__view.mostra_mensagem("CPF inválido!")
            return

        if not paciente.maiorDeIdade():
            self.__view.mostra_mensagem("Paciente deve ser maior de idade.")
            return

        self.__dao.add(paciente)
        self.__view.mostra_mensagem("Paciente cadastrado com sucesso.")

    def alterar(self):
        cpf = self.__view.pega_cpf(motivo="alterar")
        if not cpf:
            return

        paciente = self.busca_paciente(cpf)
        if not paciente:
            self.__view.mostra_mensagem("Paciente não encontrado.")
            return

        dados = self.__view.pega_dados_formulario()
        if not dados:
            return

        paciente.nome = dados["nome"]
        paciente.celular = dados["celular"]

        self.__dao.add(paciente)
        self.__view.mostra_mensagem("Paciente alterado com sucesso.")

    def excluir(self):
        cpf = self.__view.pega_cpf(motivo="excluir")
        if not cpf:
            return

        if not self.busca_paciente(cpf):
            self.__view.mostra_mensagem("Paciente não encontrado.")
            return

        self.__dao.remove(cpf)
        self.__view.mostra_mensagem("Paciente removido.")

    def listar(self):
        pacientes = self.__dao.get_all()
        if not pacientes:
            self.__view.mostra_mensagem("Nenhum paciente cadastrado.")
            return

        conteudo_lista = "=== PACIENTES CADASTRADOS ===\n\n"
        for paciente in pacientes:
            conteudo_lista += f"Nome: {paciente.nome}\nCPF: {paciente.cpf}\nCelular: {paciente.celular}\n-----------------------\n"

        self.__view.mostra_mensagem(conteudo_lista)

    def busca_paciente(self, cpf):
        return self.__dao.get(cpf)