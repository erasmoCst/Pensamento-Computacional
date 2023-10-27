import datetime

from pessoa import Pessoa

class Paciente(Pessoa):
    __slots__ = ["possuiConvenio", "nomeConvenio"]

    def __init__(self, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime, possuiConvenio: bool, nomeConvenio: str):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.possuiConvenio: bool = possuiConvenio

        if possuiConvenio:
            self.nomeConvenio: str = nomeConvenio
        else:
            self.nomeConvenio: str = "-"

    def __str__(self):
        if self.possuiConvenio:
            return f"Convênio: {self.nomeConvenio}"
        return "O paciente não possui convênio."
