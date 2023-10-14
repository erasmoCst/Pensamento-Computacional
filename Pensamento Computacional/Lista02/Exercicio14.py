# Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.

valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
valor3 = int(input("Insira o terceiro valor: "))

if valor1 > valor2 > valor3:
    print(valor1, valor2, valor3)
elif valor1 > valor3 > valor2:
    print(valor1, valor3, valor2)
elif valor2 > valor1 > valor3:
    print(valor2, valor1, valor3)
elif valor2 > valor3 > valor1:
    print(valor2, valor3, valor1)
elif valor3 > valor1 > valor2:
    print(valor3, valor1, valor2)
elif valor3 > valor2 > valor1:
    print(valor3, valor2, valor1)
