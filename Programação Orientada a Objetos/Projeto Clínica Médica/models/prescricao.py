import datetime


class Prescricao():
    codigo: int = 1

    #__slots__ = ["data", "__exames", "__medicamentos"]

    def __init__(self, data: datetime.date, exames: list, medicamentos: list):
        self.codigo: int = Prescricao.codigo
        self.data: datetime.date = data
        self.exames: list = exames
        self.medicamentos: list = medicamentos
        Prescricao.codigo += 1

    def __str__(self):
        return f"\n\tCód.: {self.codigo}\n" \
               f"\tExames: {self.exames}\n" \
               f"\tMedicamentos: {self.medicamentos}\n" \
               f"\tData da Prescrição: {self.data}\n"
