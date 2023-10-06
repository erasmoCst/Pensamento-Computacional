## Projeto: M A Q U I N A   D E   T R O C O
## Autor: Erasmo Costa

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

    while not checkEntrada:
        entrada = input(f"Informe o valor total {complemento}: R$")
        checkEntrada = validaNumeroRealPositivo(entrada)
        if not checkEntrada:
            print(f"Valor inválido! Infome um valor válido.")
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

##
valorConta = recebeEntradaUsuario("da conta")

if valorConta == 0:
    print("A conta não possui valor. Não é necessário troco.")
else:
    qtdCedula = 0
    cedulas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

    valorPagamento = recebeEntradaUsuario("do pagemento")
    auxValorConta = valorPagamento - valorConta

    if auxValorConta < 0:
        print("Valor do pagamento insuficiente!")
    elif auxValorConta == 0:
        print("Valor do pagamento igual ao valor da conta. Não é necessário troco!")
    else:
        trocoFormatado = f"R${valorPagamento - valorConta:.2f}".replace(".",",")
        print(f"O troco é {trocoFormatado}. A melhor forma de pagar o troco é: ")
        for cedula in cedulas:
            while auxValorConta >= cedula:
                auxValorConta -= cedula
                qtdCedula += 1
            nomeCedula = formataTipoCedula(cedula, qtdCedula)
            if qtdCedula > 0:
                if cedula < 1:
                    if cedula == 0.01:
                        print(f"{qtdCedula} {nomeCedula} de {cedula * 100:.0f} centavo.")
                    else:
                        print(f"{qtdCedula} {nomeCedula} de {cedula * 100:.0f} centavos.")
                else:
                    print(f"{qtdCedula} {nomeCedula} de R${cedula},00.")
            qtdCedula = 0