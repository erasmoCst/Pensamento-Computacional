from models.curso import Curso
from models.professor import Professor
from models.espaco import Espaco

class Escola:
    """Classe escola é responsável por criar Cursos
    """
    __slots__ = ["__nome", "__cnpj", "__cursos", "__espaco"]

    def __init__(self, nome: str, cnpj: str):
        self.__nome: str = nome
        self.__cnpj: str = cnpj
        self.__cursos: list[Curso] = []
        self.__espaco: Espaco = Espaco()

    def criaCurso(self, nome: str, data: str, professor: Professor,
                  horas: int = 20, valor: float = 1000.00):
        """
            Método responsável por criar Cursos e salvar na lista de cursos da Escola
        """
        curso = Curso(nome, data, professor, horas, valor)
        self.__cursos.append(curso)

    def getCurso(self, posicao: int):
        if posicao < len(self.__cursos):
            return self.__cursos[posicao-1]
        else:
            print(f"Não existe curso na posição {posicao}!!")

    def listaCursos(self):
        for i, curso in enumerate(self.__cursos):
            print(f"Posição: {i+1}{curso}")

    def insereEspaco(self, numero, nome):
        self.__espaco.addBloco(numero, nome)

    def mostraEspacos(self):
        self.__espaco.imprimeBlocos()

    def __str__(self):
        return f"Nome: {self.__nome}; CNPJ: {self.__cnpj}"
