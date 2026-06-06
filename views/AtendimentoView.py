class AtendimentoView:
    def mostra_menu(self) -> str:
        print("\n=== ATENDIMENTOS ===")
        print("1 - Incluir Atendimento")
        print("2 - Alterar Horários")
        print("3 - Excluir Atendimento")
        print("4 - Listar Todos")
        print("5 - Adicionar Procedimento a um Atendimento")
        print("6 - Registrar/Adicionar Pagamento")
        print("0 - Voltar")
        return input("Escolha uma opção: ")

    def pega_dados_atendimento(self) -> dict:
        print("\n=== NOVO ATENDIMENTO ===")
        data = input("Data (AAAA-MM-DD): ")
        horario_inicio = input("Horário de Início (HH:MM): ")
        horario_fim = input("Horário de Fim (HH:MM): ")
        cpf_paciente = input("CPF do Paciente: ")
        nome_clinica = input("Nome da Clínica: ")
        desc_tipo = input("Descrição do Tipo de Atendimento: ")
        return {
            "data": data,
            "horarioInicio": horario_inicio,
            "horarioFim": horario_fim,
            "cpf_paciente": cpf_paciente,
            "nome_clinica": nome_clinica,
            "desc_tipo": desc_tipo
        }

    def pega_id_atendimento(self) -> int:
        """Proteção contra erros de digitação de ID numérico"""
        try:
            return int(input("Digite o ID do Atendimento: "))
        except (ValueError, TypeError):
            return -1  # Retorna ID inválido controlado para o Except do Controller tratar

    def pega_dados_alteracao(self) -> dict:
        print("\n=== ALTERAR HORÁRIOS ===")
        horario_inicio = input("Novo Horário de Início (HH:MM): ")
        horario_fim = input("Novo Horário de Fim (HH:MM): ")
        return {"horarioInicio": horario_inicio, "horarioFim": horario_fim}

    def pega_descricao_procedimento(self) -> str:
        return input("Descrição do Procedimento a incluir: ")

    def mostra_atendimento(self, idx: int, atendimento, valor_total: float, saldo_restante: float):
        print(f"\n[ID: {idx}] Data: {atendimento.data} | Horário: {atendimento.horarioInicio} - {atendimento.horarioFim}")
        print(f"Clínica: {atendimento.clinica.nome} | Paciente: {atendimento.paciente.nome}")
        print(f"Tipo: {atendimento.tipoAtendimento.descricao}")
        
        # Exibição segura de listas vazias ou populadas
        procedimentos_desc = [p.descricao for p in sorted(atendimento.procedimentos, key=lambda x: x.custo)]
        print(f"Procedimentos ({len(atendimento.procedimentos)}): {procedimentos_desc if procedimentos_desc else 'Nenhum'}")
        
        print(f"Valor Base: R$ {atendimento.valor:.2f} | Valor Total (com procedimentos): R$ {valor_total:.2f}")
        print(f"Saldo Restante a Pagar: R$ {saldo_restante:.2f}")

    def mostra_mensagem(self, msg: str):
        print(msg)