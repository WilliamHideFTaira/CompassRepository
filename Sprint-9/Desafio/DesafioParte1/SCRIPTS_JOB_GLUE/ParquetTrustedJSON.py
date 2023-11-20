import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH_1', 'S3_TARGET_PATH_2', 'S3_TARGET_PATH_3', 'S3_TARGET_PATH_4', 'S3_TARGET_PATH_5', 'S3_TARGET_PATH_6'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

from pyspark.sql import SparkSession # Import de biblioteca adicional
from pyspark.sql.functions import explode, col, explode_outer # Import de biblioteca adicional

source_file = args['S3_INPUT_PATH']
target_path1 = args['S3_TARGET_PATH_1']
target_path2 = args['S3_TARGET_PATH_2']
target_path3 = args['S3_TARGET_PATH_3']
target_path4 = args['S3_TARGET_PATH_4']
target_path5 = args['S3_TARGET_PATH_5']
target_path6 = args['S3_TARGET_PATH_6']

dfCompleto = spark.read.json(source_file, multiLine=True) # DataFrame completo json

# DataFrame para "genres"
dfGenres = dfCompleto.select(
    explode("genres").alias("genre")
).select(
    col("genre.id").alias("genre_id"),
    col("genre.name").alias("genre_name")
).dropDuplicates(["genre_id"])

# DataFrame para "production_companies"
dfProductionCompanies = dfCompleto.select(
    explode("production_companies").alias("production_company")
).select(
    col("production_company.id").alias("company_id"),
    col("production_company.logo_path").alias("logo_path"),
    col("production_company.name").alias("company_name"),
    col("production_company.origin_country").alias("origin_country")
).dropDuplicates(["company_id"])

# DataFrame para "production_countries"
dfProductionCountries = dfCompleto.select(
    explode("production_countries").alias("production_country")
).select(
    col("production_country.iso_3166_1").alias("iso_3166_1"),
    col("production_country.name").alias("country_name")
).dropDuplicates(["iso_3166_1"])

# DataFrame para "spoken_languages"
dfSpokenLanguages = dfCompleto.select(
    explode("spoken_languages").alias("spoken_language")
).select(
    col("spoken_language.english_name").alias("english_name"),
    col("spoken_language.iso_639_1").alias("iso_639_1"),
    col("spoken_language.name").alias("language_name")
).dropDuplicates(["iso_639_1"])

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

# Remover colunas do DataFrame dfCompleto
colunas = ["genres", "production_companies", "production_countries", "spoken_languages"]
dfCompleto = dfCompleto.drop(*colunas)

dfCompleto.write.parquet(target_path1)
dfGenres.write.parquet(target_path2)
dfProductionCompanies.write.parquet(target_path3)
dfProductionCountries.write.parquet(target_path4)
dfSpokenLanguages.write.parquet(target_path5)
dfAssociations.write.parquet(target_path6)

job.commit()