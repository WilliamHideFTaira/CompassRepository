import random

random_list = random.sample(range(500), 50)
mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

random_list.sort()

tam = len(random_list)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / tam
if (tam % 2 != 0):
    mediana = random_list[tam//2]
else: 
    a = random_list[(tam // 2) - 1]
    b = random_list[tam // 2]
    mediana  = (a + b) / 2
print("Media: {}, Mediana: {}, Mínimo: {}, Máximo: {}".format(media, mediana, valor_minimo, valor_maximo))
