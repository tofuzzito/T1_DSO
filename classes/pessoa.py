from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

    def validarCpf(self) -> bool:
        # Validação simples
        return len(self.cpf) == 11 and self.cpf.isdigit()
    