# IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
# IMC = massa / altura2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do
# usuário e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o
# critério apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC<
# 25. Caso não esteja, calcule sua massa máxima considerada normal (usando IMC igual
# a 24,9).

peso = float(input("Informe o peso (em kg): "))
altura = float(input("Informe a altura (em metros): "))

imc = peso / (altura * altura)
print(f"IMC: {imc}")

if imc >= 18.5 and imc < 25:
    print("Este IMC é considerado normal")
else:
    print("Este IMC é considerado está fora da faixa normal (18.5 <= imc < 25)")
    print(f"A massa mínima considerada normal é de {18.5 *  altura ** 2}")
    print(f"A massa máxima considerada normal é de {24.9 *  altura ** 2}")

