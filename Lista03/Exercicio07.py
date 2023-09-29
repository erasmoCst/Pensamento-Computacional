# Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela de conversão de
# metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10 quilômetros.

i = 20

while i <= 160:
    print(f"{i} km = {i * 1.609344:.2f} mi")
    i += 10