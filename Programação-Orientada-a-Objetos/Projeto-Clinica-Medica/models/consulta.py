import datetime
from models.prescricao import Prescricao

class Consulta():

    #__slots__ = ["__paciente", "__medico", "__data", "__prescricao"]

    def __init__(self, paciente: str, medico: str, data: datetime.datetime, prescricao: Prescricao):
        self.paciente: str = paciente
        self.medico: str = medico
        self.data: datetime.datetime = data
        self.prescricao: Prescricao = prescricao

    def __str__(self):
        return f"Paciente: {self.paciente}\n" \
               f"Medico: {self.medico}\n" \
               f"Data: {self.data}\n" \
               f"Prescrição: {self.prescricao}\n"

