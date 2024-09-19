from comum import f
def searchx(a, b, f, e):
    while b-a > e:
        x = (a+b)/2
        if positivo(f(a))^positivo(f(x)): b = x
        else: a = x
    return x

def positivo(d):
    return d > 0

print(f'    [x]: {searchx(0, 1, f, 5e-2)}')
print(f'    [f(x)]: {f(searchx(0, 1, f, 5e-2))}')