from abc import ABC, abstractmethod
from datetime import date

class Pagamento(ABC):
    def __init__(self, data: date, valorPago: float):
        self.data = data
        self.valorPago = float(valorPago)

    @abstractmethod
    def calcularRestante(self, valor_total: float) -> float:
        """Método abstrato que deve ser implementado por todas as subclasses."""
        pass


class PagamentoPix(Pagamento):
    def __init__(self, data: date, valorPago: float, cpfPagador: str):
        # O super().__init__ chama o construtor da classe mãe (Pagamento)
        super().__init__(data, valorPago)
        self.cpfPagador = str(cpfPagador)

    def calcularRestante(self, valor_total: float) -> float:
        """Calcula o quanto falta pagar subtraindo o valor pago do valor total."""
        restante = valor_total - self.valorPago
        return max(0.0, restante)  # Garante que não retorne valores negativos


# --- Mantendo o esqueleto das outras classes ---

class PagamentoDinheiro(Pagamento):
    def calcularRestante(self, valor_total: float) -> float:
        restante = valor_total - self.valorPago
        return max(0.0, restante)


class PagamentoCartao(Pagamento):
    def __init__(self, data: date, valorPago: float, numeroCartao: str, bandeira: str):
        super().__init__(data, valorPago)
        self.numeroCartao = str(numeroCartao)
        self.bandeira = str(bandeira)

    def calcularRestante(self, valor_total: float) -> float:
        restante = valor_total - self.valorPago
        return max(0.0, restante)