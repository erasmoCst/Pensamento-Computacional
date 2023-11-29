# Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da
# seguinte forma:
# - Opção 1 - A vista - 8% de desconto
# - Opção 2 - em 2 parcelas - 4% de desconto, dividido em 2x
# - Opção 3 - em 3 parcelas - sem desconto, dividido em 3x
# - Opção 4 - em 4 parcelas - 4% de acréscimo, dividido em 4x
# Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto,
# mostrando então o valor calculado conforme a condição escolhida.

preco = float(input("Informe o preço do produto: R$"))
opcaoPgto = input("Informe a opção de pagamento\n1 - A Vista(8% de desconto)\n2 - Em 2x(4% de desconto)\n3 - Em 3x (valor integral)\n4 - Em 4x (4% de juros)\n")

valor = 0

if opcaoPgto == '1':
    valor = preco * 0.92
    parcelas = "A vista"
elif opcaoPgto == '2':
    valor = preco * 0.96
    parcelas = "2x"
elif opcaoPgto == '3':
    valor = preco
    parcelas = "3x"
elif opcaoPgto == '4':
    valor = preco * 1.04
    parcelas = "A vista"
else:
    print("Opção Inválida!")

if valor > 0:
    print(f"Com pagamento {parcelas}, o produto de R${preco:.2f}, fica por R${valor:.2f}.")
