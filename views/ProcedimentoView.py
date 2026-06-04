class ProcedimentoView:

    def mostra_menu(self):

        print("\n=== PROCEDIMENTOS ===")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        return input("Escolha uma opção: ")

    def pega_dados_procedimento(self):

        print("\n=== DADOS DO PROCEDIMENTO ===")

        descricao = input("Descrição: ")
        custo = float(input("Custo: "))
        cpf_profissional = input(
            "CPF do profissional responsável: "
        )

        return {
            "descricao": descricao,
            "custo": custo,
            "cpf_profissional": cpf_profissional
        }

    def pega_descricao(self):

        return input(
            "Descrição do procedimento: "
        )

    def mostra_procedimento(self, procedimento):

        print(
            f"Descrição: {procedimento.descricao}\n"
            f"Custo: R$ {procedimento.custo:.2f}\n"
            f"Profissional: {procedimento.profissional.nome}\n"
        )

    def mostra_mensagem(self, mensagem):

        print(mensagem)