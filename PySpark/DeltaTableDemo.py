from pyspark.sql import SparkSession

builder = SparkSession.builder \
    .appName("DeltaTableInPyCharm") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = builder.getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Save as Delta table
df.write.format("delta").mode("overwrite").save("delta-table")

# Read it back
delta_df = spark.read.format("delta").load("delta-table")
delta_df.show()