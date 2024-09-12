from entrada import entrada 

def kojima(coeficientes):
    return sum(sorted([pow(abs(coeficientes[i]/coeficientes[0]), 1/i) for i in range(1, len(coeficientes))], reverse=True)[:2])

print(f'  cota de Kojima: {kojima(entrada())}')