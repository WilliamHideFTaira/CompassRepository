arquivo = 'actors.csv'

atores = []
with open(arquivo, 'r') as file:
    linha = file.readlines()
    
    coluna = linha[0].strip().split(',')
    
    for line in linha[1:]:
        nomeAtor = ''
        lista = []
        aspas = False
        
        for char in line.strip():
            if char == '"':
                aspas = not aspas
            elif char == ',' and not aspas:
                lista.append(nomeAtor.strip())
                nomeAtor = ''
            else:
                nomeAtor += char
        
        lista.append(nomeAtor.strip())
        
        ator = {}
        ator[coluna[0]] = lista[0]
        ator[coluna[1]] = float(lista[1])
        ator[coluna[2]] = int(lista[2])
        ator[coluna[3]] = float(lista[3])
        ator[coluna[4]] = lista[4]
        ator[coluna[5]] = float(lista[5])
        
        atores.append(ator)

# =================================================================================================

# 1- Encontre o ator/atriz com o maior número de filmes
numMaxF = max(atores, key=lambda x: x['Number of Movies'])
atorMaisFilmes = numMaxF['Actor']
numFilmes = numMaxF['Number of Movies']

with open('etapa-1.txt', 'w', encoding="utf-8") as file:
    file.write("1- Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.\n")
    file.write(f"R: ATOR/ATRIZ: {atorMaisFilmes} / NÚMERO DE FILMES: {numFilmes} FILMES")

# =================================================================================================

# 2- Calcule a média de receita de bilheteria bruta dos principais filmes
vlrBruto = [entry['Gross'] for entry in atores]
mediaBruta = sum(vlrBruto) / len(vlrBruto)

with open('etapa-2.txt', 'w', encoding="utf-8") as file:
    file.write("2- Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. Estamos falando aqui da média da coluna Gross.\n")
    file.write(f'R: MÉDIA DE RECEITA DE BILHETERIA BRUTA: ${mediaBruta:.2f} milhões de dólares.')

# =================================================================================================

# 3- Encontre o ator/atriz com a maior média de receita de bilheteria bruta por filme
maiorMediaPorATOR = max(atores, key=lambda x: x['Average per Movie'])
atorMaiorMedia = maiorMediaPorATOR['Actor']
mediaMAXbruto = maiorMediaPorATOR['Average per Movie']

with open('etapa-3.txt', 'w', encoding="utf-8") as file:
    file.write("3- Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. Considere a coluna Avarage per Movie para fins de cálculo.\n")
    file.write(f'R: ATOR/ATRIZ: {atorMaiorMedia} / MÉDIA: ${mediaMAXbruto:.2f} MILHÕES DE DÓLARES POR FILMES.')

# =================================================================================================

# 4- Contagem de aparições dos filmes de maior bilheteria
contFilmes = {}
for ator in atores:
    filme = ator['#1 Movie']
    if filme in contFilmes:
        contFilmes[filme] += 1
    else:
        contFilmes[filme] = 1

# Ordene os filmes por quantidade e nome
filmesOrd = sorted(contFilmes.items(), key=lambda x: (-x[1], x[0]))

with open('etapa-4.txt', 'w', encoding='utf-8') as file:
    file.write("4- A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do  filme.\n")
    file.write("Ao escrever no arquivo, considere o padrão de saída <sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset, adicionando um resultado a cada linha.\n")
    file.write("R: Os filmes de maior bilheteria aparecem no dataset da seguinte forma:\n")
    for i, (filme, quantidade) in enumerate(filmesOrd, 1):
        file.write(f'{i} - O filme "{filme}" aparece {quantidade} vez(es) no dataset.\n')

# =================================================================================================

# 5- Ordene os atores pela receita bruta de bilheteria de seus filmes em ordem decrescente
atoresOrd = sorted(atores, key=lambda x: x['Total Gross'], reverse=True)

with open('etapa-5.txt', 'w', encoding="utf-8") as file:
    file.write("5- Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente.\n")
    file.write("Ao escrever no arquivo, considere o padrão de saída <nome do ator> -  <receita total bruta>, adicionando um resultado a cada linha.\n")
    file.write("R: LISTA:\n")
    for actor_entry in atoresOrd:
        file.write(f"{actor_entry['Actor']} - {actor_entry['Total Gross']:.2f}\n")
