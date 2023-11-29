# Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um algoritmo que leia o
# código da moeda que o cliente quer comprar e qual o montante que ele quer adquirir nessa moeda.
# Mostre então quanto ele deverá pagar em reais para concretizar a operação. Além da cotação, a empresa
# cobra uma comissão de 5% (quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual
# a R$1.000). Considere o câmbio do dia.

cambioDia = [5, 6, 7]
cambioMoeda = ['dol', 'eur', 'lib']

moeda = input("Informe a moeda que deseja comprar\nDolar: digite 'dol'\nEuro: digite 'eur'\nLibra: digite 'lib'\n")

while moeda not in cambioMoeda:
    moeda = input("Moeda inválida! Informe uma moeda válida!\nDolar: digite 'dol'\nEuro: digite 'eur'\nLibra: digite 'lib'\n")

montante = int(input("Informe o montante que deseja comprar: "))

if moeda == 'dol':
    valorTotal = montante * cambioDia[0]
elif moeda == 'eur':
    valorTotal = montante * cambioDia[1]
elif moeda == 'lib':
    valorTotal = montante * cambioDia[2]

if valorTotal < 1000:
    valorTotal = valorTotal * 1.05
else:
    valorTotal = valorTotal * 1.03

print(f"Para comprar {montante} {moeda}, você deve pagar R${valorTotal:.2f}.")