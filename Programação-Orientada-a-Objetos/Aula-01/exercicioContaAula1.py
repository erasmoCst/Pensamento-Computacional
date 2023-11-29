def criarConta():
    titular = input("Titular: ")
    numero = input("Número: ")
    saldo = float(input("Saldo: "))
    limite = float(input("Limite: "))
    status = True if input("ATIVA (S/N): ").upper() == "S" else False

    return dict(titular=titular, numero=numero, saldo=saldo, limite=limite, ativa=status)

def imprimirDados(conta: dict):
    print(f"Titular: {conta['titular']} \n"
          f"Numero: {conta['numero']} \n"
          f"Saldo: {conta['saldo']} \n"
          f"Limite: {conta['limite']} \n"
          f"Status: {'Ativa' if conta['ativa'] else 'Inativa'} \n")

def depositar(conta, valor):
    conta['saldo'] = conta['saldo'] + valor  # conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] = conta['saldo'] - valor # conta['saldo'] -= valor

def transferir(transfere, recebe, valor):
    transfere['saldo'] -= valor
    recebe['saldo'] += valor
criar = True
contasLista = []
while criar:
    criar = True if input("Deseja criar uma conta? (S/N)").upper() == "S" else False
    if criar:
        conta = criarConta()
        contasLista.append(conta)
    else:
        break

for conta in contasLista:
    imprimirDados(conta)

transferir(contasLista[0], contasLista[1], 1000)