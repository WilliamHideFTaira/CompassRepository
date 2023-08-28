# Você deve Utilizar a função enumerate().
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, pNome in enumerate(primeirosNomes):
    print(f"{i} - {pNome} {sobreNomes[i]} está com {idades[i]} anos")