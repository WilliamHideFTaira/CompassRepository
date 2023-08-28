def my_map(lista, deff):
    x = []
    for elemento in lista:
        x.append(deff(elemento))
    return x

def potencia_de_2(x):
    return x ** 2

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = my_map(L, potencia_de_2)

print(res)