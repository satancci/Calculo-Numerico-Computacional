from comum import f
def searchx(a, b, f, erro):
    anterior = 0; x=1
    while abs(x-anterior) >= erro:
        fb = f(b); fa=f(a); anterior = x
        x = (a*fb-b*fa)/(fb-fa)
        if positivo(f(a))^positivo(f(x)): b = x
        else: a = x
    return x

def positivo(d):
    return d > 0

print(f'    [x]: {searchx(0, 1, f, 5e-2)}')
print(f'    [f(x)]: {f(searchx(0, 1, f, 5e-2))}')