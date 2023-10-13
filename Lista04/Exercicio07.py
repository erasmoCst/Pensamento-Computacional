# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é
# triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.

numero = -1

while numero < 0:
    numero = int(input(f"Informe um número inteiro positivo: "))

i = 0
triangular = False

while i < numero:
    if i * (i + 1) * (i + 2) == numero:
        triangular = True
        i = numero
    else:
        i += 1

if triangular:
    print(f"\nO número é triangular!")
else:
    print(f"\nO número não é triangular!")
