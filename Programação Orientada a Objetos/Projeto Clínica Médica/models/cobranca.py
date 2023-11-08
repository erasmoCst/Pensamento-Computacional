import datetime
from models.consulta import Consulta

class Cobranca():

    __slots__ = ["data", "valorTotal", "consulta"]

    def __init__(self, data: datetime.date, valorTotal: float, consulta: Consulta):
        self.data: datetime.datetime = data
        self.valorTotal: float = valorTotal
        self.consulta: Consulta = consulta

    def __str__(self):
        return f"Data: {self.data}\n" \
               f"Valor Total: {self.valorTotal}\n" \
               f"Consulta: {self.consulta.codigo}\n"
