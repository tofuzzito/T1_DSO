from classes.profissional_saude import ProfissionalSaude

class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: 'ProfissionalSaude'):
        self.descricao = descricao
        self.custo = float(custo)
        self.profissional = profissional  # Associação 1 para * com ProfissionalSaude