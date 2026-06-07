from datetime import datetime

class ClinicaView:

    def mostra_menu(self):

        print("\n=== CLÍNICAS ===")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        return input("Escolha uma opção: ")

    def pega_dados_clinica(self):

        nome = input("Nome: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")

        try:
            horarioAbertura = input(
                "Horário de abertura (HH:MM): "
            )

            horarioFechamento = input(
                "Horário de fechamento (HH:MM): "
            )

            datetime.strptime(
                horarioAbertura,
                "%H:%M"
            )

            datetime.strptime(
                horarioFechamento,
                "%H:%M"
            )

        except ValueError:

            self.mostra_mensagem(
                "Horário inválido. Use HH:MM."
            )

            return None

        return {
            "nome": nome,
            "cidade": cidade,
            "descricao": descricao,
            "horarioAbertura": horarioAbertura,
            "horarioFechamento": horarioFechamento
        }

    def pega_nome(self):

        return input("Nome da clínica: ")

    def mostra_clinica(self, clinica):

        print(
            f"Nome: {clinica.nome} | "
            f"Cidade: {clinica.cidade} | "
            f"Descrição: {clinica.descricao}"
        )

    def mostra_mensagem(self, mensagem):

        print(mensagem)