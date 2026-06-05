class TipoAtendimentoView:
    def mostra_menu(self) -> str:
        print("\n=== TIPOS DE ATENDIMENTO ===")
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        return input("Escolha uma opção: ")

    def pega_dados(self) -> dict:
        print("\n=== DADOS DO TIPO DE ATENDIMENTO ===")
        descricao = input("Descrição (ex: Consulta, Exame, Retorno): ")
        return {"descricao": descricao}

    def pega_descricao(self) -> str:
        return input("Digite a descrição do Tipo de Atendimento: ")

    def mostra_tipo(self, tipo):
        print(f"Descrição: {tipo.descricao}")

    def mostra_mensagem(self, msg: str):
        print(msg)