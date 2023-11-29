# Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores positivos. Modifique
# então o vetor de forma que, tenhamos primeiro todos os números pares, depois, os números impares. Mostre o vetor antes de
# depois da modificação.

TAM = 10
vLido = [0] * TAM
vPar = []
vImpar = []

for i in range(TAM):
    numero = int(input(f"Informe o {i + 1}° número inteiro positivo: "))
    while numero <= 0:
        print("Numero inválido")
        numero = int(input(f"Informe o {i + 1}° número inteiro positivo: "))
    vLido[i] = numero

    if vLido[i] % 2 == 0:
        vPar.append(vLido[i])
    else:
        vImpar.append(vLido[i])

print("Números:", vLido)

for i in range(len(vPar)):
    vLido[i] = vPar[i]


for i in range(len(vImpar)):
     vLido[len(vPar) + i] = vImpar[i]

print("Números:", vLido)
