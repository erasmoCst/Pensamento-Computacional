from view.menu import Menu
from models.paciente import Paciente

pacientes: list = []
__medicos: list = []

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
            case '1':
                cls.criaPaciente()
            case '2': pass
            case '3': pass
            case '4': pass
            case '5': pass
            case '6': pass

    @classmethod
    def criaPaciente(cls):
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        possuiConvenio, nomeConvenio = Menu.dadosPaciente()

        paciente = Paciente(cls, nome, cpf, rg, genero, email, telefone, dataNascimento, possuiConvenio, nomeConvenio)
        print(paciente)
        pacientes.append(paciente)