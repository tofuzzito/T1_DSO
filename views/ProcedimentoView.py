import FreeSimpleGUI as sg


class ProcedimentoView:

    def mostra_menu(self):
        layout = [
            [sg.Text('=== PROCEDIMENTOS ===', font=('Arial', 14, 'bold'))],
            [sg.Button('1', size=(5, 1)), sg.Text('Incluir')],
            [sg.Button('2', size=(5, 1)), sg.Text('Alterar')],
            [sg.Button('3', size=(5, 1)), sg.Text('Excluir')],
            [sg.Button('4', size=(5, 1)), sg.Text('Listar')],
            [sg.Button('0', size=(5, 1), button_color=('white', 'darkgray')),
             sg.Text('Voltar')]
        ]

        window = sg.Window('Menu Procedimentos', layout)
        botao, valores = window.read()
        window.close()

        # Se fechar no X, retorna '0' para voltar com segurança
        return botao if botao is not None else '0'

    def pega_dados_procedimento(self):
        layout = [
            [sg.Text('=== DADOS DO PROCEDIMENTO ===',
                     font=('Arial', 12, 'bold'))],
            [sg.Text('Descrição:', size=(25, 1)),
             sg.InputText(key='descricao')],
            [sg.Text('Custo:', size=(25, 1)), sg.InputText(key='custo')],
            [sg.Text('CPF do profissional responsável:', size=(25, 1)),
             sg.InputText(key='cpf_profissional')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastrar Procedimento', layout)
        botao, valores = window.read()
        window.close()

        if botao != 'Confirmar':
            return None

        try:
            custo = float(valores['custo'].replace(",", "."))
        except ValueError:
            self.mostra_mensagem("Custo inválido.")
            return None

        return {
            "descricao": valores['descricao'],
            "custo": custo,
            "cpf_profissional": valores['cpf_profissional']
        }

    def pega_descricao(self):
        layout = [
            [sg.Text('Descrição do procedimento:')],
            [sg.InputText(key='descricao')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Buscar Procedimento', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            return valores['descricao']
        return None

    def mostra_procedimento(self, procedimento):
        # Transforma o print antigo num popup formatado
        info = (
            f"Descrição: {procedimento.descricao}\n"
            f"Custo: R$ {procedimento.custo:.2f}\n"
            f"Profissional: {procedimento.profissional.nome}\n"
        )
        sg.popup(info, title="Dados do Procedimento")

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem, title="Aviso")