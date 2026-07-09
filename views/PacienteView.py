import FreeSimpleGUI as sg


class PacienteView:
    __instance = None

    def __init__(self):
        if PacienteView.__instance is not None:
            raise Exception(
                "Esta classe é um Singleton! Use PacienteView.getInstance()")
        self.__window = None  # Atributo window do diagrama
        PacienteView.__instance = self

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = PacienteView()
        return cls.__instance

    def mostra_tela(self):
        """Janela principal do menu de Pacientes"""
        layout = [
            [sg.Text('=== GERENCIAMENTO DE PACIENTES ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('Incluir Paciente', size=(25, 1))],
            [sg.Button('Alterar Paciente', size=(25, 1))],
            [sg.Button('Excluir Paciente', size=(25, 1))],
            [sg.Button('Listar Pacientes', size=(25, 1))],
            [sg.Button('Voltar', size=(25, 1),
                       button_color=('white', 'darkred'))]
        ]

        self.__window = sg.Window('Menu Pacientes', layout,
                                  element_justification='c')
        botao, valores = self.__window.read()
        self.__window.close()
        return botao

    def pega_dados_formulario(self):
        """Retorna um dicionário com os dados digitados ou None se cancelado"""
        layout = [
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText(key='cpf')],
            [sg.Text('Celular:', size=(15, 1)), sg.InputText(key='celular')],
            [sg.Text('Data Nasc. (AAAA-MM-DD):', size=(20, 1)),
             sg.InputText(key='data_nascimento')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        janela = sg.Window('Cadastro de Paciente', layout)
        botao, valores = janela.read()
        janela.close()

        if botao == 'Confirmar':
            return valores  # Retorna o dict solicitado pelo método do diagrama
        return None

    def mostra_mensagem(self, mensagem: str):
        """Exibe popups de aviso, sucesso ou erro"""
        sg.popup(mensagem, title="Aviso")

    def pega_cpf(self, motivo="buscar"):
        layout = [
            [sg.Text(f'Digite o CPF do paciente que deseja {motivo}:')],
            [sg.InputText(key='cpf')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        janela = sg.Window('Buscar Paciente', layout)
        botao, valores = janela.read()  # Aqui foi definido como 'valores'
        janela.close()

        if botao == 'OK':
            return valores['cpf']  # Corrigido aqui de 'values' para 'valores'
        return None