from datetime import datetime
from classes.paciente import Paciente
from views.PacienteView import PacienteView
from DAOs.PacienteDAO import PacienteDAO

class PacienteController:
    def __init__(self):
        self.__dao = PacienteDAO()
        self.__view = PacienteView()

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
        dados = self.__view.pega_dados_paciente()
        
        if self.busca_paciente(dados["cpf"]):
            self.__view.mostra_mensagem("Paciente com este CPF já cadastrado!")
            return

        try:
            data_nascimento = datetime.strptime(dados["data_nascimento"], "%Y-%m-%d").date()
        except ValueError:
            self.__view.mostra_mensagem("Data inválida. Use AAAA-MM-DD.")
            return

        paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"], data_nascimento)

        if not paciente.validarCpf():
            self.__view.mostra_mensagem("CPF inválido!")
            return

        if not paciente.maiorDeIdade():
            self.__view.mostra_mensagem("Paciente deve ser maior de idade.")
            return

        self.__dao.add(paciente.cpf, paciente)
        self.__view.mostra_mensagem("Paciente cadastrado com sucesso.")

    def alterar(self):
        cpf = self.__view.pega_cpf()
        paciente = self.busca_paciente(cpf)

        if not paciente:
            self.__view.mostra_mensagem("Paciente não encontrado.")
            return

        dados = self.__view.pega_dados_paciente()
        paciente.nome = dados["nome"]
        paciente.celular = dados["celular"]
        
        self.__dao.add(paciente.cpf, paciente)
        self.__view.mostra_mensagem("Paciente alterado com sucesso.")

    def excluir(self):
        cpf = self.__view.pega_cpf()
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
        for paciente in pacientes:
            self.__view.mostra_paciente(paciente)

    def busca_paciente(self, cpf):
        return self.__dao.get(cpf)

    def retornar(self):
        pass