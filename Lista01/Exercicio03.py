nome = input("Informe o nome do profissional: ")
salario = float(input(f"Informe o salario do {nome}: "))
salarioMinimo = 1320.00
print(f"O salário do {nome} de {salario:.2f}, corresponde a de {(salario/salarioMinimo):.2f} salários mínimos de R${salarioMinimo:.2f}.")