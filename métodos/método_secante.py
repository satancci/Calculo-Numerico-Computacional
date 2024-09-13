import math
from parada import parada
def secante(x):
    if x >= 2:
        x1 = secante(x-1)
        x0 = secante(x-2)
        fx1 = math.cos(x1)-x1
        return x1-(fx1/((fx1-(math.cos(x0)-x0))/(x1-x0)))
    if x == 1:
        return 0.001
    return 0

print(f'  método das secantes: {parada(float(input("erro [0.001]: ") or 0.001), secante)}')