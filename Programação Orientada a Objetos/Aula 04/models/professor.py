#  Agregação da classe Curso

class Professor:
    __id = 1
    __slots__ = ["__codigo", "__nome", "__cpf", "__dataNasc", "__email", "__telefone", "__formacao"]

    def __init__(self, nome, cpf, data_nasc, email, telefone, formacao):
        self.__codigo: int = Professor.__id
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__dataNasc: str = data_nasc
        self.__email: str = email
        self.__telefone: str = telefone
        self.__formacao: str = formacao
        Professor.__id += 1

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

