import datetime
from models.pessoa import Pessoa

class Funcionario(Pessoa):
    __slots__ = ["__salarioMensal", "jornadaTrabalho"]

    def __init__(self, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime.date, salarioMensal: float, jornadaTrabalho: str):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.__salarioMensal: float = salarioMensal
        self.jornadaTrabalho: str = jornadaTrabalho

    def __str__(self):
        return f"Cód.: {self.codigo}\n" \
               f"Nome: {self.nome}\n" \
               f"Gênero: {'Masculino' if self.sexo == 'M' else 'Feminino'}\n" \
               f"Jornada de Trabalho: {self.jornadaTrabalho}\n"
