# Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.

m = 1
n = 0
for i in range(100):
    n += 1
    print(f"{m} x {n} = {m * n}")
    if n == 10:
        m += 1
        n = 0
        print("\n")