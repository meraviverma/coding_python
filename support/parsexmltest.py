import spark as spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import  col

# Initialize SparkSession with spark-xml package
builder = SparkSession.builder \
    .appName("Read XML Example") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.17.0")

spark=builder.getOrCreate()

# Path to your XML file
xml_path = r"D:\pythonProject\support\rawxml.xml"

df=spark.read.format("xml")\
    .option("rowTag","Results")\
    .load(xml_path)

result_df=df.select(
    col("embeddedProduct").alias("embeded_Product")
)




# Show the schema and data
result_df.printSchema()
result_df.show(truncate=False)
