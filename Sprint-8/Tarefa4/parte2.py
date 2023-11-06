# 1
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, rand, when, expr

spark = SparkSession.builder \
	.master("local[*]") \
	.appName("Exercicio Intro") \
	.getOrCreate()

txt = "nomes_aleatorios.txt"

df_nomes = spark.read.text(txt)
df_nomes.show(5)

# 2
df_nomes = df_nomes.withColumnRenamed("value", "Nomes")
df_nomes.show(10)

# 3
df_nomes = df_nomes.withColumn("Escolaridade", 
    when(expr("rand() <= 0.33"), "Fundamental")
    .when(expr("rand() <= 0.66"), "Médio")
    .otherwise("Superior")
)

# 4
paises = ["Brasil", "Argentina", "Chile", "Colômbia", "Peru", "Venezuela", "Equador", "Bolívia", "Paraguai", "Uruguai", "Suriname", "Guiana", "Guiana Francesa"]
df_nomes = df_nomes.withColumn("Indice_Pais", (rand() * 13).cast("int"))
df_nomes = df_nomes.withColumn("Pais", lit(paises).getItem(col("Indice_Pais")))
df_nomes = df_nomes.drop("Indice_Pais")

# 5
df_nomes = df_nomes.withColumn("AnoNascimento", 
    expr("CAST(FLOOR(1945 + (2010 - 1945) * rand()) AS INT)")
)
df_nomes.show(10)

# 6
df_select = df_nomes.select("*").filter(col("AnoNascimento") > 2000)
df_select.show(10)

# 7
df_nomes.createOrReplaceTempView("pessoas")
query = "SELECT * FROM pessoas WHERE AnoNascimento > 2000"
df_select = spark.sql(query)
df_select.show(10)

# 8
millennials = df_nomes.select("*").filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()

# 9
queryMillennials = "SELECT COUNT(*) AS CountMillennials FROM pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994"
millennials = spark.sql(queryMillennials)
millennials.show()

# 10
queryBoomers = """
SELECT Pais, 'Baby Boomers' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1944 AND AnoNascimento <= 1964
GROUP BY Pais
"""


queryGenX = """
SELECT Pais, 'Geracao X' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1965 AND AnoNascimento <= 1979
GROUP BY Pais
"""

queryMillennials2 = """
SELECT Pais, 'Millennials' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
GROUP BY Pais
"""

queryGenZ = """
SELECT Pais, 'Geracao Z' AS Geracao, COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento >= 1995 AND AnoNascimento <= 2015
GROUP BY Pais
"""

dfResultado = spark.sql(queryBoomers).union(spark.sql(queryGenX)).union(spark.sql(queryMillennials2)).union(spark.sql(queryGenZ))
dfResultado = dfResultado.orderBy("Pais", "Geracao", "Quantidade")
totLinhas = dfResultado.count()
dfResultado.show(totLinhas)