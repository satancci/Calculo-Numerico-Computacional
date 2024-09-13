def parada(erro, funcao):
    anterior = 0
    atual = i = 1
    while abs((atual-anterior)/atual) >= erro:
        i += 1
        anterior = atual
        atual = funcao(i)
    return atual