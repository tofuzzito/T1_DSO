class RelatorioView:
    def mostra_menu(self) -> str:
        print("\n=== RELATÓRIOS DO SISTEMA ===")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Voltar")
        return input("Escolha uma opção: ")

    def mostra_ranking_clinicas(self, ranking: list):
        print("\n--- CLÍNICAS COM MAIOR NÚMERO DE ATENDIMENTOS ---")
        for i, (nome, qtd) in enumerate(ranking, 1):
            print(f"{i}º. Clínica: {nome} | Total de Atendimentos: {qtd}")

    def mostra_extremos_atendimentos(self, mais_caros: list, mais_baratos: list):
        print("\n--- ATENDIMENTOS MAIS CAROS ---")
        for idx, valor in mais_caros:
            print(f"ID Atendimento: {idx} | Valor Total: R$ {valor:.2f}")
            
        print("\n--- ATENDIMENTOS MAIS BARATOS ---")
        # Removido o reversed() duplicado para evitar misturar ordens com poucos dados
        for idx, valor in mais_baratos:
            print(f"ID Atendimento: {idx} | Valor Total: R$ {valor:.2f}")

    def mostra_ranking_procedimentos(self, ranking: list):
        print("\n--- PROCEDIMENTOS MAIS REALIZADOS ---")
        for i, (desc, qtd) in enumerate(ranking, 1):
            print(f"{i}º. Procedimento: {desc} | Total de Vezes: {qtd}")

    def mostra_extremos_procedimentos(self, mais_caros: list, mais_baratos: list):
        print("\n--- PROCEDIMENTOS MAIS CAROS (POR CUSTO UNITÁRIO) ---")
        for p in mais_caros:
            print(f"Procedimento: {p.descricao} | Custo: R$ {p.custo:.2f}")
            
        print("\n--- PROCEDIMENTOS MAIS BARATOS (POR CUSTO UNITÁRIO) ---")
        for p in mais_baratos:
            print(f"Procedimento: {p.descricao} | Custo: R$ {p.custo:.2f}")

    def mostra_mensagem(self, msg: str):
        print(msg)