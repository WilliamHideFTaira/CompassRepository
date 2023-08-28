def divide_lista(L):
    tam = len(L)
    x = []
    y = []
    z = []
    divisa = tam//3
    x = lista[:divisa]
    y = lista[divisa:2* divisa]
    z = lista[2*divisa:]
    return x, y, z

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
X, Y, Z = divide_lista(lista)
print(X, Y, Z)