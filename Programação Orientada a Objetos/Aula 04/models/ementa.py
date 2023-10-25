#  Ementa é uma composição da classe Curso
from datetime import datetime, date


class Ementa:
    def __init__(self):
        self.__dataCriacao: date = date.today()
        self.__dataAlteracao: datetime = datetime.now()
        self.__conteudos: list[str] = []

    def setDataAlteracao(self, data_alteracao):
        self.__dataAlteracao = data_alteracao

    def addConteudo(self, conteudo: str):
        if conteudo not in self.__conteudos:
            self.__conteudos.append(conteudo)
        else:
            print(f"Conteúdo \"{conteudo}\" já existe na ementa!")

    def removeConteudo(self, conteudo: str):
        if conteudo in self.__conteudos:
            self.__conteudos.remove(conteudo)
        else:
            print(f"Conteúdo \"{conteudo}\" não existe na ementa!")


    def imprimirEmenta(self):
        for i, conteudo in enumerate(self.__conteudos):
            print(f"{i+1}: {conteudo}")
