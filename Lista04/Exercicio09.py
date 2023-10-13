# Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número que ele
# gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is) posição(ões) ele foi encontrado e
# quantas ocorrências foram detectadas.

TAM = 10
numero = [0] * TAM

for i in range(TAM):
    numero[i] = int(input(f"Informe o {i + 1}° número inteiro: "))

verificaNumero = int(input(f"Informe o número que deseja pesquisar na lista: "))

for i in range(TAM):
    if numero[i] == verificaNumero:
        print(f"O número {verificaNumero} se encontra na(s) posição(ões) {i} da lista.")