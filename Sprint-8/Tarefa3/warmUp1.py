import random

# 250 inteiros aleatórios
lista = [random.randint(1, 1000) for _ in range(250)]
# Reverse
lista.reverse()

print(lista)