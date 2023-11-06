from view.menu import Menu
from models.paciente import Paciente
from models.funcionario import Funcionario
from models.medico import Medico
from models.consulta import Consulta

pacientes: list = []
funcionarios: list = []
medicos: list = []
consultas: list =  []

class ControleClinica:

    @classmethod
    def run(cls):
        while True:
            opcao = Menu.menuPrincipal()

            if opcao == '0':
                break

            cls.opcoesMenu(opcao)

    @classmethod
    def opcoesMenu(cls, opcao):
        match opcao:
            case '1': cls.criaPaciente()
            case '2': cls.criaFuncionario()
            case '3': cls.criaMedico()
            case '4': cls.criaConsulta()
            case '5': cls.listaPaciente()
            case '6': cls.listaFuncionario()
            case '7':  cls.listaMedico()
            case '8':  cls.listaConsulta()
            case _:
                print("\n Opção Inválida!\n")

    @staticmethod
    def criaPaciente():
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        possuiConvenio, nomeConvenio = Menu.dadosPaciente()

        paciente = Paciente(nome, cpf, rg, genero, email, telefone, dataNascimento, possuiConvenio, nomeConvenio)
        pacientes.append(paciente)
        print("\nCliente Cadastrado com Sucesso!\n")

    @staticmethod
    def listaPaciente():
        if not len(pacientes):
            print("\n -- Nenhum paciente cadastrado --\n")
        else:
            print(" -- Lista de Pacientes --")
            for paciente in pacientes:
                print(paciente)

    @staticmethod
    def criaFuncionario():
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        jornada, salario = Menu.dadosFuncionario()

        funcionario = Funcionario(nome, cpf, rg, genero, email, telefone, dataNascimento, jornada, salario)
        funcionarios.append(funcionario)
        print("\nFuncionario Cadastrado com Sucesso!\n")

    @staticmethod
    def listaFuncionario():
        if not len(funcionarios):
            print("\n -- Nenhum Funcionario cadastrado --\n")
        else:
            print(" -- Lista de Funcionarios --")
            for funcionario in funcionarios:
                print(funcionario)

    @staticmethod
    def criaMedico():
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        jornada, salario = Menu.dadosFuncionario()
        crm, valorConsulta, especialidade = Menu.dadosMedico()

        medico = Medico(nome, cpf, rg, genero, email, telefone, dataNascimento, jornada, salario, crm, valorConsulta, especialidade)
        medicos.append(medico)
        print("\nMedico Cadastrado com Sucesso!\n")

    @staticmethod
    def listaMedico():
        if not len(medicos):
            print("\n -- Nenhum Medico cadastrado --\n")
        else:
            print(" -- Lista de Médicos --")
            for medico in medicos:
                print(medico)

    @staticmethod
    def criaConsulta():
        medico, paciente, data = Menu.dadosConsulta()

        consulta = Consulta(medico, paciente, data)
        consultas.append(consulta)
        print("\nConsulta Cadastrado com Sucesso!\n")

    @staticmethod
    def listaConsulta():
        if not len(consultas):
            print("\n -- Nenhuma Consulta cadastrada --\n")
        else:
            print(" -- Lista de Consultas --")
            for consulta in consultas:
                print(consulta)

    @staticmethod
    def criaPrescricao():
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        jornada, salario = Menu.dadosFuncionario()
        crm, valorConsulta, especialidade = Menu.dadosMedico()

        medico = Medico(nome, cpf, rg, genero, email, telefone, dataNascimento, jornada, salario, crm, valorConsulta, especialidade)
        medicos.append(medico)
        print("\nMedico Cadastrado com Sucesso!\n")

    @staticmethod
    def listaPrescricao():
        if not len(consultas):
            print("\n -- Nenhuma Consulta cadastrada --\n")
        else:
            print(" -- Lista de Consultas --")
            for consulta in consultas:
                print(consulta)
