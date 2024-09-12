import math

def newton(x):
    if x != 0:
        n = newton(x-1)
        return n-((math.cos(n)-n)/(-math.sin(n)-1))
    return 0

def parada(erro):
    atual = 0
    anterior = i = 1
    while abs((atual-anterior)/atual) >= erro:
        i += 1
        anterior = atual
        atual = newton(i)
    return atual

print(f'  método de newton: {parada(float(input("erro [0.001]: ") or 0.001))}')
