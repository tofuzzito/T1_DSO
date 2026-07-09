from classes.clinica import Clinica
from views.ClinicaView import ClinicaView
from DAOs.ClinicaDAO import ClinicaDAO


class ClinicaController:
    def __init__(self):
        self.__dao = ClinicaDAO()
        # Atualizado para usar o padrão Singleton exigido
        self.__view = ClinicaView.getInstance()

    def abre_tela(self):
        # Chaves alteradas dos números para os textos exatos dos botões da interface gráfica
        lista_opcoes = {
            "Incluir Clínica": self.incluir,
            "Alterar Clínica": self.alterar,
            "Excluir Clínica": self.excluir,
            "Listar Clínicas": self.listar
        }
        while True:
            # Chama o método da nova view gráfica
            opcao = self.__view.mostra_tela()

            # Condição de parada caso clique em 'Voltar' ou feche no 'X' (None)
            if opcao in (None, "Voltar"):
                break

            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()

    def incluir(self):
        # Método atualizado para capturar o formulário gráfico
        dados = self.__view.pega_dados_formulario()
        if not dados: return

        if self.busca_clinica(dados["nome"]):
            self.__view.mostra_mensagem("Já existe uma clínica com esse nome.")
            return

        clinica = Clinica(dados["nome"], dados["cidade"], dados["descricao"],
                          dados["horarioAbertura"], dados["horarioFechamento"])

        # Ajustado para salvar usando o objeto (se o seu DAO exigir a chave antes, mantenha 'clinica.nome, clinica')
        self.__dao.add(clinica.nome, clinica)
        self.__view.mostra_mensagem("Clínica cadastrada com sucesso.")

    def alterar(self):
        # Adicionado o parâmetro motivo para avisar o usuário na janela gráfica
        nome = self.__view.pega_nome(motivo="alterar")
        if not nome: return

        clinica = self.busca_clinica(nome)

        if not clinica:
            self.__view.mostra_mensagem("Clínica não encontrada.")
            return

        # Passa os dados antigos para preencher automaticamente os campos da janela gráfica
        dados_antigos = {
            "nome": clinica.nome,
            "cidade": clinica.cidade,
            "descricao": clinica.descricao,
            "horarioAbertura": clinica.horarioAbertura,
            "horarioFechamento": clinica.horarioFechamento
        }

        dados = self.__view.pega_dados_formulario(dados_antigos)
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
        # Adicionado o parâmetro motivo para avisar o usuário na janela gráfica
        nome = self.__view.pega_nome(motivo="excluir")
        if not nome: return

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

        # Concatena todas as clínicas em uma única String para exibir em um popup gráfico de uma vez só
        conteudo_lista = "=== LISTA DE CLÍNICAS ===\n\n"
        for clinica in clinicas:
            conteudo_lista += (
                f"Nome: {clinica.nome} | "
                f"Cidade: {clinica.cidade} | "
                f"Descrição: {clinica.descricao}\n"
                f"Abertura: {clinica.horarioAbertura} | Fechamento: {clinica.horarioFechamento}\n"
                f"----------------------------------------\n"
            )

        self.__view.mostra_mensagem(conteudo_lista)

    def busca_clinica(self, nome):
        return self.__dao.get(nome)