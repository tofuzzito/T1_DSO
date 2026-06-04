class PacienteView:

    def mostra_menu(self):
        print("\n=== PACIENTES ===")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        return input("Escolha uma opção: ")

    def pega_dados_paciente(self):
        print("\n=== DADOS DO PACIENTE ===")

        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF (somente números): ")
        data_nascimento = input("Data nascimento (AAAA-MM-DD): ")

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "data_nascimento": data_nascimento
        }

    def pega_cpf(self):
        return input("CPF do paciente: ")

    def mostra_paciente(self, paciente):
        print(
            f"Nome: {paciente.nome} | "
            f"CPF: {paciente.cpf} | "
            f"Celular: {paciente.celular}"
        )

    def mostra_mensagem(self, msg):
        print(msg)