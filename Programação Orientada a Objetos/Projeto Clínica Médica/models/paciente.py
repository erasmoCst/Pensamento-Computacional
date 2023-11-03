import datetime
from models.pessoa import Pessoa

class Paciente(Pessoa):
    __slots__ = ["possuiConvenio", "nomeConvenio"]

    def __init__(self, int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime, possuiConvenio: bool, nomeConvenio: str):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.possuiConvenio: bool = possuiConvenio
        self.nomeConvenio: str = nomeConvenio


    def __str__(self):
        if self.possuiConvenio:
            return f"Convênio: {self.nomeConvenio}"
        return "O paciente não possui convênio."
