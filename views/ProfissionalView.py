class ProfissionalView:

    def mostra_menu(self):
        print("\n=== PROFISSIONAIS ===")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        return input("Escolha uma opção: ")

    def pega_dados_profissional(self):

        print("\n=== DADOS DO PROFISSIONAL ===")

        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro_profissional = input("Registro profissional: ")

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "especialidade": especialidade,
            "registro_profissional": registro_profissional
        }

    def pega_cpf(self):
        return input("CPF do profissional: ")

    def mostra_profissional(self, profissional):

        print(
            f"Nome: {profissional.nome} | "
            f"CPF: {profissional.cpf} | "
            f"Especialidade: {profissional.especialidade} | "
            f"Registro: {profissional.registroProfissional}"
        )

    def mostra_mensagem(self, mensagem):
        print(mensagem)