import datetime
from models.pessoa import Pessoa

class Paciente(Pessoa):
    __slots__ = ["possuiConvenio", "nomeConvenio"]

    def __init__(self, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime, possuiConvenio: bool, nomeConvenio: str):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.possuiConvenio: bool = possuiConvenio
        self.nomeConvenio: str = nomeConvenio

    def __str__(self):
        return f"Cód.: {self.codigo}\n" \
               f"Nome: {self.nome}\n" \
               f"Gênero: {'Masculino' if self.sexo == 'M' else 'Feminino'}\n" \
               f"Convênio: {self.nomeConvenio}\n"
