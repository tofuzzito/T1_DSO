from DAOs.DAO import DAO
from classes.paciente import Paciente

# ---------------------------------------------------------
# CLASSE CONCRETA PacienteDAO
# ---------------------------------------------------------

class PacienteDAO(DAO):
    def __init__(self):
        # Define o nome do arquivo binário onde os pacientes serão salvos
        super().__init__("pacientes.pkl")

    def add(self, key, obj=None):
        # A chave primária do paciente no dicionário será o CPF
        if isinstance(key, Paciente) and obj is None:
            paciente = key
            key = paciente.cpf
        else:
            paciente = obj

        if key and paciente:
            super().add(key, paciente)

    def get(self, key: str):
        return super().get(key)

    def remove(self, key: str):
        super().remove(key)