import math
def searchx(a, b, f, e):
    while b-a > e:
        x = (a+b)/2
        if positivo(f(a))^positivo(f(x)): b = x
        else: a = x
    return x

def positivo(d):
    return d > 0

def f(argumento):
    return math.cos(argumento)-argumento ###   altere aqui sua função

def minimo(a,b,e):
    return int(math.log2(b-a)-math.log2(e))+1

print(f'    [x]: {searchx(0, 1, f, 0.05)}')
print(f'    [f(x)]: {f(searchx(0, 1, f, 0.05))}')