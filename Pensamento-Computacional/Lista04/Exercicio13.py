# Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente, utilizando a seguinte
# estratégia de ordenação:
# • selecione o elemento do vetor de 20 posições que apresenta o menor valor;
# • troque este elemento pelo primeiro;
# • repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de menor valor com a segunda
# posição), depois os 18 elementos (trocando o de menor valor com a terceira posição), depois os 17, 16 e assim por diante,
# até restar um único elemento, o maior deles.
# Observação: este método de ordenação é conhecido como “Seleção Direta”

TAM = 20
vLido = [0] * TAM

# Entrada de dados
for i in range(TAM):
    vLido[i] = int(input(f"Informe o {i + 1}° número inteiro positivo: "))

for i in range(19):
    menor = i
    j = i + 1
    while j < 20:
        if vLido[j] < vLido[menor]:
            menor = j
        j += 1
    aux = vLido[i]
    vLido[i] = vLido[menor]
    vLido[menor] = aux

print(vLido)