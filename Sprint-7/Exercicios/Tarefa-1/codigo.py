import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('actors.csv')

# 1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
atorMaisFilmes = df[df['Number of Movies'] == df['Number of Movies'].max()]
print("Ator/atriz com o maior número de filmes:")
print(f"{atorMaisFilmes['Actor'].values[0]} - {atorMaisFilmes['Number of Movies'].values[0]} filmes")

# 2. Apresente a média da coluna contendo o número de filmes.
mediaFilmes = df['Number of Movies'].mean()
print("\nMédia do número de filmes:", mediaFilmes)

# 3. Apresente o nome do ator/atriz com a maior média por filme.
df['Average per Movie'] = df['Total Gross'] / df['Number of Movies']
atorMediaFilme = df[df['Average per Movie'] == df['Average per Movie'].max()]
print("\nAtor/atriz com a maior média por filme:")
print(f"{atorMediaFilme['Actor'].values[0]} - {atorMediaFilme['Average per Movie'].values[0]}")

# 4. Apresente o nome do(s) 5 filme(s) mais frequente(s) e sua respectiva frequência.
top5 = df['#1 Movie'].value_counts().head(5).to_string()
print("\nOs 5 filmes mais frequentes e sua respectiva frequência:")
print(top5)
