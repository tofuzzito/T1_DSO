import sys
from controladores.ClinicaController import ClinicaController
from controladores.PacienteController import PacienteController
from controladores.ProfissionalController import ProfissionalController
from controladores.ProcedimentoController import ProcedimentoController
from controladores.TipoAtendimentoController import TipoAtendimentoController
from controladores.AtendimentoController import AtendimentoController
from controladores.RelatorioController import RelatorioController
from views.TelaSistema import SistemaView  # Importando a nova View

class ControladorSistema:
    def __init__(self):
        self.__view = SistemaView()  # Instanciando a View do Sistema
        
        # Instanciando Controladores do Integrante 1
        self.__controlador_clinicas = ClinicaController()
        self.__controlador_pacientes = PacienteController()
        self.__controlador_profissionais = ProfissionalController()
        self.__controlador_procedimentos = ProcedimentoController(self.__controlador_profissionais)
        
        # Instanciando Controladores do Integrante 2
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
            # Delega para a View a responsabilidade de interagir com o terminal
            opcao = self.__view.mostra_menu_principal()
            
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                if opcao != "0":
                    self.__view.mostra_opcao_invalida()

    def encerrar_sistema(self):
        self.__view.mostra_mensagem_encerramento()
        sys.exit(0)