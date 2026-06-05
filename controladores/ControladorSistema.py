import sys
from .ClinicaController import ClinicaController
from .PacienteController import PacienteController
from .ProfissionalController import ProfissionalController
from .ProcedimentoController import ProcedimentoController
from .TipoAtendimentoController import TipoAtendimentoController
from .AtendimentoController import AtendimentoController
from .RelatorioController import RelatorioController

class ControladorSistema:
    def __init__(self):
        # Instanciando Controladores do Integrante 1
        self.__controlador_clinicas = ClinicaController()
        self.__controlador_pacientes = PacienteController()
        self.__controlador_profissionais = ProfissionalController()
        self.__controlador_procedimentos = ProcedimentoController(self.__controlador_profissionais)
        
        # Instanciando Controladores do Integrante 2 (Injetando dependências)
        self.__controlador_tipos = TipoAtendimentoController()
        self.__controlador_atendimentos = AtendimentoController(
            self.__controlador_pacientes,
            self.__controlador_clinicas,
            self.__controlador_procedimentos,
            self.__controlador_tipos
        )
        self.__controlador_relatorios = RelatorioController(
            self.__controlador_atendimentos,
            self.__controlador_procedimentos
        )

    def inicializa_sistema(self):
        self.mostra_menu_principal()

    def mostra_menu_principal(self):
        opcoes = {
            "1": self.__controlador_clinicas.abre_tela,
            "2": self.__controlador_pacientes.abre_tela,
            "3": self.__controlador_profissionais.abre_tela,
            "4": self.__controlador_procedimentos.abre_tela,
            "5": self.__controlador_tipos.abre_tela,
            "6": self.__controlador_atendimentos.abre_tela,
            "7": self.__controlador_relatorios.abre_tela,
            "0": self.encerrar_sistema
        }

        while True:
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
            
            opcao = input("Escolha o módulo desejado: ")
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                if opcao != "0":
                    print("Opção inválida!")

    def encerrar_sistema(self):
        print("\nFinalizando o sistema... Até logo!")
        sys.exit(0)

if __name__ == "__main__":
    # Ponto de entrada que executa o software completo
    ControladorSistema().inicializa_sistema()