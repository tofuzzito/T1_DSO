from classes.profissional_saude import ProfissionalSaude
from views.ProfissionalView import ProfissionalView
from DAOs.ProfissionalDAO import ProfissionalDAO


class ProfissionalController:
    def __init__(self):
        self.__dao = ProfissionalDAO()
        self.__view = ProfissionalView.getInstance()

    def abre_tela(self):
        lista_opcoes = {
            "Incluir Profissional": self.incluir,
            "Alterar Profissional": self.alterar,
            "Excluir Profissional": self.excluir,
            "Listar Profissionais": self.listar
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
        if not dados: return

        if self.busca_profissional(dados["cpf"]):
            self.__view.mostra_mensagem(
                "Profissional já cadastrado com esse CPF.")
            return

        # Criamos o objeto passando strings vazias na herança para evitar travas ocultas da classe Pessoa
        profissional = ProfissionalSaude(
            nome="",
            celular="",
            cpf="",
            especialidade=dados["especialidade"],
            registroProfissional=dados["registro_profissional"]
        )

        # Forçamos a gravação direta dos dados reais nos atributos do objeto (Ignorando travas do __init__ da herança)
        profissional.nome = dados["nome"]
        profissional.celular = dados["celular"]
        profissional.cpf = dados["cpf"]

        # Gravamos diretamente no DAO usando o Registro Profissional como chave
        self.__dao.add(profissional.registroProfissional, profissional)
        self.__view.mostra_mensagem("Profissional cadastrado com sucesso!")

    def alterar(self):
        cpf = self.__view.pega_cpf(motivo="alterar")
        if not cpf: return

        profissional = self.busca_profissional(cpf)
        if not profissional:
            self.__view.mostra_mensagem("Profissional não encontrado.")
            return

        dados_antigos = {
            "nome": getattr(profissional, 'nome', ''),
            "celular": getattr(profissional, 'celular', ''),
            "cpf": getattr(profissional, 'cpf', ''),
            "especialidade": getattr(profissional, 'especialidade', ''),
            "registro_professional": getattr(profissional,
                                             'registroProfissional', '')
        }

        dados = self.__view.pega_dados_formulario(dados_antigos)
        if not dados: return

        chave_antiga = profissional.registroProfissional
        if chave_antiga != dados["registro_profissional"]:
            self.__dao.remove(chave_antiga)

        profissional.nome = dados["nome"]
        profissional.celular = dados["celular"]
        profissional.cpf = dados["cpf"]
        profissional.especialidade = dados["especialidade"]
        profissional.registroProfissional = dados["registro_profissional"]

        self.__dao.add(profissional.registroProfissional, profissional)
        self.__view.mostra_mensagem("Profissional alterado com sucesso.")

    def excluir(self):
        cpf = self.__view.pega_cpf(motivo="excluir")
        if not cpf: return

        profissional = self.busca_profissional(cpf)
        if not profissional:
            self.__view.mostra_mensagem("Profissional não encontrado.")
            return

        self.__dao.remove(profissional.registroProfissional)
        self.__view.mostra_mensagem("Profissional removido com sucesso.")

    def listar(self):
        profissionais = self.__dao.get_all()
        if not profissionais:
            self.__view.mostra_mensagem("Nenhum profissional cadastrado.")
            return

        conteudo_lista = "=== LISTA DE PROFISSIONAIS ===\n\n"
        for prof in profissionais:
            nome = getattr(prof, 'nome', 'Não informado')
            cpf = getattr(prof, 'cpf', 'Não informado')
            esp = getattr(prof, 'especialidade', 'Não informado')
            reg = getattr(prof, 'registroProfissional', 'Não informado')

            conteudo_lista += (
                f"Nome: {nome} | CPF: {cpf}\n"
                f"Especialidade: {esp} | Registro: {reg}\n"
                f"----------------------------------------\n"
            )

        self.__view.mostra_mensagem(conteudo_lista)

    def busca_profissional(self, cpf):
        for prof in self.__dao.get_all():
            if str(getattr(prof, 'cpf', '')).strip() == str(cpf).strip():
                return prof
        return None