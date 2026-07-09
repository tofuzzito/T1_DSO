from DAOs.DAO import DAO
from typing import Any

class ProfissionalDAO(DAO):
    def __init__(self):
        super().__init__("profissionais.pkl")

    def add(self, key: str, obj: Any):
        """Usa o registroConselho contido no objeto como chave."""
        if obj and getattr(obj, "registroProfissional", None):
            super().add(obj.registroProfissional, obj)

    def get(self, key: str) -> Any:
        return super().get(key)  # type: ignore

    def remove(self, key: str):
        super().remove(key)