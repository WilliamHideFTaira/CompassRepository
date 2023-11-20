# Desafio Sprint 9

O desafio na Sprint 9 consiste em: processamento da Trusted, Modelagem de dados da Refined e processamento da Refined. Para cada um dos estágios, algumas séries de jobs e buckets foram criados no processo:

## Parte 1

Nessa primeira parte, o começo foi a criação de arquivos parquet a partir do arquivo movies.csv original. O arquivo series.csv foi desconsiderado pois não entrará na análise final. O spark dispõe de bibliotecas que recebem um arquivo csv inteiro com `dfCSV = spark.read.csv(source_file, header=True, sep='|')`, onde foi necessário o uso do "sep = '|'", pois define o separador do arquivo .csv.

```
from pyspark.sql import SparkSession

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

dfCSV = spark.read.csv(source_file, header=True, sep='|')
dfCSV.write.parquet(target_path)
```

Após isso, notei a falta de alguns dados que poderiam ser necessários para a análise, então foi feita uma alteração no AWS Lambda, com foco em buscar mais dados em sua forma mais "bruta" da API. Abaixo segue a principal mudança, onde os dados foram simplesmente armazenados como json, sem nenhum filtro, com o propósito de manter os dados da forma mais original possível:
```
for movie_id in filmesTerror['id']:
        # Busca por informações do filme (id)
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url)
        filmeInfo = response.json()

        # Busca por informações da equipe
        url_credits = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
        response_credits = requests.get(url_credits)
        credits_info = response_credits.json()

        # Adiciona o JSON completo de filmeInfo ao vetor rentaveis
        rentaveis.append(filmeInfo)

        # Adiciona o JSON completo de credits_info a outro vetor
        equipe_info.append(credits_info)
```
Nota-se que foram duas requisições a API, então foram necessários dois jobs para processar os json resultantes da Lambda. Com isso, foi feito o código para receber todos os json do diretório e armazená-los como arquivos parquet em sua pasta com a data de extração (inserida na variável S3_TARGET_PATH). 

Lidando com a primeira requisição, nota-se que a estrutura do arquivo possui listas que poderiam dificultar a análise posteriormente. Foi usada a função explode para criar novas tabelas a partir do dataframe dos arquivos json. Abaixo um exemplo da estrutura:
```
from pyspark.sql import SparkSession # Import de biblioteca adicional
from pyspark.sql.functions import explode, col, explode_outer # Import de biblioteca adicional

dfCompleto = spark.read.json(source_file, multiLine=True) # DataFrame completo json

# DataFrame para "genres"
dfGenres = dfCompleto.select(
    explode("genres").alias("genre")
).select(
    col("genre.id").alias("genre_id"),
    col("genre.name").alias("genre_name")
).dropDuplicates(["genre_id"])
```

Para "relacionar" essas tabelas, foi feita uma tabela M:N que liga todas as tabelas que foram criadas: Genres, ProductionCountries, SpokenLanguages e ProductionCompanies. Como a função explode só aceita um argumento, minha solução foi usar join:
```
# DataFrame para a tabela de associação M:N
dfAssociations = dfCompleto.select(
    col("id").alias("movie_id"),
    explode_outer("genres").alias("genre")
).select(
    "movie_id",
    col("genre.id").alias("genre_id")
).dropDuplicates(["movie_id", "genre_id"])

dfAssociations = dfAssociations.join(
    dfCompleto.select(
        col("id").alias("movie_id"),
        explode_outer("production_companies").alias("production_company")
    ).select(
        "movie_id",
        col("production_company.id").alias("company_id")
    ).dropDuplicates(["movie_id", "company_id"]),
    on="movie_id"
)

dfAssociations = dfAssociations.join(
    dfCompleto.select(
        col("id").alias("movie_id"),
        explode_outer("production_countries").alias("production_country")
    ).select(
        "movie_id",
        col("production_country.iso_3166_1").alias("country_id")
    ).dropDuplicates(["movie_id", "country_id"]),
    on="movie_id"
)

dfAssociations = dfAssociations.join(
    dfCompleto.select(
        col("id").alias("movie_id"),
        explode_outer("spoken_languages").alias("spoken_language")
    ).select(
        "movie_id",
        col("spoken_language.iso_639_1").alias("language_id")
    ).dropDuplicates(["movie_id", "language_id"]),
    on="movie_id"
)
```

Por fim, cada um dos dataframes foi guardado em um diretório diferente, mas mantendo a regra de data de extração e em formato parquet:

```
dfCompleto.write.parquet(target_path1)
dfGenres.write.parquet(target_path2)
dfProductionCompanies.write.parquet(target_path3)
dfProductionCountries.write.parquet(target_path4)
dfSpokenLanguages.write.parquet(target_path5)
dfAssociations.write.parquet(target_path6)

```

Para o job da segunda requisição, o foco era conseguir relacionar um único id de filme a todos os participantes (elenco ou equipe) daquele filme. Foi realizado a separação de duas tabelas: crew e cast, cada uma tendo o id do filme mais a informação da pessoa que trabalhou no filme. Veja uma parte do código:
```
dfCompleto = spark.read.json(source_file, multiLine=True)
dfCompleto = dfCompleto.withColumn("id_filme", col("id"))

# Explode o DataFrame do elenco (cast)
dfCast = dfCompleto.select(
    col("id_filme"),
    explode("cast").alias("pessoa_cast")
).select(
    col("id_filme"),
    col("pessoa_cast.adult"),
    col("pessoa_cast.gender"),
    col("pessoa_cast.id").alias("id_actor"),
    col("pessoa_cast.known_for_department"),
    col("pessoa_cast.name"),
    col("pessoa_cast.original_name"),
    col("pessoa_cast.popularity"),
    col("pessoa_cast.cast_id"),
    col("pessoa_cast.character"),
    col("pessoa_cast.credit_id"),
    col("pessoa_cast.order")
)
```
Após a criação das duas tabelas, a mesma regra de guardar os arquivos parquet com data de extração foi aplicada.

Para confirmar a estrutura correta das tabelas, foi criado um Crawler que criou as tabelas em um database, e a partir do Athena foi possível fazer buscas e conferir os dados e estrutura das tabelas.

## Parte 2

Para a modelagem dimensional, foi usada a ferramenta do site app.sqldbm.com. Com ela foi possível fazer a modelagem da análise que eu pensei para o desafio final: diretores, seus filmes de TERROR e seus resultados: comparação lado a lado com as empresas que as produzem. A ideia é ver se as empresas de filmes trazem um sistema rentável, que tende a melhorar ou piorar com o tempo, e a reflexão desses resultados nos diretores. Achei necessário pegar apenas as informações do diretor de cada filme, as informações das companias de produção, os dados sobre os filmes (principalmente popularidade, budget/revenue, nota média e número de votos, focando bastante no desempenho desses filmes), os gêneros para poder comparar se terror misturado com outros gêneros podem gerar resultados diferentes, e idiomas falados.

## Parte 3

O processamento da Refined ficou no S3. Ainda não foi verificado se as estruturas estão corretas, mas na data de hoje (20/11/2023), isso ainda será analisado e resolvido. Essa mensagem não existirá posteriormente. Foi usada apenas um job para criação das tabelas do modelo dimensional, que pegou todos os arquivos parquet criados na primeira parte desse desafio, os processou em novas tabelas e foram separados em um novo bucket refined.
```
# Criação da tabela dimensional DIMDiretores
dfDIMDiretores = spark.sql("""
    SELECT DISTINCT c.id_crew, c.name, c.known_for_department, c.job
    FROM crew c
    WHERE c.job = 'Director'
""")
```