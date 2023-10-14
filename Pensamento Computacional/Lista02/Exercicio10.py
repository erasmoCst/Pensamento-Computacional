# Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação
# segundo uma das seguintes categorias:
# - 5 até 7 anos: Infantil A;
# - 8 até 10 anos: Infantil B;
# - 11 até 13 anos: Juvenil A;
# - 14 até 17 anos: Juvenil B;
# - Maiores de 18 anos: Adulto.

idadeMinima = 5

idade = int(input("Informe a idade do nadador: "))

if idade < idadeMinima:
    print(f"Nadador muito novo. A idade mínima para classificação é de {idadeMinima} anos.")
elif idade <= 5 and idade <= 7:
    print("Classificação: Infantil A.")
elif idade <= 8 and idade <= 10:
    print("Classificação: Infantil B.")
elif idade <= 11 and idade <= 13:
    print("Classificação: Juvenil A.")
elif idade <= 14 and idade <= 17:
    print("Classificação: Juvenil B")
else:
    print("Classificação: Adulto")