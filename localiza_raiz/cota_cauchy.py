from entrada import entrada 

def soma_cauchy(coeficientes):
    return tuple((abs(coeficientes[i]/coeficientes[0]), len(coeficientes)-1-i) for i in range(1, len(coeficientes)))

def cauchy(x, pol):
    if x != 0:
        d = cauchy(x-1, pol)
        return pow(sum([pol[i][0]*pow(d, pol[i][1]) for i in range(0, len(pol))]), 1/(len(pol)))
    return 0

print(f'  cota de Cauchyd: {cauchy(int(input("parada desejada [5]: ") or 5), soma_cauchy(entrada()))}')