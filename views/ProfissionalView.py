import FreeSimpleGUI as sg


class ProfissionalView:
    __instance = None

    def __init__(self):
        if ProfissionalView.__instance is not None:
            raise Exception(
                "Esta classe é um Singleton! Use ProfissionalView.getInstance()")

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = ProfissionalView()
        return cls.__instance

    def mostra_tela(self):
        layout = [
            [sg.Text('=== GERENCIAR PROFISSIONAIS ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('Incluir Profissional', size=(25, 1))],
            [sg.Button('Alterar Profissional', size=(25, 1))],
            [sg.Button('Listar Profissionais', size=(25, 1))],
            [sg.Button('Excluir Profissional', size=(25, 1))],
            [sg.Button('Voltar', size=(25, 1),
                       button_color=('white', 'darkgray'))]
        ]

        window = sg.Window('Menu Profissionais', layout,
                           element_justification='c')
        botao, valores = window.read()
        window.close()
        return botao

    def pega_dados_formulario(self, dados_antigos=None):
        # Preenche com os dados antigos se for uma alteração
        nome_padrao = dados_antigos['nome'] if dados_antigos else ''
        celular_padrao = dados_antigos['celular'] if dados_antigos else ''
        cpf_padrao = dados_antigos['cpf'] if dados_antigos else ''
        esp_padrao = dados_antigos['especialidade'] if dados_antigos else ''
        registro_padrao = dados_antigos[
            'registro_professional'] if dados_antigos else ''

        layout = [
            [sg.Text('Nome:', size=(20, 1)),
             sg.InputText(nome_padrao, key='nome')],
            [sg.Text('Celular:', size=(20, 1)),
             sg.InputText(celular_padrao, key='celular')],
            # CPF fica desabilitado se for uma alteração (pois ele é a chave de busca do DAO)
            [sg.Text('CPF:', size=(20, 1)), sg.InputText(cpf_padrao, key='cpf',
                                                         disabled=(
                                                                     dados_antigos is not None))],
            [sg.Text('Especialidade:', size=(20, 1)),
             sg.InputText(esp_padrao, key='especialidade')],
            [sg.Text('Registro Profissional:', size=(20, 1)),
             sg.InputText(registro_padrao, key='registro_profissional')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Dados do Profissional', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar':
            return valores
        return None

    def pega_cpf(self, motivo="buscar"):
        layout = [
            [sg.Text(f'Digite o CPF do profissional que deseja {motivo}:')],
            [sg.InputText(key='cpf')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Buscar Profissional', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            return valores['cpf']
        return None

    def mostra_mensagem(self, mensagem: str):
        sg.popup(mensagem, title="Aviso")