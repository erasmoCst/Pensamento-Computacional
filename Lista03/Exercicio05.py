# Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário.

n = int(input("Informe um número inteiro: "))
i = 1

if n % 2 != 0:
    n += 1

while i < n:
    print(i)
    i += 2