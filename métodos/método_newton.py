from comum import parada, f, df
def newton(x):
    if x != 0:
        n = newton(x-1)
        return n-(f(n)/df(n))
    return 0

def nw(n, f , df, maxerro = 1e-5, maxitem = 100):
    k = 0
    while abs(f(n))> maxerro or k > maxitem:
        n -= (f(n)/df(n)) 
        k += 1
    return n

print(f'  método de newton: {parada(float(input("erro (recursividade) [1e-5]: ") or 1e-5), newton)}    (recursividade)')
print(f'  método de newton: {nw(0, f, df, float(input("erro (decremento contínuo) [1e-5]: ") or 1e-5))}    (decremento contínuo)\n')