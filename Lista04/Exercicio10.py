# Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido. Depois, crie dois outros
# vetores: vPares, contendo somente os números pares de vLido, e vImpares contendo somente os números ímpares de vLido.
# Os vetores vPares e vLido não deverão conter zeros. Mostre então os três vetores.

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
print("Números Pares:",vPar)
print("Números Ímpares:",vImpar)