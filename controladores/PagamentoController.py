from datetime import datetime
from classes.pagamento import PagamentoPix, PagamentoDinheiro, PagamentoCartao
from views.PagamentoView import PagamentoView

class PagamentoController:
    def __init__(self):
        self.__view = PagamentoView()

    def registrar_pagamento(self, atendimento, saldo_restante: float):
        """
        Recebe o atendimento selecionado e o saldo devedor atual.
        Cria a instância correta de pagamento e associa ao atendimento.
        """
        if saldo_restante <= 0:
            self.__view.mostra_mensagem("Este atendimento já está totalmente quitado!")
            return

        opcao = self.__view.escolhe_modalidade()
        
        if opcao == "0" or opcao not in ["1", "2", "3"]:
            self.__view.mostra_mensagem("Operação cancelada ou opção inválida.")
            return

        # Pega os dados comuns a todas as modalidades (Data e Valor)
        dados_comuns = self.__view.pega_dados_comuns()
        
        # Validação básica de valor
        if dados_comuns["valorPago"] <= 0:
            self.__view.mostra_mensagem("Erro: O valor do pagamento deve ser maior que zero.")
            return
            
        if dados_comuns["valorPago"] > saldo_restante:
            self.__view.mostra_mensagem(f"Erro: O valor pago (R$ {dados_comuns['valorPago']:.2f}) "
                                        f"não pode ser maior que o saldo restante (R$ {saldo_restante:.2f}).")
            return

        # Converte a string de data para objeto date
        try:
            data_pagamento = datetime.strptime(dados_comuns["data"], "%Y-%m-%d").date()
        except ValueError:
            self.__view.mostra_mensagem("Erro: Formato de data inválido (Use AAAA-MM-DD).")
            return

        novo_pagamento = None

        # 1 - PIX
        if opcao == "1":
            cpf_pagador = self.__view.pega_dados_pix()
            novo_pagamento = PagamentoPix(data_pagamento, dados_comuns["valorPago"], cpf_pagador)
        
        # 2 - DINHEIRO
        elif opcao == "2":
            novo_pagamento = PagamentoDinheiro(data_pagamento, dados_comuns["valorPago"])
        
        # 3 - CARTÃO
        elif opcao == "3":
            dados_cartao = self.__view.pega_dados_cartao()
            novo_pagamento = PagamentoCartao(
                data_pagamento, 
                dados_comuns["valorPago"], 
                dados_cartao["numeroCartao"], 
                dados_cartao["bandeira"]
            )

        if novo_pagamento:
            # Vincula o pagamento ao atendimento (Regra de Negócio / Composição)
            atendimento.adicionar_pagamento(novo_pagamento)
            self.__view.mostra_mensagem(f"Pagamento de R$ {dados_comuns['valorPago']:.2f} registrado com sucesso!")