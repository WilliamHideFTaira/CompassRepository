# Leitura do arquivo CSV
with open('estudantes.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

# Lista para armazenar os resultados
result = []

# Processamento das linhas do arquivo
for linha in linhas:
    partes = linha.strip().split(',')
    nome = partes[0]
    notas = list(map(int, partes[1:]))
    notas.sort(reverse=True) # Ordena as notas em ordem decrescente 
    tres_maiores_notas = notas[:3] # Seleciona as três maiores notas
    media = round(sum(tres_maiores_notas) / 3, 2) # Média das três maiores notas
    resultado = f"Nome: {nome} Notas: {tres_maiores_notas} Média: {media}"
    result.append(resultado) # Adiciona o restulado à lista de resultados

# Ordena os resultados pelo nome do estudante
result = sorted(result)

# Imprime os resultados
for resultado in result:
    print(resultado)
