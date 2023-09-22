# Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2
# - feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as
# seguintes fórmulas:
# para homens: p = (72.7 * h) - 58
# para mulheres: p = (62.1 * h) - 44.7

altura = float(input("Informe a altura (em metros): "))
genero = input("Informe o gênero\n(1 - Masculino)\n(2 - Feminino): ")

pesoIdeal = 0

if genero == '1':
    pesoIdeal = (78.7 * altura) - 58
elif genero == '2':
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("Gênero não identificado. Não é possível calcular o peso ideal.")
if pesoIdeal > 0:
    print(f"Peso Ideal para seu genero é {pesoIdeal} kg!")