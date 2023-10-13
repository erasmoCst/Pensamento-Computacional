# Leia dois valores reais do teclado, calcular e imprimir na tela:
# a) A soma destes valores b) O produto deles c) O quociente entre eles

TAM = 2
numero = [0] * TAM

for i in range(TAM):
    numero[i] = float(input(f"Informe o {i + 1}° número: "))

# a) A soma destes valores
print(f"{numero[0]} + {numero[1]} = {numero[0] + numero[1]}")

# b) O produto deles
print(f"{numero[0]} * {numero[1]}  = {numero[0] * numero[1]}")

# c) O quociente entre eles
print(f"{numero[0]} / {numero[1]}  = {numero[0] / numero[1]}")
