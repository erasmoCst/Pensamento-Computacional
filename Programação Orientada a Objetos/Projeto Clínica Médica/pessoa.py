from typing import List
from datetime import datetime
class Pessoa:
    codigo: int = 1
    __slots__ = ["nome", "__cpf", "__rg", "sexo", "__email", "__telefone", "dataNascimento"]

    def __init__(self, nome, cpf, rg, sexo, email, telefone, dataNascimento):
        self.codigo = Pessoa.codigo
        self.nome: str = nome
        self.__cpf: str = cpf
        self.__rg: str = rg
        self.sexo: str = sexo
        self.__email: str = email
        self.__telefone: str = telefone
        self.dataNascimento: str = dataNascimento
        Pessoa.codigo += 1

class Paciente(Pessoa):
    __slots__ = ["possuiConvenio", "nomeConvenio"]

    def __init__(self, nome, cpf, rg, sexo, email, telefone, dataNascimento, possuiConvenio, nomeConvenio):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.possuiConvenio: bool = possuiConvenio
        if possuiConvenio:
            self.nomeConvenio: str = nomeConvenio
        else:
            self.nomeConvenio: str = "Não Possui Convênio"


class Funcionario(Pessoa):
    __slots__ = ["__salarioMensal", "horarioEntrada", "horiarioSaida"]

    def __init__(self, nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, horarioEntrada, horiarioSaida):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.__salarioMensal: float = salarioMensal
        self.horarioEntrada: str = horarioEntrada
        self.horiarioSaida: str = horiarioSaida

class Medico(Funcionario):
    __slots__ = ["crm", "__valorConsulta", "especialidades"]

    def __init__(self, nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, jornadaTrabalho, crm, valorConsulta, especialidades: List[Especialidades]):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, jornadaTrabalho)
        self.crm: str = crm
        self.__valorConsulta: float = valorConsulta
        self.especialidades: List[Especialidades] = especialidades

class Especialidades:
    codigo: int = 1
    __slots__ = ["nome", "descricao"]

    def __init__(self, nome, descricao):
        self.nome: str = nome
        self.descricao: str = descricao
        Especialidades.codigo += 1

class Pagamento:
    __slots__ = ["data", "__valor", "__funcionario"]

    def __init__(self, data: datetime, valor: float, funcionario: Funcionario):
        self.__data: datetime = data
        self.__valor: float = valor
        self.__funcionario: Funcionario = funcionario
