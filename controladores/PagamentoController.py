from datetime import datetime
from classes.pagamento import PagamentoPix, PagamentoDinheiro, PagamentoCartao
from views.PagamentoView import PagamentoView


class PagamentoController:
    def __init__(self):
        self.__view = PagamentoView()

    def processar_pagamento(self, saldo_restante: float):
        """
        Interage com a View para capturar os dados, valida os limites financeiros 
        e retorna a instância polimórfica correta sem associar diretamente.
        """
        opcao = self.__view.escolhe_modalidade()

        if opcao == "0" or opcao not in ["1", "2", "3"]:
            return None

        dados_comuns = self.__view.pega_dados_comuns()

        # Proteção se fechar a janela ou clicar em Cancelar
        if not dados_comuns or dados_comuns["valorPago"] == -1.0:
            return None

        if dados_comuns["valorPago"] <= 0:
            self.__view.mostra_mensagem(
                "Erro: O valor do pagamento deve ser maior que zero.")
            return None

        if dados_comuns["valorPago"] > saldo_restante:
            self.__view.mostra_mensagem(
                f"Erro: O valor pago (R$ {dados_comuns['valorPago']:.2f}) "
                f"não pode ser maior que o saldo restante (R$ {saldo_restante:.2f}).")
            return None

        try:
            data_pagamento = datetime.strptime(dados_comuns["data"],
                                               "%Y-%m-%d").date()
        except (ValueError, TypeError):
            self.__view.mostra_mensagem(
                "Erro: Formato de data inválido (Use AAAA-MM-DD).")
            return None

        # Instanciação Polimórfica
        if opcao == "1":
            cpf_pagador = self.__view.pega_dados_pix()
            if not cpf_pagador: return None  # Proteção se cancelar
            return PagamentoPix(data_pagamento, dados_comuns["valorPago"],
                                cpf_pagador)

        elif opcao == "2":
            return PagamentoDinheiro(data_pagamento, dados_comuns["valorPago"])

        elif opcao == "3":
            dados_cartao = self.__view.pega_dados_cartao()
            # Proteção se cancelar no formulário do cartão
            if not dados_cartao or not dados_cartao[
                "numeroCartao"]: return None
            return PagamentoCartao(
                data_pagamento,
                dados_comuns["valorPago"],
                dados_cartao["numeroCartao"],
                dados_cartao["bandeira"]
            )

        return None