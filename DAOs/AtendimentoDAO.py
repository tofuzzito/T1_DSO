from DAOs.DAO import DAO
from typing import Any

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, key: str, obj: Any):
        """
        Gera uma chave única combinando dados do atendimento 
        caso nenhuma chave direta seja enviada.
        """
        if obj:
            data = getattr(obj, "data", "")
            horario = getattr(obj, "horarioInicio", "")
            paciente = getattr(obj, "paciente", None)
            cpf = paciente.cpf if paciente else ""
            chave_unica = f"{data}_{horario}_{cpf}"
            super().add(chave_unica, obj)

    def get(self, key: str) -> Any:
        return super().get(key)  # type: ignore

    def remove(self, key: str):
        super().remove(key)