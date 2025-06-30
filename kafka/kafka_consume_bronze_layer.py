from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, date_format, current_timestamp

spark = SparkSession.builder \
    .appName("KafkaToBronzeDelta") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

#Read from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test-topic") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON
raw_df = kafka_df.selectExpr("CAST(value AS STRING) as raw_value") \
    .withColumn("event_time", date_format(current_timestamp(), "yyyy-MM-dd HH:mm:ss"))



bronze_path = "file:///D:/StorageAccount/bronze/kafka_json"
checkpoint_location="file:///D:/StorageAccount/bronze/checkpoints/kafka_json"

query = raw_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", checkpoint_location) \
    .start(bronze_path)

query.awaitTermination()