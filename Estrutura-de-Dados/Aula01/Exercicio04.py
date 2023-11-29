import random

def gerarMatriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        matriz.append(linha)
    return matriz


matrizZone = gerarMatriz()
print("0 = Não tem Mina!")
print("1 = Perdeu, tem mina!")

cont = 0
while cont < 11:
    linhaAleatoria = random.randint(1, 9)
    colunaAleatoria = random.randint(1, 9)

    if matrizZone[linhaAleatoria][colunaAleatoria] != 1:
        matrizZone[linhaAleatoria][colunaAleatoria] = 1
        cont += 1
for elementos in matrizZone:
    print(elementos)