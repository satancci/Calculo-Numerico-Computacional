import math

def newton(x):
    if x != 0:
        n = newton(x-1)
        return n-((math.cos(n)-n)/(-math.sin(n)-1))
    return 0

def parada(erro):
    xant = 0
    xo = i = 1
    while abs((xo-xant)/xo) >= erro:
        i += 1
        xant = xo
        xo = newton(i)
    return xo

print(f'  método de newton: {parada(float(input("erro [0.001]: ") or 0.001))}')