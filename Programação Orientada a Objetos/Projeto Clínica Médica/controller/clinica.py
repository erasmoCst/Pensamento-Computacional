from view.menu import Menu
from models.paciente import Paciente
from models.funcionario import Funcionario
from models.medico import Medico
from models.consulta import Consulta
from models.prescricao import Prescricao

pacientes: list = []
funcionarios: list = []
medicos: list = []
consultas: list = []
prescricoes: list = []

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
            case '5': cls.listaCadastro("Paciente", pacientes)
            case '6': cls.listaCadastro("Funcionario", funcionarios)
            case '7': cls.listaCadastro("Médico", medicos)
            case '8': cls.listaCadastro("Consulta", consultas)
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
    def criaFuncionario():
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        jornada, salario = Menu.dadosFuncionario()

        funcionario = Funcionario(nome, cpf, rg, genero, email, telefone, dataNascimento, jornada, salario)
        funcionarios.append(funcionario)
        print("\nFuncionario Cadastrado com Sucesso!\n")


    @staticmethod
    def criaMedico():
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        jornada, salario = Menu.dadosFuncionario()
        crm, valorConsulta, especialidade = Menu.dadosMedico()

        medico = Medico(nome, cpf, rg, genero, email, telefone, dataNascimento, jornada, salario, crm, valorConsulta, especialidade)
        medicos.append(medico)
        print("\nMedico Cadastrado com Sucesso!\n")

    @classmethod
    def criaConsulta(cls):
        medico, paciente, data = Menu.dadosConsulta()
        prescricao = cls.criaPrescricao()
        consulta = Consulta(medico, paciente, data, prescricao)
        consultas.append(consulta)

        print("\nConsulta Cadastrado com Sucesso!\n")

    @staticmethod
    def criaPrescricao():
        data, exames, medicamentos = Menu.dadosPrescricao()

        prescricao = Prescricao(data, exames, medicamentos)
        prescricoes.append(prescricao)
        print("\nPrescricao Cadastrada com Sucesso!\n")
        return prescricao

    @staticmethod
    def listaCadastro(nomeCadastro: str, cadastro: list):
        if not len(cadastro):
            print(f"\n -- Nenhum {nomeCadastro} cadastrado --\n")
        else:
            print(f" -- Lista de {nomeCadastro}s --")
            for item in cadastro:
                print(item)
