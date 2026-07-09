import FreeSimpleGUI as sg


class TipoAtendimentoView:
    def mostra_menu(self) -> str:
        layout = [
            [sg.Text('=== TIPOS DE ATENDIMENTO ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('1', size=(5, 1)), sg.Text('Incluir')],
            [sg.Button('2', size=(5, 1)), sg.Text('Alterar')],
            [sg.Button('3', size=(5, 1)), sg.Text('Excluir')],
            [sg.Button('4', size=(5, 1)), sg.Text('Listar')],
            [sg.Button('0', size=(5, 1), button_color=('white', 'darkgray')),
             sg.Text('Voltar')]
        ]

        window = sg.Window('Menu Tipos de Atendimento', layout)
        botao, valores = window.read()
        window.close()

        # Se fechar a janela no X, retorna '0' para voltar com segurança
        return botao if botao is not None else '0'

    def pega_dados(self) -> dict:
        layout = [
            [sg.Text('=== DADOS DO TIPO DE ATENDIMENTO ===',
                     font=('Arial', 12, 'bold'))],
            [sg.Text('Descrição (ex: Consulta, Exame):', size=(30, 1))],
            [sg.InputText(key='descricao')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastrar Tipo de Atendimento', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar' and valores['descricao'].strip() != '':
            return {"descricao": valores['descricao']}
        return None

    def pega_descricao(self) -> str:
        layout = [
            [sg.Text('Digite a descrição do Tipo de Atendimento:')],
            [sg.InputText(key='descricao')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Buscar Tipo de Atendimento', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            return valores['descricao']
        return None

    def mostra_tipo(self, tipo):
        info = f"• Descrição: {tipo.descricao}"
        sg.popup(info, title="Tipo de Atendimento")

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Aviso")