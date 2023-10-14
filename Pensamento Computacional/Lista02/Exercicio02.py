# A partir do mês e ano de nascimento informado pelo usuário, elabore um algoritmo que
# informe a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer
# a carteira de motorista ou não, informando sua situação.

import datetime

mesAtual = datetime.datetime.now().month
anoAtual = datetime.datetime.now().year

mes = int(input("Informe o mês de nascimento: "))
ano = int(input("Informe o ano de nascimento: "))

idade = anoAtual - ano

if mesAtual < mes:
    idade -= 1

print(f"Você tem {idade} anos!")

if idade >= 18:
    print("Com essa idade, já pode tirar carteira de motorista!")
else:
    print("Com essa idade, ainda não pode tirar carteira de motorista!")
