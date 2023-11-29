'''class Conta:
    titular: str = None
    numero: str = None
    saldo: float = None
    limite: float = None
    ativa: bool = None

conta1 = Conta()
conta2 = Conta()

conta1.titular = "Erasmo Costa"
conta1.numero = "12111999"
conta1.saldo = 89897897.99
conta1.limite = 90000000
conta1.ativa = True

conta2.titular = "Rebeca Rufo"
conta2.numero = "15101999"
conta2.saldo = 150000000.99
conta2.limite = 200000000
conta2.ativa = True
'''
class Conta:
    codigo: int = 0
    def __init__(self, titular: str, numero: str, saldo: float, limite: float, ativa: bool = True):
        Conta.codigo += 1
        (self).codigo = Conta.codigo
        self.titular: str = titular
        self.numero: str = numero
        self.saldo: float = saldo
        self.limite: float = limite
        self.ativa: bool = ativa
    
    def saque(self, valor: float):
        if self.ativa:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente!")
        else:
            print("Conta inativa!")

    def deposito(self, valor: float):
        if self.ativa:
            self.saldo += valor
        else:
            print("Conta inativa!")

    def extrato(self):
        print(f"Titular: {self.titular}\n"\
              f"Saldo: R${self.saldo:.2f}\n"\
              f"Limite: R${self.limite:.2f}\n")
        
    def __str__(self):
        return f"Código: {self.codigo}\n"\
                f"Titular: {self.titular}\n"\
                f"Número: {self.numero}\n"\
                f"Saldo: {self.saldo}\n"\
                f"Limite: {self.limite}\n"\
                f"Ativa: {self.ativa}\n"
             
conta1 = Conta("Erasmo Costa", "12111999", 4000.99, 12000, True)
conta2 = Conta("Rebeca Rufo", "15101999", 5000.99, 8000, True)
conta1.saque(1000)
conta1.extrato()
conta2.deposito(4000)
conta2.extrato()