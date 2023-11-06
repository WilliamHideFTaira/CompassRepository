import random
import time
import names
import os

random.seed(40)

# Declaração variáveis
nomesUnicos = 3000
nomesAleatorios = 10000000
aux = []

for i in range(nomesUnicos):
    aux.append(names.get_full_name())
dados = []

for i in range(nomesAleatorios):
    dados.append(random.choice(aux))

arquivo = "nomes_aleatorios.txt"
with open(arquivo, "w") as file:
    for nome in dados:
        file.write(nome + "\n")

if os.path.exists(arquivo):
    print(f"Arquivo {arquivo} gerado com sucesso!")
else:
    print(f"Falha ao gerar o arquivo.")