from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGO_URI")  # FULL URI, tanpa hardcode

spark = (
    SparkSession.builder
    .appName("SaveToMongo")
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.0")
    .config("spark.mongodb.write.connection.uri", uri)
    .config("spark.mongodb.write.database", "bigdata")
    .config("spark.mongodb.write.collection", "spark_output")
    .getOrCreate()
)

df = spark.createDataFrame([("A", 10), ("B", 20)], ["category", "value"])
df.write.format("mongodb").mode("append").save()
spark.stop()