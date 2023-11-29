from models.professor import Professor
from models.ementa import Ementa


class Curso:  # Definindo a estrutura de um objeto, criando um novo tipo de dados
    codigo: int = 1  # atributo estático (atributo da classe)/ e também um atributo público do objeto

    __slots__ = ["__id", "__nome", "data", "__professor", "horas", "__valor", "__ementa"]

    def __init__(self, nome: str, data: str, professor: Professor, horas: int = 20, valor: float = 1000.00):
        self.__id = Curso.codigo
        self.__nome: str = nome
        self.data: str = data
        self.__professor: Professor = professor
        self.horas: int = horas
        self.__valor: float = valor
        self.__ementa = Ementa()
        Curso.codigo += 1

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getProfessor(self):
        return self.__professor

    def setProfessor(self, novo):
        self.__professor = novo

    def adia(self, novadata: str):
        self.data = novadata

    def encarece(self, aumento: float):
        self.__valor = self.__valor + aumento

    def trocaProfessor(self, novo_professor):
        self.setProfessor(novo_professor)

    def insereConteudo(self, conteudo: str):
        self.__ementa.addConteudo(conteudo)

    def removeConteudo(self, conteudo):
        self.__ementa.removeConteudo(conteudo)

    def listaConteudos(self):
        print(self)
        self.__ementa.imprimirEmenta()

    def __str__(self):
        return f"\nCódigo: {self.__id}; "\
               f"Nome: {self.__nome}; "\
               f"Data: {self.data}; "\
               f"Professor: {self.__professor.getNome()}; "\
               f"Horas: {self.horas}; "\
               f"Valor: {self.__valor}; "
