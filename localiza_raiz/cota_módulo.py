from entrada import entrada 

def r_max(coeficientes):
    return 1 + (max([abs(num) for num in coeficientes][1:])/coeficientes[0])

def r_min(coeficientes):
    return 1 / (1+(max([abs(num) for num in coeficientes][:-1])/coeficientes[-1]))

func = entrada()
print(f'  valor máximo: {r_max(func):.4f}')
print(f'  valor mínimo: {r_min(func):.4f}')