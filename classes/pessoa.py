from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.nome = nome
        self.celular = celular
        self.cpf = cpf

    def validarCpf(self) -> bool:

        cpf = self.cpf.replace(".", "").replace("-", "")

        if len(cpf) != 11:
            return False

        if not cpf.isdigit():
            return False

        return True

