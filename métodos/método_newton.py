import math
from parada import parada
from time import time
def newton(x):
    if x != 0:
        n = newton(x-1)
        return n-(f(n)/df(n))
    return 0

def nw(n, f, df, maxerro = 1e-5, maxitem = 10):
    k = 0
    while abs(f(n))> maxerro or k > maxitem:
        n = n-(f(n)/df(n)) 
        k += 1
    return n

def f(x):
    return math.cos(x)-x

def df(x):
    return -math.sin(x)-1

print(f'  método de newton: {parada(float(input("erro [0.001]: ") or 1e-3), newton)}')