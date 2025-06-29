from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("KafkaToBronzeDelta") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Define schema for parsing
json_schema = StructType() \
    .add("id", IntegerType()) \
    .add("name", StringType()) \
    .add("role", StringType()) \
    .add("project", StringType())

# Read raw data from Bronze
bronze_path = "file:///D:/StorageAccount/bronze/kafka_json"

bronze_df = spark.readStream \
    .format("delta") \
    .load(bronze_path)

# Parse the raw JSON
parsed_df = bronze_df.select(
    col("event_time"),
    from_json(col("raw_value"), json_schema).alias("data")
).select("event_time", "data.*")

silver_path = "file:///D:/StorageAccount/silver/kafka_json"
checkpointLocation_silver="file:///D:/StorageAccount/silver/checkpoints/kafka_json"

query = parsed_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", checkpointLocation_silver) \
    .start(silver_path)

query.awaitTermination()