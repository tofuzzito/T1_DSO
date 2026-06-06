class SistemaView:
    def mostra_menu_principal(self) -> str:
        print("\n=========================================")
        print("    SISTEMA DE GESTÃO MÉDICA - MVC       ")
        print("=========================================")
        print("1 - Gerenciar Clínicas")
        print("2 - Gerenciar Pacientes")
        print("3 - Gerenciar Profissionais de Saúde")
        print("4 - Gerenciar Procedimentos")
        print("5 - Gerenciar Tipos de Atendimento")
        print("6 - Gerenciar Atendimentos & Pagamentos")
        print("7 - Central de Relatórios")
        print("0 - Sair do Sistema")
        print("=========================================")
        return input("Escolha o módulo desejado: ")

    def mostra_opcao_invalida(self):
        print("Opção inválida!")

    def mostra_mensagem_encerramento(self):
        print("\nFinalizando o sistema... Até logo!")