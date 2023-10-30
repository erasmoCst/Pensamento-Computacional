import datetime
from pessoa import Pessoa

class Funcionario(Pessoa):
    __slots__ = ["__salarioMensal", "jornadaTrabalho"]

    def __init__(self, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime, salarioMensal: float, jornadaTrabalho: int):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.__salarioMensal: float = salarioMensal
        self.jornadaTrabalho: int = jornadaTrabalho

    def __str__(self):
        return f"Jornada de trabalho: {self.jornadaTrabalho}"