# Um produtor de abóboras deve verificar a classificação dos seus produtos para posterior
# empacotamento e venda. Um de seus clientes compra apenas abóboras médias (aquelas
# que possuem o diâmetro (d) no intervalo 15 cm ≤ d < 20 cm). Elabore um algoritmo que
# leia o diâmetro de uma abóbora e mostre se ela é do tipo médio ou não. Caso ela não se
# encaixe na classificação, informe “produto fora das medidas”.

diametro = float(input("Informe o diametro da abóbora (em centímetros): "))

if diametro < 15 or diametro >= 20:
    print("Produto fora das medidas.")
else:
    print("Abóbora do tipo médio!")