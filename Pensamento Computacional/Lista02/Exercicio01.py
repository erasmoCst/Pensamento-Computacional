# Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("Informe um número: "))

if numero % 2 != 0:
    print(f"O número {numero} é ímpar!")
else:
    print(f"O número {numero} é par!")