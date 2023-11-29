def merge(l1, l2):
    l3 = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    while i < len(l1):
        l3.append(l1[i])
        i += 1
    while j < len(l2):
        l3.append(l2[j])
        j += 1
    return l3

# Exemplos de uso
listaA = [1, 3, 5, 7, 9]
listaB = [2, 4, 6, 8, 10]

print(merge(listaA, listaB))
