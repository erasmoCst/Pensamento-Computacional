import datetime
from models.funcionario import Funcionario


class Medico(Funcionario):
    __slots__ = ["crm", "__valorConsulta", "especialidades"]

    def __init__(self, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime.date, salarioMensal: float, jornadaTrabalho: int, crm: str, valorConsulta: float, especialidades: list):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, jornadaTrabalho)
        self.crm: str = crm
        self.__valorConsulta: float = valorConsulta
        self.especialidades: list = especialidades

    def __str__(self):
        return f"Cód.: {self.codigo}\n" \
               f"{'Dr.' if self.sexo == 'M' else 'Dr(a).'} {self.nome}\n" \
               f"CRM: {self.crm}\n" \
               f"Especialidades: {self.especialidades}\n"
