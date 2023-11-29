import datetime
from models.funcionario import Funcionario

class Pagamento():

    __slots__ = ["data", "valorTotal", "consulta"]

    def __init__(self, data: datetime.date, valorTotal: float, funcionario: Funcionario):
        self.data: datetime.datetime = data
        self.valorTotal: float = valorTotal
        self.funcionario: Funcionario = funcionario

    def __str__(self):
        return f"Data: {self.data}\n" \
               f"Valor Total: {self.valorTotal}\n" \
               f"Funcionario: {self.funcionario.nome}\n"
