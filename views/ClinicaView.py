from datetime import datetime
import FreeSimpleGUI as sg


class ClinicaView:
    __instance = None

    def __init__(self):
        if ClinicaView.__instance is not None:
            raise Exception(
                "Esta classe é um Singleton! Use ClinicaView.getInstance()")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = ClinicaView()
        return cls.__instance

    def mostra_tela(self):
        layout = [
            [sg.Text('=== GERENCIAR CLÍNICAS ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('Incluir Clínica', size=(25, 1))],
            [sg.Button('Alterar Clínica', size=(25, 1))],
            [sg.Button('Listar Clínicas', size=(25, 1))],
            [sg.Button('Excluir Clínica', size=(25, 1))],
            [sg.Button('Voltar', size=(25, 1),
                       button_color=('white', 'darkgray'))]
        ]

        window = sg.Window('Menu Clínicas', layout, element_justification='c')
        botao, valores = window.read()
        window.close()
        return botao

    def pega_dados_formulario(self, dados_antigos=None):
        # Se for alteração, preenche com os dados antigos, senão deixa vazio
        nome_padrao = dados_antigos['nome'] if dados_antigos else ''
        cidade_padrao = dados_antigos['cidade'] if dados_antigos else ''
        desc_padrao = dados_antigos['descricao'] if dados_antigos else ''
        abertura_padrao = dados_antigos[
            'horarioAbertura'] if dados_antigos else ''
        fechamento_padrao = dados_antigos[
            'horarioFechamento'] if dados_antigos else ''

        layout = [
            [sg.Text('Nome:', size=(25, 1)),
             sg.InputText(nome_padrao, key='nome',
                          disabled=(dados_antigos is not None))],
            [sg.Text('Cidade:', size=(25, 1)),
             sg.InputText(cidade_padrao, key='cidade')],
            [sg.Text('Descrição:', size=(25, 1)),
             sg.InputText(desc_padrao, key='descricao')],
            [sg.Text('Horário de abertura (HH:MM):', size=(25, 1)),
             sg.InputText(abertura_padrao, key='horarioAbertura')],
            [sg.Text('Horário de fechamento (HH:MM):', size=(25, 1)),
             sg.InputText(fechamento_padrao, key='horarioFechamento')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Dados da Clínica', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar':
            # Mantém a validação de horário idêntica à que você tinha no terminal
            try:
                datetime.strptime(valores['horarioAbertura'], "%H:%M")
                datetime.strptime(valores['horarioFechamento'], "%H:%M")
                return valores
            except ValueError:
                self.mostra_mensagem("Horário inválido. Use o formato HH:MM.")
                return None
        return None

    def pega_nome(self, motivo="buscar"):
        layout = [
            [sg.Text(f'Digite o Nome da clínica que deseja {motivo}:')],
            [sg.InputText(key='nome')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Buscar Clínica', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            return valores['nome']
        return None

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="Aviso")