from datetime import date
from classes.pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(
        self,
        nome: str,
        celular: str,
        cpf: str,
        dataNascimento: date
    ):
        super().__init__(nome, celular, cpf)
        self.dataNascimento = dataNascimento

    def maiorDeIdade(self) -> bool:
        hoje = date.today()

        idade = (
            hoje.year
            - self.dataNascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.dataNascimento.month, self.dataNascimento.day)
            )
        )

        return idade >= 18