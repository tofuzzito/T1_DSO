import FreeSimpleGUI as sg


class PagamentoView:
    def escolhe_modalidade(self) -> str:
        layout = [
            [sg.Text('=== MODALIDADES DE PAGAMENTO ===',
                     font=('Arial', 12, 'bold'))],
            [sg.Button('1', size=(5, 1)), sg.Text('Pix')],
            [sg.Button('2', size=(5, 1)), sg.Text('Dinheiro')],
            [sg.Button('3', size=(5, 1)), sg.Text('Cartão')],
            [sg.Button('0', size=(5, 1), button_color=('white', 'darkgray')),
             sg.Text('Cancelar')]
        ]

        window = sg.Window('Forma de Pagamento', layout)
        botao, valores = window.read()
        window.close()

        return botao if botao is not None else '0'

    def pega_dados_comuns(self) -> dict:
        layout = [
            [sg.Text('=== DADOS DO PAGAMENTO ===',
                     font=('Arial', 11, 'bold'))],
            [sg.Text('Data do Pagamento (AAAA-MM-DD):', size=(28, 1)),
             sg.InputText(key='data')],
            [sg.Text('Valor a ser Pago: R$', size=(28, 1)),
             sg.InputText(key='valor')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Dados Comuns', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar':
            # Substitui vírgula por ponto de forma amigável como no original
            valor_str = valores['valor'].replace(",", ".")
            try:
                valor = float(valor_str)
            except (ValueError, TypeError):
                valor = -1.0  # Força valor inválido controlado para o controller barrar

            return {"data": valores['data'], "valorPago": valor}

        return {"data": "", "valorPago": -1.0}

    def pega_dados_pix(self) -> str:
        layout = [
            [sg.Text('CPF do Pagador Pix:')],
            [sg.InputText(key='cpf')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Dados Pix', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            return valores['cpf']
        return ""

    def pega_dados_cartao(self) -> dict:
        layout = [
            [sg.Text('=== DADOS DO CARTÃO ===', font=('Arial', 11, 'bold'))],
            [sg.Text('Número do Cartão:', size=(15, 1)),
             sg.InputText(key='numeroCartao')],
            [sg.Text('Bandeira:', size=(15, 1)), sg.InputText(key='bandeira')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Dados Cartão', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar':
            return {"numeroCartao": valores['numeroCartao'],
                    "bandeira": valores['bandeira']}
        return {"numeroCartao": "", "bandeira": ""}

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Pagamentos")