# Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de
# 100 cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20.
# Elabore um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.

custoPoucaCopia = 0.25
custoMais100Copia = 0.2

copias = int(input("Informe o número de cópias: "))

if copias < 0:
    print("Número de copias inválido! Informe uma quantidade maior que zero!")
elif copias > 100:
    print(f"Para tirar {copias} fotocópias, o valor é de R${copias * custoMais100Copia:.2f}.")
else:
    print(f"Para tirar {copias} fotocópias, o valor é de R${copias * custoPoucaCopia:.2f}.")
