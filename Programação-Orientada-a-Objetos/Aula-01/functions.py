
# parametros posicionais
def imprimeCurso(nome, cargaHoraria):
    print(f"O nome do curso é {nome}, com carga horária de {cargaHoraria} horas")


# parâmetros nomeados
def imprimePadrao(nome="Programação Orientada a Objetos", cargaHoraria=20):
    print(f"O nome do curso é {nome}, com carga horária de {cargaHoraria} horas")


imprimeCurso("Pensamento Computacional", 24)
imprimeCurso("Programação Orientada a Objetos", 20)

imprimePadrao()
imprimePadrao(cargaHoraria=24, nome="Estrutura de Dados")


def imprimeInfoCurso(inicio, nome="Programação Orientada a Objetos", cargaHoraria=20):
    print(f"O nome do curso é {nome}, com carga horária de {cargaHoraria} horas, inicio em {inicio}")


imprimeInfoCurso("07/10/2023", nome="Desenvolvimento Ágil")
imprimeInfoCurso("07/10/2023", cargaHoraria=30)

imprimeInfoCurso("07/10/2023", nome="Teste Curso")

def imprimeParametros(*args):
    print(args)

imprimeParametros(10,20,30,50,60,70)



def funcao():
    print("Bloco de código")

funcao()

def imprimir(nome):
    print(f"Nome: {nome}")

imprimir("João da Silva")
imprimir("José de Jesus")
imprimir("Maria das Dores")

def horarios(disciplina='Programação em Python', horario='13:00 as 17:00'):
    print(f"A horário da disciplina {disciplina} é {horario}")

horarios()
horarios("Desenvolvimento Ágil", "08:00 as 12:00")


def matricula(curso='', disciplina='', periodo=0):
    print(f'Realizando a matrícula: \n'
            f'\t-Curso: {curso}\n'
            f'\t-Disciplina: {disciplina}\n'
            f'\t-Período: {periodo}')
matricula("Ciência da Computação", "RA", 2)


def matricula(curso='', disciplina='', periodo=0):
    print(f'Realizando a matrícula: \n'
            f'\t-Curso: {curso}\n'
            f'\t-Disciplina: {disciplina}\n'
            f'\t-Período: {periodo}')

matricula("Ciência da Computação", "RA", 2)
matricula(periodo=2, curso="Ciência da Computação", disciplina="RA")

def maior_30(*args):
    print(args)
    for num in args:
        if num > 30:
            print(num)

maior_30(10, 20, 30, 40, 50, 60)

def dadosPessoais(**kwargs):
    print(type(kwargs))
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dadosPessoais(nome='João', idade=35, carreira='Professor Auxiliar')

def operacao(val1, val2, operador):
    match(operador):
        case "+": return val1 + val2
        case "-": return val1 - val2
        case "*": return val1 * val2
        case "/": return val1 / val2
        case "_": return "Operador inválido"

valor = operacao(1,45,"/")
print(valor)

def soma_media(valor1, valor2):
    soma = valor1 + valor2
    media = (valor1 + valor2)/2
    return soma, media

valores = soma_media(12, 42)
print(valores)
valor_soma, valor_media = soma_media(12, 42)
print(valor_soma, valor_media)


def myFunction():
    """    Do nothing, but document it.
    No, really, it doesn't do anything."""
    pass

print(myFunction.__doc__)


def f(nome: str, cep: str = '00000000') -> str:
    print("Annotations:", f.__annotations__)
    print("Argumentos:", nome, cep)
    return nome + ' e ' + cep
f('Antonio')
print(valores)




