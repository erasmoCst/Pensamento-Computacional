# Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo
# praticado. Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. Elabore um
# algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no
# estacionamento e mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado,
# R$ x”, no qual x será o valor a pagar calculado pelo algoritmo.
import math

valorMinimo = 8.0
valorFracinado = 1.5

minutos = int(input("Informe quantidade de minutos: "))

if minutos < 60:
    valorDevido = valorMinimo
else:
    valorDevido = math.ceil((minutos - 60) / 15) * valorFracinado + valorMinimo

print(f"Ao ficar estacionado {minutos} minutos deve-se pagar R${valorDevido:.2f}.")