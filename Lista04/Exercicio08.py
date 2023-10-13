# A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor máximo e o valor mínimo
# de uma amostra. Elabore um programa que leia um vetor de 10 posições inteiras e então mostre o valor máximo, o valor
# mínimo e a amplitude amostral do conjunto fornecido.

TAM = 10
numero = [0] * TAM
max = 0
min = 0

for i in range(TAM):
    numero[i] = int(input(f"Informe o {i + 1}° número inteiro: "))
    if i == 0:
        max = numero[i]
        min = numero[i]
    else:
        if numero[i] > max:
            max = numero[i]
        elif numero[i] < min:
            min = numero[i]

print(f"\n")
print(f"Menor valor: {min}")
print(f"Maior valor: {max}")
print(f"Amplitude Amostral: {max - min}")