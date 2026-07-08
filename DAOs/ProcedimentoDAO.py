from DAOs.DAO import DAO
from typing import Any

class ProcedimentoDAO(DAO):
    def __init__(self):
        super().__init__("procedimentos.pkl")

    def add(self, key: str, obj: Any):
        """Usa o código do procedimento como chave."""
        if obj and getattr(obj, "codigo", None):
            super().add(obj.codigo, obj)

    def get(self, key: str) -> Any:
        return super().get(key)  # type: ignore

    def remove(self, key: str):
        super().remove(key)