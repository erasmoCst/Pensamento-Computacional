# Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
# “Valor inválido” para números negativos).

numero = int(input("Informe um número inteiro: "))

if numero < 0:
    print("Número inválido! Informe um número maior que 0!")
else:
    print(f"A raíz quadrada de {numero} é {numero**0.5:.2f}.")