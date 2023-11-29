#  Espaço é uma composição da classe Escola
from datetime import date


class Espaco:

    def __init__(self):
        self.__dataCriacao: date = date.today()
        self.__blocos: dict = {}

    def addBloco(self, numero, nome):
        self.__blocos[numero] = nome  # {"nome": nome, "Salas": 10}
        """
        dicionario = {
            1: {"Nome": "Bloco Amarelo", "Salas": 10},
            2: {"Nome": "Bloco Azul", "Salas": 10},
            3: {"Nome": "Bloco Verde", "Salas": 10}
        }"""

    def imprimeBlocos(self):
        for key in sorted(self.__blocos):
            print(f"{key}: {self.__blocos[key]}")

    def removerBloco(self, numero):
        del self.__blocos[numero]

    def modificaBloco(self, numero, novo_nome):
        self.__blocos[numero] = novo_nome
