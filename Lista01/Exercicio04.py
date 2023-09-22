precoProduto = float(input("Informe o valor do produto: "))
descontoAVista = 5
acrescimoParcela = 5
print(f"Valor do produto para pagamento a vista ({descontoAVista:.2f}% de desconto) R${precoProduto * (1 - (descontoAVista / 100)):.2f}")
print(f"Valor da parcela em 2x é de: R${precoProduto/2:.2f} por parcela.")
print(f"Valor da parcela em 3x é de: R${precoProduto * (1 + acrescimoParcela / 100) / 3:.2f} por parcela.")
