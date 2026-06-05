class PagamentoView:
    def escolhe_modalidade(self) -> str:
        print("\n=== MODALIDADES DE PAGAMENTO ===")
        print("1 - Pix")
        print("2 - Dinheiro")
        print("3 - Cartão")
        print("0 - Cancelar")
        return input("Escolha a modalidade: ")

    def pega_dados_comuns(self) -> dict:
        data = input("Data do Pagamento (AAAA-MM-DD): ")
        valor = float(input("Valor a ser Pago: R$ "))
        return {"data": data, "valorPago": valor}

    def pega_dados_pix(self) -> str:
        return input("CPF do Pagador: ")

    def pega_dados_cartao(self) -> dict:
        numero = input("Número do Cartão: ")
        bandeira = input("Bandeira do Cartão: ")
        return {"numeroCartao": numero, "bandeira": bandeira}

    def mostra_mensagem(self, msg: str):
        print(msg)