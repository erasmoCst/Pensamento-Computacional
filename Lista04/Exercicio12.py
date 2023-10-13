import random

numerosSorteados = []
numerosApostados = []
i = 0
count = 0

# Sortea 6 números no intervalo de 1 a 60
while len(numerosSorteados) < 6:
    numero = random.randint(1, 60)
    # Valida op número sorteado, evitando repetição
    if numero not in numerosSorteados:
        numerosSorteados.append(numero)

# Usuário digita os número que deseja apostar
while len(numerosApostados) < 6:
    numero = int(input(f"Informe o {len(numerosApostados) + 1}° número que deseja apostar (entre 1 e 60): "))

    # Valida o número digitado, evitando repetição
    if numero < 1 or numero > 60:
        print("Número inválido! Informe números entre 1 e 60. ")
    else:
        if numero in numerosApostados:
            print("Número já apostado, digite outro número")
        else:
            numerosApostados.append(numero)

# Compara os números sorteados com os números apostados
while i < 6:
    if numerosApostados[i] in numerosSorteados:
        count += 1
    i += 1


print(f"Números sorteados: {numerosSorteados}")
print(f"Número apostados: {numerosApostados}")
print(f"Total de número acertados: {count}")