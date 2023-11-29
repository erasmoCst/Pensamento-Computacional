from models.escola import Escola
from models.professor import Professor

print(__name__)

if __name__ == '__main__':
    escola = Escola(nome="PUCPR", cnpj="8293801238021")
    print(escola)

    escola.insereEspaco("cinco", "Bloco Vermelho")
    escola.insereEspaco("dois", "Bloco Azul")
    escola.insereEspaco("um", "Bloco Amarelo")
    escola.insereEspaco("três", "Bloco Verde")
    escola.insereEspaco("quatro", "Bloco Laranja")

    escola.mostraEspacos()

    antonio = Professor(nome="Antonio David Viniski",
                        cpf="0101010101011",
                        data_nasc="04/11/1993",
                        email="antonio.david@pucpr.br",
                        telefone="41990909090",
                        formacao="Doutor em Informática")

    escola.criaCurso("POO", "07/10/2023", antonio)
    escola.criaCurso("BD", "31/01/2024", antonio, 24, 1500)
    escola.listaCursos()

    antonio.setNome("Antonio David Travensoli Viniski")
    escola.listaCursos()

    escola.criaCurso("Projeto Hands On", "01/03/2024", antonio, 12)
    escola.listaCursos()

    poo = escola.getCurso(1)
    poo.insereConteudo("Funções e Dicionários")
    poo.insereConteudo("Classes, atributos e métodos")
    poo.insereConteudo("Encapsulamento e Módulos")
    poo.insereConteudo("Associação entre Objetos")
    poo.listaConteudos()

