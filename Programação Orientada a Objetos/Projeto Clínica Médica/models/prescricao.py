import datetime


class Prescricao():
    codigo: int = 1

    __slots__ = ["data", "__exames", "__medicamentos"]

    def __init__(self, data: datetime.date, exames: list, medicamentos: list):
        self.codigo: int = Prescricao.codigo
        self.data: datetime.date = data
        self.__exames: list = exames
        self.__medicamentos: list = medicamentos
        Prescricao.codigo += 1

    def __str__(self):
        return f"Cód.: {self.codigo}\n" \
               f"Exames: {self.exames}\n" \
               f"Medicamentos: {self.medicamentos}\n" \
               f"Data da Prescrição: {self.data}\n"
