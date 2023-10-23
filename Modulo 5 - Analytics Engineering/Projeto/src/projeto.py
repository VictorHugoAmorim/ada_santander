from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()
my_df = spark.read.format("csv").option("inferSchema","true").option("sep",",").option("header","true").load("dbfs:/FileStore/listings.csv")