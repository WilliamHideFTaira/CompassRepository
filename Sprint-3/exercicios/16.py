def somaValoresString(L):
    soma = 0
    L = L.split(',')
    for i in L:
        soma += int(i)
    return soma

valoresString = "1,3,4,6,10,76"
x = somaValoresString(valoresString)
print(x)