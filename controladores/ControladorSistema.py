import sys
from controladores.ClinicaController import ClinicaController
from controladores.PacienteController import PacienteController
from controladores.ProfissionalController import ProfissionalController
from controladores.ProcedimentoController import ProcedimentoController
from controladores.TipoAtendimentoController import TipoAtendimentoController
from controladores.AtendimentoController import AtendimentoController
from controladores.RelatorioController import RelatorioController
from views.TelaSistema import SistemaView


class ControladorSistema:
    def __init__(self):
        self.__view = SistemaView()

        # Instanciando Controladores do Integrante 1 (Passando self onde necessário)
        self.__controlador_clinicas = ClinicaController()
        self.__controlador_pacientes = PacienteController(self)
        self.__controlador_profissionais = ProfissionalController()
        self.__controlador_procedimentos = ProcedimentoController(
            self.__controlador_profissionais)

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
        # Mapeia os textos que os botões da sua nova SistemaView gráfica vão retornar
        opcoes = {
            "Clínicas": self.__controlador_clinicas.abre_tela,
            "Pacientes": self.__controlador_pacientes.abre_tela,
            "Profissionais": self.__controlador_profissionais.abre_tela,
            "Procedimentos": self.__controlador_procedimentos.abre_tela,
            "Tipos de Atendimento": self.__controlador_tipos.abre_tela,
            "Atendimentos": self.__controlador_atendimentos.abre_tela,
            "Relatórios": self.__controlador_relatorios.abre_tela,
            "Sair": self.encerrar_sistema
        }

        while True:
            opcao = self.__view.mostra_menu_principal()

            # Se o usuário fechar a janela no 'X', trata como encerrar o sistema
            if opcao is None:
                opcao = "Sair"

            funcao = opcoes.get(opcao)
            if funcao:
                funcao()

    def encerrar_sistema(self):
        self.__view.mostra_mensagem_encerramento()
        sys.exit(0)