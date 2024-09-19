import math
def parada(erro, funcao):
    anterior = 0
    atual = i = 1
    while abs((atual-anterior)/atual) >= erro:
        i += 1
        anterior = atual
        atual = funcao(i)
    return atual

def f(argumento):
    return math.cos(argumento)-argumento ### altere aqui sua função

def df(argumento):
    return -math.sin(argumento)-1 ### aqui a derivada dela

def minimo(a,b,e): ### quantidade mínima exclusivo para a bipartição
    return int(math.log2(b-a)-math.log2(e))+1