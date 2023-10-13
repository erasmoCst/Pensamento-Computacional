# Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

TAM = 3
numero = [0] * TAM

for i in range(TAM):
    numero[i] = float(input(f"Informe o {i + 1}° número: "))

if numero[0] > numero[1] + numero[2]:
    print(f"O número {numero[0]} é maior que a soma de {numero[1]} + {numero[2]} = {numero[1] + numero[2]}.")
else:
    print(f"O número {numero[0]} é menor que a soma de {numero[1]} + {numero[2]} = {numero[1] + numero[2]}.")