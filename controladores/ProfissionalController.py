from classes.profissional_saude import ProfissionalSaude
from views.ProfissionalView import ProfissionalView
from DAOs.ProfissionalDAO import ProfissionalDAO

class ProfissionalController:
    def __init__(self):
        self.__dao = ProfissionalDAO()
        self.__view = ProfissionalView()

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
        dados = self.__view.pega_dados_profissional()
        
        if self.busca_profissional(dados["cpf"]):
            self.__view.mostra_mensagem("Profissional já cadastrado.")
            return

        profissional = ProfissionalSaude(
            dados["nome"], dados["celular"], dados["cpf"],
            dados["especialidade"], dados["registro_profissional"]
        )

        if not profissional.validarCpf():
            self.__view.mostra_mensagem("CPF inválido.")
            return

        self.__dao.add(profissional.registroProfissional, profissional)
        self.__view.mostra_mensagem("Profissional cadastrado com sucesso.")

    def alterar(self):
        cpf = self.__view.pega_cpf()
        profissional = self.busca_profissional(cpf)

        if not profissional:
            self.__view.mostra_mensagem("Profissional não encontrado.")
            return

        dados = self.__view.pega_dados_profissional()
        profissional.nome = dados["nome"]
        profissional.celular = dados["celular"]
        profissional.especialidade = dados["especialidade"]
        profissional.registroProfissional = dados["registro_profissional"]

        self.__dao.add(profissional.registroProfissional, profissional)
        self.__view.mostra_mensagem("Profissional alterado com sucesso.")

    def excluir(self):
        cpf = self.__view.pega_cpf()
        profissional = self.busca_profissional(cpf)
        
        if not profissional:
            self.__view.mostra_mensagem("Profissional não encontrado.")
            return

        self.__dao.remove(profissional.registroProfissional)
        self.__view.mostra_mensagem("Profissional removido.")

    def listar(self):
        profissionais = self.__dao.get_all()
        if not profissionais:
            self.__view.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        for prof in profissionais:
            self.__view.mostra_profissional(prof)

    def busca_profissional(self, cpf):
        # Como o DAO usa registro_profissional como chave, a busca por CPF 
        # precisa iterar sobre os objetos em cache
        for prof in self.__dao.get_all():
            if prof.cpf == cpf: return prof
        return None

    def retornar(self):
        pass