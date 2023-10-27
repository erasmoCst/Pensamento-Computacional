import datetime

class Pessoa(object):
    codigo: int = 1
    __slots__ = ["nome", "__cpf", "__rg", "sexo", "__email", "__telefone", "dataNascimento"]

    def __init__(self, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, dataNascimento: datetime):
        self.__codigo: int = Pessoa.codigo
        self.nome: str = nome
        self.__cpf: str = cpf
        self.__rg: str = rg
        self.sexo: str = sexo
        self.__email: str = email
        self.__telefone: str = telefone
        self.dataNascimento: str = dataNascimento
        Pessoa.__codigo += 1

    def __str__(self):
        return f"Pessoa: \n" \
              f"Nome: {self.nome}" \
              f"Gênero: {'Masculino' if self.sexo == 'M' else 'Feminino'}"
