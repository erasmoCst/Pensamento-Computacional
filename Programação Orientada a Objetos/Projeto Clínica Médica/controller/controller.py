from ..view.menu import Menu
from ..models.paciente import Paciente

__pacientes: list = []
__medicos: list = []

class ControleCriacao:

    @classmethod
    def opcoesMenu(cls, opcao):
        match opcao:
            case '1':
                cls.criaPaciente(Menu.dadosPessoais(), Menu.dadosPaciente())
            case '2': pass
            case '3': pass
            case '4': pass
            # case '5': Menu.mostraVeiculo(cls.__automoveis)
            # case '6': Menu.mostraVeiculo(cls.__caminhoes)
            # case '6': Menu.mostraVeiculo(cls.__onibus)

    @staticmethod

    @classmethod
    def criaPaciente(cls):
        nome, cpf, rg, genero, email, telefone, dataNascimento = Menu.dadosPessoais()
        possuiConvenio, nomeConvenio = Menu.dadosPaciente()

        paciente = Paciente(nome, cpf, rg, genero, email, telefone, dataNascimento, possuiConvenio, nomeConvenio)

        cls.__pacientes.append(paciente)