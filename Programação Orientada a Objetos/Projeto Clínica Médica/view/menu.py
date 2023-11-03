class Menu:
    @staticmethod
    def menuPrincipal():
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
        nome = input("Nome Completo: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        genero = input("Gênero (M - Masculino F - Feminino): ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        dataNascimento = input("Data de Nascimento (DD/MM/YYYY): ")

        return nome, cpf, rg, genero, email, telefone, dataNascimento

    @staticmethod
    def dadosPaciente():
        possuiConvenio = input("O paciente possui convênio? \n'S' - Sim\n'N' - Não\n").upper()
        if(possuiConvenio == "S"):
            nomeConvenio = input("Convênio do paciente: ")
        elif(possuiConvenio == "N"):
            nomeConvenio = "-"
        else:
            print("Dado inválido! Informe 'S' para Sim e 'N' para não")
        return possuiConvenio, nomeConvenio

    @staticmethod
    def dadosFuncionario():
        jornada = input("Jornada de Trabalho: ")
        salario = input("Salário: ")
        return jornada, salario
    
    @staticmethod
    def dadosMedico():
        crm = input("CRM: ")
        valorConsulta = input("Valor da Consulta: ")
        especialidade = input("Especialidade: ")
        return crm, valorConsulta, especialidade