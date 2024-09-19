from comum import parada, f
def secante(x):
    if x >= 2:
        x1 = secante(x-1)
        x0 = secante(x-2)
        return x1-(f(x1)/((f(x1)-f(x0))/(x1-x0)))
    if x == 1:
        return 1e-3
    return 0

print(f'  método das secantes: {parada(float(input("erro [1e-4]: ") or 1e-4), secante)}')