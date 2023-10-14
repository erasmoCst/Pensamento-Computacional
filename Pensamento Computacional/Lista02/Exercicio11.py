# A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a massa
# em kg de um boxeador e mostre a qual categoria ele pertence. Caso ele não se encaixe,
# informe “Categoria inferior a Super-médio”. Lembrando que 1 quilograma = 2,20462262
# libras.
# - 161 a 168 super-médio
# - 169 a 175 meio-pesado
# - 176 a 200 cruzador
# - 201 ou mais peso-pesado

pesoKg = float(input("Informe o peso do boxeador (em kg): "))

pesoLbs = pesoKg * 2.20462262

if pesoLbs >= 161 and pesoLbs <= 168:
    categoria = "Super-Médio"
elif pesoLbs >= 169 and pesoLbs <= 175:
    categoria = "Meio-Pesado"
elif pesoLbs >= 176 and pesoLbs <= 200:
    categoria = "Cruzador"
elif pesoLbs >= 201:
    categoria = "Peso-Pesado"
else:
    categoria = "inferior a Super-Médio"

print(f"Categoria {categoria}")