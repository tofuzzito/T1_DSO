from typing import List
from classes.pagamento import Pagamento
from classes.procedimento import Procedimento
from classes.paciente import Paciente
from classes.clinica import Clinica
from datetime import date

class Atendimento:
    def __init__(self, data: date, horarioInicio: str, horarioFim: str, valor: float, 
                 paciente: 'Paciente', clinica: 'Clinica', tipoAtendimento: 'TipoAtendimento'):
        self.data = data
        self.horarioInicio = horarioInicio
        self.horarioFim = horarioFim
        self.valor = float(valor)
        
        # Associações diretas (Multiplicidade 1)
        self.paciente = paciente
        self.clinica = clinica
        self.tipoAtendimento = tipoAtendimento
        
        # Composições (Multiplicidade *) inicializadas como listas vazias
        self.procedimentos: List['Procedimento'] = []
        self.pagamentos: List['Pagamento'] = []

    def adicionar_procedimento(self, procedimento: 'Procedimento'):
        """Adiciona um procedimento à composição do atendimento."""
        self.procedimentos.append(procedimento)

    def adicionar_pagamento(self, pagamento: 'Pagamento'):
        """Adiciona um pagamento à composição do atendimento."""
        self.pagamentos.append(pagamento)

class TipoAtendimento:
    def __init__(self, descricao: str):
        self.descricao = str(descricao)