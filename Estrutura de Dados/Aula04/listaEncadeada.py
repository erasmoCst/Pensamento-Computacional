class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def vazia(self):
        return self.cabeca is None

    def inserir_no_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def imprimir(self):
        print("Lista Encadeada:")
        atual = self.cabeca
        while atual != None:
            print(atual.valor, " ",end="")
            atual = atual.proximo

    def buscar(self, alvo):
        print(f"Busca número {alvo}:")
        atual = self.cabeca
        while atual != None:
            if atual.valor == alvo:
                return True
            else:
                atual = atual.proximo
        return False


    def tamanho(self):
        print(f"Tamanho lista:")
        tamanho = 0
        atual = self.cabeca
        while atual != None:
            tamanho += 1
            atual = atual.proximo
        return tamanho

    def inserir_no_fim(self, valor):
        atual = self.cabeca
        if self.vazia():
            self.inserir_no_inicio(valor)
        else:
            while atual.proximo != None:
                atual = atual.proximo
            atual.proximo = No(valor)

    def inserir_ordenado(self, valor):
        atual = self.cabeca
        if self.vazia():
            self.inserir_no_inicio(valor)
        else:
            while atual.proximo != None:
                if atual.valor < valor and atual.proximo.valor > valor:
                    novo_no = No(valor)
                    novo_no.proximo = atual.proximo
                    atual.proximo = novo_no
                    return
                atual = atual.proximo

    def remover(self, valor):
        if self.vazia():
            print("Lista vazia")
        elif self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
        else:
            atual = self.cabeca
            anterior = atual
            while atual != None:
                if atual.valor == valor:
                    anterior.proximo = atual.proximo
                    return
                anterior = atual
                atual = atual.proximo
            print(f"Valor {valor} não encontrado na lista")

    def remover_primeiro(self):
        if self.vazia():
            print("Lista vazia")
        else:
            self.cabeca = self.cabeca.proximo


    def remover_ultimo(self):
        atual = self.cabeca
        anterior = atual
        if self.vazia():
            print("Lista vazia")
        elif self.tamanho() == 1:
            self.remover_primeiro()
        else:
            while atual.proximo != None:
                atual = atual.proximo
                anterior = atual
            anterior.proximo = None


# Exemplo de uso:
lista = ListaEncadeada()
lista.remover_primeiro()
lista.remover_ultimo()
lista.inserir_ordenado(15)
lista.remover_ultimo()
lista.inserir_no_inicio(4)
lista.remover(4)
lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(1)
lista.inserir_no_fim(10)
lista.inserir_no_fim(30)
lista.inserir_ordenado(20)
lista.remover_primeiro()
lista.remover_ultimo()
lista.remover(20)
lista.remover(50)

lista.imprimir()
