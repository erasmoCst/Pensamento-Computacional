import datetime


class Menu:
    @staticmethod
    def menuPrincipal():
        print(" -- Menu --")
        print("1 - Cadastrar Paciente")
        print("2 - Cadastrar Funcionário")
        print("3 - Cadastrar Médico")
        print("4 - Cadastrar Consulta")
        print("5 - Listar Pacientes")
        print("6 - Listar Funcionários")
        print("7 - Listar Médicos")
        print("8 - Listar Consultas")
        print("9 - Listar Cobranças")
        print("0 - Sair")
        return input("Infome uma opção: ")

    @staticmethod
    def dadosPessoais():
        print(" -- Informe os Dados Pessoais --")
        nome: str = input("Nome Completo: ")
        cpf: str = input("CPF: ")
        rg: str = input("RG: ")
        genero: str = input("Gênero \nM - Masculino\nF - Feminino\n").upper()

        while genero not in ("M", "F"):
            print("Dado inválido! Informe 'M' para Masculino e 'F' para Feminino")
            genero = input("Gênero \nM - Masculino\nF - Feminino\n").upper()

        email: str = input("E-mail: ")
        telefone: str = input("Telefone: ")
        dataNascimento: datetime.date = input("Data de Nascimento (DD/MM/AAAA): ")

        return nome, cpf, rg, genero, email, telefone, dataNascimento

    @staticmethod
    def dadosPaciente():
        print(" -- Informe os Dados do Paciênte --")
        convenio: str = None

        while convenio not in ("S", "N"):
            convenio = input("O paciente possui convênio? \n'S' - Sim\n'N' - Não\n").upper()
            if (convenio == "S"):
                possuiConvenio: bool = True
                nomeConvenio: str = input("Convênio do paciente: ")
            elif (convenio == "N"):
                possuiConvenio: bool = False
                nomeConvenio: str = "-"
            else:
                print("Dado inválido! Informe 'S' para Sim e 'N' para não")
        return possuiConvenio, nomeConvenio

    @staticmethod
    def dadosFuncionario():
        print(" -- Informe os Dados do Funcionário --")
        entrada = datetime.time(input("Horário de Entrada: "))
        saida = datetime.time(input("Horário de Saída: "))
        salario: str = input("Salário: ")
        jornada: str = f"{entrada}h às {saida}h"
        return jornada, salario

    @staticmethod
    def dadosMedico():
        print(" -- Informe os Dados do Médico --")
        especialidade: str = None
        especialidades: list = []

        crm: str = input("CRM: ")
        valorConsulta: float = input("Valor da Consulta: R$")

        while especialidade != 'Sair':
            especialidade = input("Especialidade (digite 'sair' para finalizar o cadastro): ").capitalize()

            if especialidade != 'Sair':
                especialidades.append(especialidade)
        return crm, valorConsulta, especialidades

    @staticmethod
    def dadosConsulta():
        dataCobranca: datetime.date = None
        valorTotal: float = None
        criarCobranca: str = None

        print(" -- Informe os Dados da Consulta --")

        medico: str = input("Informe o Nome do Médico: ")
        paciente: str = input("Informe o Nome do Paciente: ")
        data: datetime = input("Informe a data e hora da consulta (DD/MM/AAAA HH:MM:SS): ")

        while criarCobranca not in ("S", "N"):
            criarCobranca = input("\nDeseja criar a cobrança desta consulta?\n'S' - Sim\n'N' - Não\n").upper()
            if (criarCobranca == "S"):
                dataCobranca = input("Informe a data da cobrança(DD/MM/AAAA): ")
                valorTotal = float(input("Informe o valor total da consulta: "))
                return medico, paciente, data, dataCobranca, valorTotal
            elif (criarCobranca == "N"):
                return medico, paciente, data, dataCobranca, valorTotal
            else:
                print("Dado inválido! Informe 'S' para Sim e 'N' para não")

    @staticmethod
    def dadosPrescricao():
        print(" -- Informe os Dados da Prescrição Médica --")
        exame: str = None
        exames: list = []
        medicamento: str = None
        medicamentos: list = []

        data: datetime.date = input("Informe a data da prescrição (DD/MM/AAAA): ")
        while exame != 'Sair':
            exame: str = input("Exames (digite 'sair' para finalizar o cadastro): ").capitalize()
            if exame != 'Sair':
                exames.append(exame)
        while medicamento != 'Sair':
            medicamento: str = input("Medicamentos (digite 'sair' para finalizar o cadastro): ").capitalize()
            if medicamento != 'Sair':
                medicamentos.append(medicamento)
        return data, exames, medicamentos
