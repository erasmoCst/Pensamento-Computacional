def buscaBinaria(A, item):
    esq,dir = 0, len(A) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            dir = meio - 1
        else:
            esq = meio + 1
    return 'O valor informado não consta na lista'

A = [0, 12, 22, 44, 49, 52, 62, 77, 88, 99]
print("Resultado:", buscaBinaria(A, 22))
print("Resultado :", buscaBinaria(A, 0))
print("Resultado:", buscaBinaria(A, 150))
print("Resultado:", buscaBinaria(A, 52))
print("Resultado:", buscaBinaria(A, 88))
print("Resultado:", buscaBinaria(A, 44))
print("Resultado:", buscaBinaria(A, 100))