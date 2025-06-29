from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("SampleDF").getOrCreate()

# Sample data and column names
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)

# Show the DataFrame
df.show()