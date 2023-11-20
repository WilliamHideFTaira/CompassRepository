import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_1','S3_INPUT_PATH_2', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

from pyspark.sql import SparkSession

source_file = args['S3_INPUT_PATH_1']
target_path = args['S3_TARGET_PATH']

df_csv = spark.read.parquet(source_file)

source_file = args['S3_INPUT_PATH_2']

# Carregar dataframes para as tabelas dimensionais
df_cast = spark.read.parquet(f"{source_file}/ParquetCast")
df_crew = spark.read.parquet(f"{source_file}/ParquetCrew")
df_genres = spark.read.parquet(f"{source_file}/ParquetGenres")
df_json = spark.read.parquet(f"{source_file}/ParquetJSON")
df_production_companies = spark.read.parquet(f"{source_file}/ParquetProductionCompanies")
df_production_countries = spark.read.parquet(f"{source_file}/ParquetProductionCountries")
df_spoken_languages = spark.read.parquet(f"{source_file}/ParquetSpokenLanguages")
df_tabela_mn = spark.read.parquet(f"{source_file}/ParquetTabelaMN")

# Criar tabelas temporárias para realizar a junção
df_cast.createOrReplaceTempView("cast")
df_crew.createOrReplaceTempView("crew")
df_csv.createOrReplaceTempView("csv")
df_genres.createOrReplaceTempView("genres")
df_json.createOrReplaceTempView("json")
df_production_companies.createOrReplaceTempView("production_companies")
df_production_countries.createOrReplaceTempView("production_countries")
df_spoken_languages.createOrReplaceTempView("spoken_languages")
df_tabela_mn.createOrReplaceTempView("tabela_mn")

# Consultas SQL para criar tabelas dimensionais
dfDIMDiretores = spark.sql("""
    SELECT DISTINCT c.id_crew, c.name, c.known_for_department, c.job
    FROM crew c
    WHERE c.job = 'Director'
""")

dfDIMFilmes = spark.sql("""
    SELECT DISTINCT j.imdb_id, j.id, j.original_title AS titulo_principal,
                    j.original_title AS titulo_original, j.release_date AS ano_lancamento,
                    j.runtime AS tempo_minutos, j.popularity, j.vote_average AS nota_media,
                    j.vote_count AS numero_votos, j.budget, j.revenue
    FROM json j
""")

dfDIMProductionCompanies = spark.sql("""
    SELECT DISTINCT pc.company_id, pc.company_name, pc.origin_country
    FROM production_companies pc
""")

dfDIMGeneros = spark.sql("""
    SELECT DISTINCT g.genre_id, g.genre_name
    FROM genres g
""")

dfDIMProdCompanies = spark.sql("""
    SELECT DISTINCT pc.iso_3166_1, pc.country_name
    FROM production_countries pc
""")

dfLanguages = spark.sql("""
    SELECT DISTINCT sl.iso_639_1, sl.english_name, sl.language_name
    FROM spoken_languages sl
""")

dfFATOFilmes = spark.sql("""
    SELECT DISTINCT j.imdb_id, c.id_crew, pt.company_id, pt.genre_id,
                    pt.country_id, pt.language_id, (j.revenue - j.budget) AS profit
    FROM json j
    JOIN crew c ON j.id = c.id_filme AND c.job = 'Director'
    LEFT JOIN cast ct ON j.id = ct.id_filme
    LEFT JOIN tabela_mn pt ON j.id = pt.movie_id
    LEFT JOIN genres g ON pt.genre_id = g.genre_id
    LEFT JOIN production_companies pc ON pt.company_id = pc.company_id
    LEFT JOIN production_countries pco ON pt.country_id = pco.iso_3166_1
    LEFT JOIN spoken_languages sl ON pt.language_id = sl.iso_639_1
""")


# Salvar as tabelas dimensionais no formato parquet
dfDIMDiretores.write.parquet(f"{target_path}/DIM_Diretores")
dfDIMFilmes.write.parquet(f"{target_path}/DIM_Filmes")
dfDIMProductionCompanies.write.parquet(f"{target_path}/DIM_CompanhiasProducao")
dfDIMGeneros.write.parquet(f"{target_path}/DIM_Generos")
dfDIMProdCompanies.write.parquet(f"{target_path}/DIM_PaisesProducao")
dfLanguages.write.parquet(f"{target_path}/DIM_Idiomas")


# Registrar tabelas dimensionais no AWS Glue Data Catalog
#glueContext.create_dynamic_frame.from_catalog(frame = "dfDIMDiretores", database = "refined-database", table_name = "DIM_Diretores")
#glueContext.create_dynamic_frame.from_catalog(frame = "dfDIMFilmes", database = "refined-database", table_name = "DIM_Filmes")
#glueContext.create_dynamic_frame.from_catalog(frame = "dfDIMProductionCompanies", database = "refined-database", table_name = "DIM_CompanhiasProducao")
#glueContext.create_dynamic_frame.from_catalog(frame = "dfDIMGeneros", database = "refined-database", table_name = "DIM_Generos")
#glueContext.create_dynamic_frame.from_catalog(frame = "dfDIMProdCompanies", database = "refined-database", table_name = "Dim_PaisesProducao")
#glueContext.create_dynamic_frame.from_catalog(frame = "dfLanguages", database = "refined-database", table_name = "DIM_Idiomas")
#glueContext.create_dynamic_frame.from_catalog(frame = "df_fato_filmes_diretores_producao", database = "refined-database", table_name = "FATO_FilmesDiretoresProducao")

# Salvar a tabela fato no formato parquet
dfFATOFilmes.write.parquet(f"{target_path}/FATO_FilmesDiretoresProducao")
# Registrar tabela fato no AWS Glue Data Catalog
#glueContext.create_dynamic_frame.from_catalog(frame="dfFATOFilmes", database="refined-database", table_name="FATO_FilmesDiretoresProducao")

job.commit()