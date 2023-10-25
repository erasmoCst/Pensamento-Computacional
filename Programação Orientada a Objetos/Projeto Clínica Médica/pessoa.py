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
    __slots__ = ["__salarioMensal", "jornadaTrabalho"]

    def __init__(self, nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, jornadaTrabalho):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento)
        self.__salarioMensal: float = salarioMensal
        self.jornadaTrabalho: int = jornadaTrabalho


class Medico(Funcionario):
    __slots__ = ["crm", "__valorConsulta", "especialidades"]

    def __init__(self, nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, jornadaTrabalho, crm, valorConsulta, especialidades):
        super().__init__(nome, cpf, rg, sexo, email, telefone, dataNascimento, salarioMensal, jornadaTrabalho)
        self.crm: str = crm
        self.__valorConsulta: float = valorConsulta
        self.especialidades: [] = especialidades