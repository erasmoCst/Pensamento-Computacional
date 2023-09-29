# Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então qual o valor da soma e
# da média aritmética do conjunto.

i = 0
soma = 0
quantidadeInput = 10

while i < quantidadeInput:
    soma += int(input(f"Informe o {i+1}° número inteiro: "))
    media = soma/quantidadeInput
    i += 1

print(f"Soma dos números: {soma}")
print(f"Media dos números: {media:.2f}")