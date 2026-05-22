from classes.pessoa import Pessoa

class ProfissionalSaude(Pessoa):
    def __init__(
        self,
        nome: str,
        celular: str,
        cpf: str,
        especialidade: str,
        registroProfissional: str
    ):
        super().__init__(nome, celular, cpf)
        self.especialidade = especialidade
        self.registroProfissional = registroProfissional