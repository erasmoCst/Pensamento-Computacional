import random
matriz = []
TAMANHO = 4

for i in range(TAMANHO):
    matriz.append([])
    for j in range(TAMANHO):
        matriz[i].append(random.randint(1,50))

for i in matriz:
    print(i)
