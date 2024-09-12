def entrada():
    while True:
        val = list(map(float, input("lista de coeficientes [1 -8 19 12]: ").split() or [1.0, -8.0, 19.0, 12.0]))
        if len(val) != 0:
            break
    return val