import datetime
from models.paciente import Paciente
from models.medico import Medico
from models.prescricao import Prescricao

class Consulta():

    __slots__ = ["__paciente", "__medico", "__data", "__prescricao"]

    def __init__(self, paciente: Paciente, medico: Medico, data: datetime.datetime, prescricao: Prescricao):
        self.__paciente: Paciente = paciente
        self.__medico: Medico = medico
        self.__data: datetime.datetime = data
        self.__prescricao: Prescricao = prescricao


    def __str__(self):
        return f"Paciente: {self.nome}\n" \
               f"{'Dr.' if self.sexo == 'M' else 'Dr(a).'} {self.nome}\n" \
               f"Data: {self.data}\n"
