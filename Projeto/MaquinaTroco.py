## Projeto: M A Q U I N A   D E   T R O C O
## Autor: Erasmo Costa
import random

def validaNumeroRealPositivo(entrada):
    numerosValidos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",",", "."]
    simbolosValidos = [",", "."]
    qtdSimbolos = 0

    for char in entrada:
        if char not in numerosValidos:
            return False
        if char in simbolosValidos:
            qtdSimbolos += 1
    if qtdSimbolos > 1:
        return False
    return True

def recebeEntradaUsuario(complemento):
    checkEntrada = False
    entrada = input(f"\nInforme o valor total {complemento}: R$")
    if entrada == 'sair' or entrada == 'SAIR':
        return -1
    while not checkEntrada:
        checkEntrada = validaNumeroRealPositivo(entrada)
        if not checkEntrada:
            print(f"\nValor inválido! Infome um valor válido.")
    if "," in entrada:
        entrada = entrada.replace(",", ".")
    entrada = float(entrada)
    return entrada

def formataTipoCedula(cedula,qtdCedula):
    if cedula > 1:
        if qtdCedula > 1:
            return "notas"
        return "nota"
    else:
        if qtdCedula > 1:
            return "moedas"
        return "moeda"

def formataBRL(valor):
    return f"R${valor:.2f}".replace(".", ",")

def calculaTrocoDisponivel(cedulas, estoqueCedulas):
    trocoDisponivel = 0
    for i in range(len(cedulas)):
        trocoDisponivel += cedulas[i] * estoqueCedulas[i]
    return trocoDisponivel
##
cedulas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
estoqueCedulas = [0] * len(cedulas)
trocoDisponivel = calculaTrocoDisponivel(cedulas, estoqueCedulas)

for i in range(len(estoqueCedulas)):
    if cedulas[i] > 1:
        estoqueCedulas[i] = random.randint(0, 10)
    else:
        estoqueCedulas[i] = random.randint(0, 20)

print("MÁQUINA DE TROCO - digite 'sair' para sair")

while True:
    valorConta = recebeEntradaUsuario("da conta")
    if valorConta < 0:
        break
    elif valorConta == 0:
        print("A conta não possui valor. Não é necessário troco.\n")
    else:
        qtdCedula = 0
        valorPagamento = recebeEntradaUsuario("do pagemento")

        if valorPagamento < 0:
            break

        troco = valorPagamento - valorConta

        if troco < 0:
            print("\nValor do pagamento insuficiente!\n")
        elif troco == 0:
            print("\nValor do pagamento igual ao valor da conta. Não é necessário troco!")
        else:
            print(f"\nO troco é {formataBRL(troco)}.")

            if trocoDisponivel < troco:
                print(f"\nNão há troco o suficiente no caixa! Troco total em caixa: R${formataBRL(trocoDisponivel)}.")
            else:
                print(f"A melhor forma de pagar o troco é: ")
                for i in range(len(cedulas)):
                    while troco >= cedulas[i] and estoqueCedulas[i]:
                        troco -= cedulas[i]
                        qtdCedula += 1
                        estoqueCedulas[i] -= 1
                    nomeCedula = formataTipoCedula(cedulas[i], qtdCedula)
                    if qtdCedula > 0:
                        if cedulas[i] < 1:
                            if cedulas[i] == 0.01:
                                print(f"{qtdCedula} {nomeCedula} de {cedulas[i] * 100:.0f} centavo.")
                            else:
                                print(f"{qtdCedula} {nomeCedula} de {cedulas[i] * 100:.0f} centavos.")
                        else:
                            print(f"{qtdCedula} {nomeCedula} de R${cedulas[i]},00.")
                    qtdCedula = 0

            trocoDisponivel = calculaTrocoDisponivel(cedulas, estoqueCedulas)
            print(f"\n--Troco total em caixa: R${formataBRL(trocoDisponivel)}.--")