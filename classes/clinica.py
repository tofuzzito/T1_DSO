from classes.paciente import Paciente
from classes.profissional_saude import ProfissionalSaude

class Clinica:
    def __init__(
        self,
        nome: str,
        cidade: str,
        descricao: str,
        horarioAbertura: str,
        horarioFechamento: str
    ):
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.horarioAbertura = horarioAbertura
        self.horarioFechamento = horarioFechamento

        # Relacionamentos
        self.pacientes = []
        self.profissionais = []

    def adicionarPaciente(self, paciente: Paciente):
        self.pacientes.append(paciente)

    def adicionarProfissional(self, profissional: ProfissionalSaude):
        self.profissionais.append(profissional)