import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv,['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

from pyspark.sql.functions import *

data = spark.read.format("csv").option("header", "true").load(source_file)
data.show()
data = data.withColumn("nome", upper(col("nome"))).sort(col("ano").desc())
data.count()

data.createOrReplaceTempView("tabela")
#spark.sql("SELECT ano, sexo, SUM(total) AS total_nomes FROM tabela GROUP BY ano, sexo ORDER BY ano DESC").show()
spark.sql("SELECT nome, ano, MAX(total) AS totRegistros FROM tabela WHERE sexo = 'F' GROUP BY nome, ano ORDER BY totRegistros DESC LIMIT 1").show()
spark.sql("SELECT nome, ano, MAX(total) AS totRegistros FROM tabela WHERE sexo = 'M' GROUP BY nome, ano ORDER BY totRegistros DESC LIMIT 1").show()
spark.sql("SELECT ano, sexo, SUM(total) AS totRegistros FROM tabela GROUP BY ano, sexo ORDER BY ano asc LIMIT 10").show()
data.write.partitionBy("sexo", "ano").json(target_path)

job.commit()