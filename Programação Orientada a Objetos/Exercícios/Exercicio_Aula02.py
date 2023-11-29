# Considere um software de um jogo MOBA (Multiplayer  Online Battle Arena).
# - Crie uma classe para representar cada um dos seguintes objetos:
# - Jogador
# - Personagem
# - Item
# - Informe os dados de cada um desses objetos (atributos)
# - Informe as operações sobre esses objetos (métodos)
# - Quais objetos adicionais você acha que fariam parte de um jogo?

#Variáveis Globais
STATUS = True
LOGADO = False
USUARIO = None
CONTAS = {}
PERSONAGENS = {}
PERSONAGEM = None
CLASSES = {"1": "Elfa",
           "2": "Blade knigth",
           "3": "Soul Master",
           "4": "Dark Lord",
           "5": "Magic Gladiator"}
ITENS = {}

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
            PERSONAGENS[login] = {}
            return True
        return False

    def __str__(self):
        return f" - Nome: {self.nome} \n" \
               f" - Login: {self.login} \n" \
               f" - Idade: {self.idade} \n"

class Personagem:
    def __init__(self, nick: str, classe: str, level: int = 0):
        self.nick = nick
        self.classe = classe
        self.level = level

    def criaPersonagem(self, nick, classe):
        if nick not in PERSONAGENS[USUARIO]:
            personagem = Personagem(nick, CLASSES[classe])
            PERSONAGENS[USUARIO] = personagem
            return True
        return False

    def listaPersonagem(self):
        print(f" -- Lista de personagens de '{USUARIO}' --\n", PERSONAGENS[USUARIO])

    def __str__(self):
        return f"- Nick: {self.nick}\n"\
               f" - Classe: {self.classe}\n"\
               f" - Level: {self.level}\n"

#Funções
def criarConta():
    print(" -- Criação de Conta --")

    idade = int(input("Informe sua idade: "))
    if idade < 15:
        print("\n -- Idade insuficiente! --\nÉ necessário ter ao menos 15 anos para jogar!\n")
    else:
        nome = input("Informe seu nome: ")
        login = input("Crie seu login: ")

        cadastro = Jogador.cadastraJogador(Jogador,nome, login, idade)

        while not cadastro:
            print(f"O Login '{login}' já esta sendo usado.\n Tente novamente outro nome de usuário!\n")
            cadastro = Jogador.cadastraJogador(Jogador,nome, login, idade)

        print("\n -- Conta Criada com Sucesso!\nRealize Login para Continuar! --\n")


def criarPersonagem():
    classe = validaClasse()

    while classe not in CLASSES:
        classe = validaClasse()

    nick = input("Informe o nick do personagem: ")

    personagem = Personagem.criaPersonagem(Personagem, nick, classe)

    while not personagem:
        print(f"O Nick '{nick}' já esta sendo usado.\n Informe outro nick para seu personagem!\n")
        personagem = Personagem.criaPersonagem(Personagem, nick, classe)

    print(f"\n -- Personagem {nick} da classe {classe} criado com Sucesso! --\n")

def validaClasse():
    print('\n -- Classes de Personagem --')
    print("1 - Elfa")
    print("2 - Blade Knigth (BK)")
    print("3 - Soul Master (SM)")
    print("4 - Dark Lord (DL)")
    print("5 - Magic Gladiator (MG)")
    classe = input("Informe a classe do personagem: ")

    if classe not in CLASSES:
        print("Classe inválida! Selecione uma classe válida!")
        return "-1"
    return classe

def loginConta():
    login = input("\nInforme o login da conta: ")
    if login in CONTAS:
        global USUARIO
        USUARIO = login
        return True
    print("\n -- Usuário não cadastrado! --\n")
    return False

def menuInicial():
    print("\n -- MENU --")
    print("1 - Criar Conta")
    print("2 - Realizar Login")
    print("0 - Sair")
    return input("Informe a opção desejada: ")

def opcoesMenuInicial(opcao):
    if opcao == "0":
        global STATUS
        STATUS = False
    elif opcao == "1":
        criarConta()
    elif opcao == "2":
         return loginConta()
    else:
        print("\n -- Opção Inválida! --\n Digite uma opção válida.\n")


def menuLogado():
    print(f"\n -- Bem Vindo, {CONTAS[USUARIO].login}! --\n")
    print(" -- MENU --")
    print("1 - Criar Personagem")
    print("2 - Listar Personagem")
    print("3 - Selecionar Personagem")
    print("4 - Deletar Personagem")
    print("5 - Deslogar")
    print("0 - Sair")
    return input("Informe a opção desejada: ")

def opcoesMenuLogado(opcaoLogado):
    if opcaoLogado == "0":
        global STATUS
        STATUS = False
    elif opcaoLogado == "1":
        criarPersonagem()
    elif opcaoLogado == "2":
        Personagem.listaPersonagem(Personagem)
    elif opcaoLogado == "3":
        pass
    elif opcaoLogado == "4":
        pass
    elif opcaoLogado == "5":
        global USUARIO, LOGADO
        USUARIO = None
        LOGADO = False
    else:
        print("\n -- Opção Inválida! --\n Digite uma opção válida.\n")

#Função Principal
while STATUS:
    if not LOGADO:
        opcao = menuInicial()
        LOGADO = opcoesMenuInicial(opcao)
    else:
        opcaoLogado = menuLogado()
        opcoesMenuLogado(opcaoLogado)