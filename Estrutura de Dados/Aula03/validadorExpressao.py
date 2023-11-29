def verificaDelimitadores(expressao):
    pilha = []
    delimitadoresAbertura = "({["
    delimitadoresFechamento = ")}]"

    for char in expressao:
        if char in delimitadoresAbertura:
            pilha.append(char)
        elif char in delimitadoresFechamento:
            if not pilha:
                return False
            topo = pilha.pop()
            if delimitadoresAbertura.index(topo) != delimitadoresFechamento.index(char):
                return False

    return not pilha


expressao1 = "(9+2)*(32+11)"
expressao2 = "(3+8)*)22+17)"
expressao3 = "(2+8)*[33+88)"
expressao4 = "(((2+11) - 5 )* 7)"
expressao5 = "(((3+3))*5)"
expressao6 = "({2+2])-(5+2)"
print(verificaDelimitadores(expressao1))
print(verificaDelimitadores(expressao2))
print(verificaDelimitadores(expressao3))
print(verificaDelimitadores(expressao4))
print(verificaDelimitadores(expressao5))
print(verificaDelimitadores(expressao6))