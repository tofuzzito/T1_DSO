# ---------------------------------------------------------
# ClinicaDAO
# ---------------------------------------------------------
from DAOs.DAO import DAO
from classes.clinica import Clinica


class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__("clinicas.pkl")

    # Mantém EXATAMENTE a mesma assinatura da classe mãe: (self, key, obj)
    def add(self, key: str, obj: Clinica):
        """Sobrescreve o add garantindo que salve usando o nome como chave."""
        if obj and getattr(obj, "nome", None):
            super().add(obj.nome, obj)

    def get(self, key: str) -> Clinica | None:
        """Busca uma clínica, podendo retornar o objeto Clinica ou None."""
        resultado = super().get(key)
        
        # Faz um 'Type Guard': se for None, retorna None
        if resultado is None:
            return None
        # Se não for None, garante que é do tipo Clinica antes de retornar
        return resultado

    def remove(self, key: str):
        super().remove(key)