def buscaBinaria(lista, item):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return -1

listaA = [2, 10, 23, 45, 59, 62, 75, 77, 80, 92, 93, 98]
valor = int(input("Informe o número que deseja buscar: "))

posicao = buscaBinaria(listaA, valor)
if posicao < 0:
    print(f"O valor {valor} não está na lista!")
else:
    print(f"O valor informado {valor} está na {posicao}ª posição da lista")    