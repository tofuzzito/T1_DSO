from classes.clinica import Clinica
from views.ClinicaView import ClinicaView
from DAOs.ClinicaDAO import ClinicaDAO

class ClinicaController:
    def __init__(self):
        self.__dao = ClinicaDAO()
        self.__view = ClinicaView()

    def abre_tela(self):
        lista_opcoes = {
            "1": self.incluir, "2": self.alterar, 
            "3": self.excluir, "4": self.listar, "0": self.retornar
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
        if not dados: return

        if self.busca_clinica(dados["nome"]):
            self.__view.mostra_mensagem("Já existe uma clínica com esse nome.")
            return

        clinica = Clinica(dados["nome"], dados["cidade"], dados["descricao"], 
                          dados["horarioAbertura"], dados["horarioFechamento"])
        
        self.__dao.add(clinica.nome, clinica)
        self.__view.mostra_mensagem("Clínica cadastrada com sucesso.")

    def alterar(self):
        nome = self.__view.pega_nome()
        clinica = self.busca_clinica(nome)

        if not clinica:
            self.__view.mostra_mensagem("Clínica não encontrada.")
            return

        dados = self.__view.pega_dados_clinica()
        if not dados: return

        if clinica.nome.lower() != dados["nome"].lower():
            self.__dao.remove(clinica.nome)

        clinica.nome = dados["nome"]
        clinica.cidade = dados["cidade"]
        clinica.descricao = dados["descricao"]
        clinica.horarioAbertura = dados["horarioAbertura"]
        clinica.horarioFechamento = dados["horarioFechamento"]

        self.__dao.add(clinica.nome, clinica)
        self.__view.mostra_mensagem("Clínica alterada com sucesso.")

    def excluir(self):
        nome = self.__view.pega_nome()
        if not self.busca_clinica(nome):
            self.__view.mostra_mensagem("Clínica não encontrada.")
            return

        self.__dao.remove(nome)
        self.__view.mostra_mensagem("Clínica removida com sucesso.")

    def listar(self):
        clinicas = self.__dao.get_all()
        if not clinicas:
            self.__view.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        for clinica in clinicas:
            self.__view.mostra_clinica(clinica)

    def busca_clinica(self, nome):
        return self.__dao.get(nome)

    def retornar(self):
        pass