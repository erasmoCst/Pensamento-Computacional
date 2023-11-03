matriz = [[10,20,30],
          [40,50,60],
          [70,80,90]]

soma = 0
for i in matriz:
    for j in i:
        soma += j
print(soma)