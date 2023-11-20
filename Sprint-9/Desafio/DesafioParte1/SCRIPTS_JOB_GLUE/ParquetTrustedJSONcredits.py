import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH_1', 'S3_TARGET_PATH_2'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

from pyspark.sql.functions import explode, col
from pyspark.sql import SparkSession

source_file = args['S3_INPUT_PATH']
target_path1 = args['S3_TARGET_PATH_1']
target_path2 = args['S3_TARGET_PATH_2']

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

# Explode o DataFrame da equipe (crew)
dfCrew = dfCompleto.select(
    col("id_filme"),
    explode("crew").alias("pessoa_crew")
).select(
    col("id_filme"),
    col("pessoa_crew.adult"),
    col("pessoa_crew.gender"),
    col("pessoa_crew.id").alias("id_crew"),
    col("pessoa_crew.known_for_department"),
    col("pessoa_crew.name"),
    col("pessoa_crew.original_name"),
    col("pessoa_crew.popularity"),
    col("pessoa_crew.credit_id"),
    col("pessoa_crew.department"),
    col("pessoa_crew.job")
)

# Salvar os DataFrames resultantes
dfCast.write.parquet(target_path1)
dfCrew.write.parquet(target_path2)

job.commit()