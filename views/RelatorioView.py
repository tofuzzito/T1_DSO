import FreeSimpleGUI as sg


class RelatorioView:
    def mostra_menu(self) -> str:
        layout = [
            [sg.Text('=== CENTRAL DE RELATÓRIOS ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('1', size=(5, 1)),
             sg.Text('Clínicas com maior número de atendimentos')],
            [sg.Button('2', size=(5, 1)),
             sg.Text('Atendimentos mais caros e mais baratos')],
            [sg.Button('3', size=(5, 1)),
             sg.Text('Procedimentos mais realizados')],
            [sg.Button('4', size=(5, 1)),
             sg.Text('Procedimentos mais caros e mais baratos')],
            [sg.Button('0', size=(5, 1), button_color=('white', 'darkgray')),
             sg.Text('Voltar')]
        ]

        window = sg.Window('Central de Relatórios', layout)
        botao, valores = window.read()
        window.close()

        return botao if botao is not None else '0'

    def mostra_ranking_clinicas(self, ranking: list):
        texto = "--- CLÍNICAS COM MAIOR NÚMERO DE ATENDIMENTOS ---\n\n"
        for i, (nome, qtd) in enumerate(ranking, 1):
            texto += f"{i}º. Clínica: {nome} | Total de Atendimentos: {qtd}\n"

        sg.popup_scrolled(texto, title="Relatório de Clínicas", size=(60, 15))

    def mostra_extremos_atendimentos(self, mais_caros: list,
                                     mais_baratos: list):
        texto = "--- ATENDIMENTOS MAIS CAROS ---\n"
        for idx, valor in mais_caros:
            texto += f"ID Atendimento: {idx} | Valor Total: R$ {valor:.2f}\n"

        texto += "\n--- ATENDIMENTOS MAIS BARATOS ---\n"
        for idx, valor in mais_baratos:
            texto += f"ID Atendimento: {idx} | Valor Total: R$ {valor:.2f}\n"

        sg.popup_scrolled(texto, title="Extremos de Atendimentos",
                          size=(60, 15))

    def mostra_ranking_procedimentos(self, ranking: list):
        texto = "--- PROCEDIMENTOS MAIS REALIZADOS ---\n\n"
        for i, (desc, qtd) in enumerate(ranking, 1):
            texto += f"{i}º. Procedimento: {desc} | Total de Vezes: {qtd}\n"

        sg.popup_scrolled(texto, title="Ranking de Procedimentos",
                          size=(60, 15))

    def mostra_extremos_procedimentos(self, mais_caros: list,
                                      mais_baratos: list):
        texto = "--- PROCEDIMENTOS MAIS CAROS (POR CUSTO UNITÁRIO) ---\n"
        for p in mais_caros:
            texto += f"Procedimento: {p.descricao} | Custo: R$ {p.custo:.2f}\n"

        texto += "\n--- PROCEDIMENTOS MAIS BARATOS (POR CUSTO UNITÁRIO) ---\n"
        for p in mais_baratos:
            texto += f"Procedimento: {p.descricao} | Custo: R$ {p.custo:.2f}\n"

        sg.popup_scrolled(texto, title="Extremos de Procedimentos",
                          size=(60, 15))

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Aviso")