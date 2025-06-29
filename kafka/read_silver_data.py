from pyspark.sql import SparkSession
builder = SparkSession.builder \
    .appName("DeltaTableInPyCharm") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = builder.getOrCreate()

# Path to your Silver Delta table
silver_path = "file:///D:/StorageAccount/silver/kafka_json"
bronze_path = "file:///D:/StorageAccount/bronze/kafka_json"

# Read the Raw Data
bronze_df = spark.read.format("delta").load(bronze_path)
# Display the data
bronze_df.show(truncate=False)

# Read the Delta table
silver_df = spark.read.format("delta").load(silver_path)

# Display the data
silver_df.show(truncate=False)