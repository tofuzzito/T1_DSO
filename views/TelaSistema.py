import FreeSimpleGUI as sg


class SistemaView:
    def mostra_menu_principal(self):
        layout = [
            [sg.Text('=== MENU PRINCIPAL - SISTEMA CLÍNICAS ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('Clínicas', size=(25, 1))],
            [sg.Button('Pacientes', size=(25, 1))],
            [sg.Button('Profissionais', size=(25, 1))],
            [sg.Button('Procedimentos', size=(25, 1))],
            [sg.Button('Tipos de Atendimento', size=(25, 1))],
            [sg.Button('Atendimentos', size=(25, 1))],
            [sg.Button('Relatórios', size=(25, 1))],
            [sg.Button('Sair', size=(25, 1),
                       button_color=('white', 'darkred'))]
        ]

        window = sg.Window('Sistema de Atendimento', layout,
                           element_justification='c')
        botao, valores = window.read()
        window.close()
        return botao

    def mostra_mensagem_encerramento(self):
        sg.popup("Encerrando o sistema. Até logo!", title="Fim")