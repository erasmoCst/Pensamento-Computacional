import math

alturaCilindro = float(input("Informe a altura do tanque (em metros): "))
raioCilindro = float(input("Informe a raio do tanque (em metros): "))
precoLataTinta = 50
volumeLataTinta = 5
rendimentoLataTinta = 3
areaLateral = 2 * math.pi * raioCilindro * alturaCilindro
areaBase = math.pi * raioCilindro ** 2
areaTotal = 2 * areaBase + areaLateral
totalLataTinta = areaTotal/rendimentoLataTinta
print(f"Para pintar todo o tanque cilindro de {areaTotal:.2f}m² será necessário {math.ceil(totalLataTinta)} ({totalLataTinta:.2f}) latas de tinta de {volumeLataTinta} litros, custanto um total de R${math.ceil(totalLataTinta) * precoLataTinta:.2f} ")