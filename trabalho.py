def main():
    n = input("")
    P = read_poly(int(n))
    a_b = compute_best_quota(P);
    print(f'Best quotas = {a_b}')
    x = compute_root(P, float(a_b[0]), float(a_b[1]))
    print(f'{x:.6f}')

def soma_cauchy(coeficientes):
    return tuple((abs(coeficientes[i]/coeficientes[0]), len(coeficientes)-1-i) for i in range(1, len(coeficientes)))

def cauchy(x, pol):
    if x != 0:
        d = cauchy(x-1, pol)
        return pow(sum([pol[i][0]*pow(d, pol[i][1]) for i in range(0, len(pol))]), 1/(len(pol)))
    return 0

def compute_root(P, a, b):
    return falsapos_searchx(P, a, b) if f(a, P)*f(b, P) <= 0 else secante(a, b, P)
    
def compute_best_quota(p):
    resultados = []
    minimo = r_min(p)
    resultados.append(r_max(p)-minimo)
    resultados.append(cauchy(100, soma_cauchy(p))-minimo)
    resultados.append(kojima(p)-minimo)
    return [f'{minimo:.2f}', f'{min(resultados)+minimo:.2f}']

def read_poly(grau):
    coeficientes = []
    while len(coeficientes) <= grau:
        coeficientes.append(int(input("")))
    return coeficientes

def r_max(coeficientes):
    return 1 + (max([abs(num) for num in coeficientes][1:])/abs(coeficientes[0]))

def r_min(coeficientes):
    return 1 / (1+(max([abs(num) for num in coeficientes][:-1])/abs(coeficientes[-1])))

def soma_cauchy(coeficientes):
    return tuple((abs(coeficientes[i]/coeficientes[0]), len(coeficientes)-1-i) for i in range(1, len(coeficientes)))

def cauchy(x, pol):
    if x != 0:
        d = cauchy(x-1, pol)
        return pow(sum([pol[i][0]*pow(d, pol[i][1]) for i in range(0, len(pol))]), 1/(len(pol)))
    return 0

def kojima(coeficientes):
    return sum(sorted([pow(abs(coeficientes[i]/coeficientes[0]), 1/i) for i in range(1, len(coeficientes))], reverse=True)[:2])

def falsapos_searchx(coef, a, b):
    anterior = contador = 0; x = 1
    while abs(x-anterior) >= 0.00000001 and contador < 5000:
        contador += 1
        fb = f(b, coef); fa=f(a, coef); anterior = x
        x = (a*fb-b*fa)/(fb-fa)
        if positivo(f(a, coef))^positivo(f(x, coef)): b = x
        else: a = x
    
    return x

def f(argumento, coeficientes):
    return sum([coeficientes[i]*pow(argumento, len(coeficientes)-1-i) for i in range(len(coeficientes))])

def positivo(d):
    return d > 0

def secante(a, b, coeficientes):
    x0 = (a+b)/2
    x1 = x0 + 0.01
    soma = contador = 0
    while abs((x1 - x0)) >= 0.0000001 and contador <= 5000: 
        contador += 1
        soma = x0 - (f(x0, coeficientes)*(x1-x0)/(f(x1, coeficientes)-f(x0, coeficientes)))
        x0 = x1
        x1 = soma
    return soma

if __name__ == '__main__':
    main()