# Abre o arquivo para leitura
with open('number.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

listaInteiros = list(map(lambda linha: int(linha.strip()), linhas)) # Converte as linhas em números inteiros
listaPares = list(filter(lambda numero: numero % 2 == 0, listaInteiros)) # Filtra apenas os números pares
listaMaioresPares = sorted(listaPares, reverse=True)[:5] # Ordem decrescente
soma = sum(listaMaioresPares) # Soma dos cinco maiores números pares

print(listaMaioresPares)
print(soma)