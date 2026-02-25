from pyspark.sql import SparkSession

# membuat Spark session
spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate()

# data contoh
data = [("A", 10), ("B", 20), ("A", 30)]
columns = ["category", "value"]

# buat dataframe
df = spark.createDataFrame(data, columns)

# agregasi data
df.groupBy("category").sum("value").show()

spark.stop()