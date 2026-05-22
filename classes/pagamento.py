from abc import ABC, abstractmethod
from datetime import date

class Pagamento(ABC):
    def __init__(self, data: date, valorPago: float):
        self.data = data
        self.valorPago = valorPago

    @abstractmethod
    def calcularRestante(self) -> float:
        pass

class PagamentoDinheiro(Pagamento):
    pass

class PagamentoCartao(Pagamento):
    pass

class PagamentoPix(Pagamento):
    pass