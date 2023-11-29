# Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os valores inteiros de li e lf
# devem ser informados pelo usuário e não pertencem ao intervalo, ou seja, intervalo aberto.

multiplicador = int(input(f"Informe o multiplicador: "))

limiteInicial = int(input(f"Informe o limite inicial: "))
limiteFinal = int(input(f"Informe o limite final: "))

while limiteFinal < limiteInicial:
    print("O limite final não pode ser menor que o limite inicial!")
    limiteFinal = int(input(f"Informe outro número para ser o limite final: "))

print(f"Múltiplos de {multiplicador} entre {limiteInicial} e {limiteFinal}: ")

if limiteInicial % multiplicador != 0:
    i = round(limiteInicial/multiplicador) * multiplicador
    print(i)
    if i == 0:
        i += 1
    # OU AINDA
    #i = limiteInicial + (multiplicador - limiteInicial % multiplicador)
else:
    i = limiteInicial + multiplicador

while limiteInicial < i < limiteFinal:
    print(i)
    i += multiplicador