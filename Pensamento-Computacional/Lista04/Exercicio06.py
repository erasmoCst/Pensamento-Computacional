# Ler 4 números inteiros e calcular a soma dos que forem par.

TAM = 4
numero = [0] * TAM
soma = 0

for i in range(TAM):
    numero[i] = int(input(f"Informe o {i + 1}° número inteiro: "))
    if numero[i] % 2 == 0:
        soma += numero[i]

print(f"\nSoma dos números pares: {soma}")
