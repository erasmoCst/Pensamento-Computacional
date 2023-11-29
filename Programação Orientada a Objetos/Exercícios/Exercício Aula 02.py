# Considere um software de um jogo MOBA (Multiplayer  Online Battle Arena).
# - Crie uma classe para representar cada um dos seguintes objetos:
# - Jogador
# - Personagem
# - Item
# - Informe os dados de cada um desses objetos (atributos)
# - Informe as operações sobre esses objetos (métodos)
# - Quais objetos adicionais você acha que fariam parte de um jogo?
import random

status = False
contas = {}
personagemConta = {}


class Jogador:
    def __init__(self, nome: str, login: str, idade: int):
        self.nome: str = nome
        self.login: str = login
        self.idade: int = idade

    def __str__(self):
        return f'Nome: {self.nome}; \n' \
               f'Login: {self.login}; \n' \
               f'Idade: {self.idade}; \n'


    def criaConta():
        nome = input('Informe seu nome: ')
        login = input('Crie seu login: ')
        idade = int(input('Informe sua idade:'))

        conta = Jogador(nome, login, idade)
        contas[login] = conta


def verificarConta():
    exist = False
    login = None
    while not exist:
        login = input("Informe o login da Conta: ")
        if login in contas:
            exist = True
            return True
    return False


class Personagem:
    nrPersonagem = 0

    def __init__(self, nick: str, idPersonagem: int, classe: str,nomeClasse: str, Level: int):
        self.nick = nick
        self.idPersonagem = idPersonagem
        self.classe = classe
        self.nomeClasse = nomeClasse
        self.Level = Level


    def criaPersonagem():
        nick = input('Informe o nick do Personagem: ')
        idPerson = random.randrange(1000)
        print('****Classes de Personagem***')
        print("1 - Elfa ")
        print("2 - Blade knigth (BK) ")
        print("3 - Soul Master (SM)")
        print("4 - Dark Lord (DL)")
        print('5 - Magic Gladiator (MG)')
        classe = input('Escolha a classe do Personagem: ')
        nomeClasse = ['Elfa','Blade knigth', 'Soul Master', 'Dark Lord','Magic Gladiator' ]
        Level = 0

        personagem = Personagem(nick, idPerson, classe,nomeClasse, Level)
        personagemConta[idPerson] = personagem


def listaContas():
    for n in contas:
        print(contas[n])

def listaPersonagem():
    for n in personagemConta:
        print(personagemConta[n])

def menu():
    print("MENU")
    print("1 - Criar Conta")
    print("2 - Lista Contas")
    print("3 - Realizar Login")
    print("0 - Sair")
    opcao = int(input("Digite a sua opção: "))
    return opcao

def opcoesMenu(opcao):
    if opcao == 1:
        Jogador.criaConta()
    elif opcao == 2:
        listaContas()
    elif opcao == 3:
         return verificarConta()
    elif opcao == 0:
        pass
    else:
        print("Digite uma opção válida")

def menu():
    print("MENU")
    print("1 - Criar Conta")
    print("2 - Lista Contas")
    print("3 - Realizar Login")
    print("0 - Sair")
    opcao = int(input("Digite a sua opção: "))
    return opcao


def menuJogo():
    print("MENU")
    print("1 - Criar Personagem")
    print("2 - Lista Personagem")
    print("0 - Sair")
    opcaoLogado = int(input("Digite a sua opção: "))
    return opcaoLogado


def menuLogado(opcaoLogado):
    if opcaoLogado == 1:
        Personagem.criaPersonagem()
    elif opcaoLogado == 2:
        listaPersonagem()
    elif opcaoLogado == 0:
        pass
    else:
        print("Digite uma opção válida")



while True:
    if not status:
        opcao = menu()
        if opcao == 0:
            break
        else:
            status = opcoesMenu(opcao)
    else:
        opcaoLogado = menuJogo()
        if opcaoLogado == 0:
            break
        else:
            menuLogado(opcaoLogado)