import FreeSimpleGUI as sg


class AtendimentoView:
    def mostra_menu(self) -> str:
        layout = [
            [sg.Text('=== GERENCIAR ATENDIMENTOS ===',
                     font=('Arial', 14, 'bold'))],
            [sg.Button('1', size=(5, 1)), sg.Text('Incluir Atendimento')],
            [sg.Button('2', size=(5, 1)), sg.Text('Alterar Horários')],
            [sg.Button('3', size=(5, 1)), sg.Text('Excluir Atendimento')],
            [sg.Button('4', size=(5, 1)), sg.Text('Listar Todos')],
            [sg.Button('5', size=(5, 1)),
             sg.Text('Adicionar Procedimento a um Atendimento')],
            [sg.Button('6', size=(5, 1)),
             sg.Text('Registrar/Adicionar Pagamento')],
            [sg.Button('0', size=(5, 1), button_color=('white', 'darkgray')),
             sg.Text('Voltar')]
        ]

        window = sg.Window('Menu Atendimentos', layout)
        botao, valores = window.read()
        window.close()

        return botao if botao is not None else '0'

    def pega_dados_atendimento(self) -> dict:
        layout = [
            [sg.Text('=== NOVO ATENDIMENTO ===', font=('Arial', 12, 'bold'))],
            [sg.Text('Data (AAAA-MM-DD):', size=(28, 1)),
             sg.InputText(key='data')],
            [sg.Text('Horário de Início (HH:MM):', size=(28, 1)),
             sg.InputText(key='horarioInicio')],
            [sg.Text('Horário de Fim (HH:MM):', size=(28, 1)),
             sg.InputText(key='horarioFim')],
            [sg.Text('CPF do Paciente:', size=(28, 1)),
             sg.InputText(key='cpf_paciente')],
            [sg.Text('Nome da Clínica:', size=(28, 1)),
             sg.InputText(key='nome_clinica')],
            [sg.Text('Descrição do Tipo Atend.:', size=(28, 1)),
             sg.InputText(key='desc_tipo')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastrar Atendimento', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar':
            return valores
        return None

    def pega_id_atendimento(self) -> int:
        layout = [
            [sg.Text('Digite o ID do Atendimento:')],
            [sg.InputText(key='id')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Selecionar Atendimento', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            try:
                return int(valores['id'])
            except (ValueError, TypeError):
                return -1
        return -1

    def pega_dados_alteracao(self) -> dict:
        layout = [
            [sg.Text('=== ALTERAR HORÁRIOS ===', font=('Arial', 12, 'bold'))],
            [sg.Text('Novo Horário de Início (HH:MM):', size=(28, 1)),
             sg.InputText(key='horarioInicio')],
            [sg.Text('Novo Horário de Fim (HH:MM):', size=(28, 1)),
             sg.InputText(key='horarioFim')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Alterar Horários', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'Confirmar':
            return valores
        return None

    def pega_descricao_procedimento(self) -> str:
        layout = [
            [sg.Text('Descrição do Procedimento a incluir:')],
            [sg.InputText(key='descricao')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Adicionar Procedimento', layout)
        botao, valores = window.read()
        window.close()

        if botao == 'OK':
            return valores['descricao']
        return None

    def mostra_atendimento(self, idx: int, atendimento, valor_total: float,
                           saldo_restante: float):
        # Esse método não será mais muito usado de forma isolada,
        # pois vamos centralizar no método listar do Controller,
        # mas mantive o popup individual por compatibilidade.
        procedimentos_desc = [p.descricao for p in
                              sorted(atendimento.procedimentos,
                                     key=lambda x: x.custo)]
        info = (
            f"[ID: {idx}] Data: {atendimento.data} | Horário: {atendimento.horarioInicio} - {atendimento.horarioFim}\n"
            f"Clínica: {atendimento.clinica.nome} | Paciente: {atendimento.paciente.nome}\n"
            f"Tipo: {atendimento.tipoAtendimento.descricao}\n"
            f"Procedimentos ({len(atendimento.procedimentos)}): {procedimentos_desc if procedimentos_desc else 'Nenhum'}\n"
            f"Valor Base: R$ {atendimento.valor:.2f} | Valor Total: R$ {valor_total:.2f}\n"
            f"Saldo Restante a Pagar: R$ {saldo_restante:.2f}"
        )
        sg.popup(info, title=f"Atendimento ID {idx}")

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Aviso")