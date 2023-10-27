class Menu:
    @staticmethod
    def menu():
        print(" -- Menu --")
        print("1 - Cadastrar Paciente")
        print("2 - Cadastrar Funcionário")
        print("3 - Cadastrar Médico")
        print("4 - Listar Pacientes")
        print("5 - Listar Funcionários")
        print("6 - Listar Médicos")
        print("0 - Sair")
        return input("Infome uma opção: ")

    @staticmethod
    def dadosPessoais():
        print(" -- Informe os Dados Pessoais --")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        genero = input("Gênero (M - Masculino\nF - Feminino)\n: ")
        email = input("Cor: ")
        telefone = input("Telefone: ")
        dataNascimento = input("Data de Nascimento (DD/MM/YYYY): ")

        return nome, cpf, rg, genero, email, telefone, dataNascimento

    @staticmethod
    def dadosPaciente():
        kilometragem = input("KM: ")
        placa = input("Placa: ")
        return kilometragem, placa

    @staticmethod
    def dadosAutomovel():
        motorizacao = float(input("Motorizacao: "))
        portas = int(input("Portas: "))

        return motorizacao, portas

    @staticmethod
    def mostraVeiculo(lista: list):
        for a in lista:
            print(a)

    @staticmethod
    def dadosCaminhao():
        cargaMaxima = float(input("Carga Máxima: "))
        eixos = int(input("Eixos: "))

        return cargaMaxima, eixos

    @staticmethod
    def criaOnibus():
        print("Recupera dados do Onibus")

    @staticmethod
    def criaHelicoptero():
        print("Recupera dados do Helicoptero")
