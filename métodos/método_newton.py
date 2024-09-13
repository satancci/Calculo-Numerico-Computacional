import math
from parada import parada
def newton(x):
    if x != 0:
        n = newton(x-1)
        return n-((math.cos(n)-n)/(-math.sin(n)-1))
    return 0

print(f'  método de newton: {parada(float(input("erro [0.001]: ") or 0.001), newton)}')