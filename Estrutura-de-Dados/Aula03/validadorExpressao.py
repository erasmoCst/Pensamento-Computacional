def verificaDelimitadores(expressao):
    pilha = []
    abreExpressao = "({["
    fechaExpressao = ")}]"

    for caracter in expressao:
        if caracter in abreExpressao:
            pilha.append(caracter)
        elif caracter in fechaExpressao:
            if not pilha:
                return False
            topo = pilha.pop()
            if abreExpressao.index(topo) != fechaExpressao.index(caracter):
                return False

    return not pilha


expressao1 = "(5 + 50) * ((2 + 7) + 2"
expressao2 = "[5 + 50) * (2 + 7) + 2"
expressao3 = "{[(5 + 50) * (2 + 7)] + 2}"
expressao4 = "(((5 + 50) * (2 + 7)) + 2)"
expressao5 = "{[(5 + 50)} * (2 + 7)] + 2}"
expressao6 = "{2 / [5* (9 + 20)* 3] +11}"

print(verificaDelimitadores(expressao1))
print(verificaDelimitadores(expressao2))
print(verificaDelimitadores(expressao3))
print(verificaDelimitadores(expressao4))
print(verificaDelimitadores(expressao5))
print(verificaDelimitadores(expressao6))