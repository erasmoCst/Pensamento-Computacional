from typing import List
from datetime import datetime
from pessoa import Paciente, Medico
class Consulta:
    codigo: int  = 1
    slots = ["__paciente", "__medico", "__dataHorario", "__prescricao"]

    def __init__(self, paciente: Paciente, medico: Medico, dataHorario: datetime, prescricao: str):
        self.__paciente: Paciente = paciente
        self.__medico: Medico = medico
        self.__dataHorario: datetime = dataHorario
        self.__prescricao: str = prescricao
        Consulta.codigo += 1

class Prescricao: 
    codigo: int = 1
    slots = ["__data", "__exames", "__medicamentos"]

    def __init__(self, data: datetime, exames: List, medicamentos: List):
        self.__data: datetime = data
        self.__exames: [] = exames
        self.__medicamentos: [] = medicamentos
        Prescricao.codigo += 1

class Cobranca:
    slots = ["__data", "__valorTotal", "__consulta"]

    def __init__(self, data: datetime, valorTotal: float, consulta: Consulta):
        self.__data: datetime = data
        self.__valorTotal: float = valorTotal
        self.__consulta: Consulta = consulta
        Cobranca.codigo += 1