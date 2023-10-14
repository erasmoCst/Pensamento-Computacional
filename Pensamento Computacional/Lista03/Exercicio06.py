# Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de 1 a 20 polegadas. A
# conversão entre estas duas unidades é dada por: centímetro = polegada × 2,54

i = 1

while i <= 20:
    print(f"{i} cm = {i * 2.54} pol")
    i += 1