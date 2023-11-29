# Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.

valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
valor3 = int(input("Insira o terceiro valor: "))

if valor1 > valor2 > valor3:
    maiorValor = valor1
elif valor2 > valor1 > valor3:
    maiorValor = valor2
elif valor3 > valor2 > valor1:
    maiorValor = valor3

print(f"O maior valor é {maiorValor}.")