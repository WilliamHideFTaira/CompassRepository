L = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(len(L)):
    if L[i] == L[i][::-1]:
        print("A palavra: {} é um palíndromo".format(L[i]))
    else:
        print("A palavra: {} não é um palíndromo".format(L[i]))