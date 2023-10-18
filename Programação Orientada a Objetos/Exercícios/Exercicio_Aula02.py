# Considere um software de um jogo MOBA (Multiplayer  Online Battle Arena).
# - Crie uma classe para representar cada um dos seguintes objetos:
# - Jogador
# - Personagem
# - Item
# - Informe os dados de cada um desses objetos (atributos)
# - Informe as operações sobre esses objetos (métodos)
# - Quais objetos adicionais você acha que fariam parte de um jogo?
import random

#Variáveis Globais
USER = None
CONTAS = {}
CLASSES = {"1": "Elfa",
           "2": "Blade knigth",
           "3": "Soul Master",
           "4": "Dark Lord",
           "5": "Magic Gladiator"}
logado = False
personagensConta = {}

#Classes
class Jogador:
    def __init__(self, nome: str, login: str, idade: int):
        self.nome: str = nome
        self.login: str = login
        self.idade: int = idade

    def cadastraJogador(self, nome, login, idade):
        if login not in CONTAS:
            conta = Jogador(nome, login, idade)
            CONTAS[login] = conta
            return True
        return False

    def __str__(self):
        return f'Nome: {self.nome}; \n' \
               f'Login: {self.login}; \n' \
               f'Idade: {self.idade}; \n'

class Personagem:
    def __init__(self, nick: str, classe: str, level: int = 0):
        self.nick = nick
        self.classe = classe
        self.level = level

    def criaPersonagem(self, nick, classe):
        if nick not in personagensConta[USER]:
            personagem = Personagem(nick, CLASSES[classe])
            personagensConta[USER] = personagem
            return True
        return False

    def listaPersonagem(self):
        print(f"-- Lista de personagens de {USER} --\n", personagensConta[USER])

    def __str__(self):
        return f'Nick: {self.nick}; \n' \
               f'Classe: {self.classe}; \n' \
               f'Level: {self.level}; \n'

#Funções
def criarConta():
    nome = input("\nInforme seu nome: ")
    login = input("Crie seu login: ")
    idade = int(input("Informe sua idade: "))

    cadastro = Jogador.cadastraJogador(Jogador,nome, login, idade)
    if cadastro:
        print("\n -- Conta Criada com Sucesso!\nRealize Login para Continuar! --\n")
    else:
        print(f"O Login '{login}' já esta sendo usado.\n Tente novamente!\n")

def criarPersonagem():
    nick = input('Informe o nick do Personagem: ')

    print('-- Classes de Personagem --')
    print("1 - Elfa")
    print("2 - Blade Knigth (BK)")
    print("3 - Soul Master (SM)")
    print("4 - Dark Lord (DL)")
    print("5 - Magic Gladiator (MG)")
    classe = input('Escolha a classe do Personagem: ')

    personagem = Personagem(nick, CLASSES[classe])


def loginConta():
    login = input("\nInforme o login da conta: ")
    if login in CONTAS:
        global USER
        USER = login
        return True
    print("\n -- Usuário não cadastrado! --\n")
    return False

def menuInicial():
    print(" -- MENU --")
    print("1 - Criar Conta")
    print("2 - Realizar Login")
    print("0 - Sair")
    return int(input("Escolha a opção desejada: "))

def opcoesMenu(opcao):
    if opcao == 1:
        criarConta()
    elif opcao == 2:
         return loginConta()
    elif opcao == 0:
        pass
    else:
        print("Digite uma opção válida: ")

def menuJogo():
    print(f" -- Bem Vindo, {CONTAS[USER].login}! --")
    print(" -- MENU --")
    print("1 - Criar Personagem")
    print("2 - Lista Personagem")
    print("0 - Sair")
    return int(input("Escolha a opção desejada: "))

def menuLogado(opcaoLogado):
    if opcaoLogado == 1:
        Personagem.criaPersonagem(Personagem)
    elif opcaoLogado == 2:
        Personagem.listaPersonagem(Personagem)
    elif opcaoLogado == 0:
        pass
    else:
        print("Digite uma opção válida: ")

#Função Principal
while True:
    if not logado:
        opcao = menuInicial()
        if opcao == 0:
            break
        else:
            logado = opcoesMenu(opcao)
    else:
        opcaoLogado = menuJogo()
        if opcaoLogado == 0:
            break
        else:
            menuLogado(opcaoLogado)