from pyspark.sql import SparkSession

builder = SparkSession.builder \
    .appName("DeltaTableInPyCharm") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = builder.getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

#airfare_df=spark.read.option("header",True).csv("D:\\pythonProject\PySpark\\airfaredata_day1.csv")
#airfare_df.show()


#airfare_df.write.format("delta").save("D:\\pythonProject\PySpark\\new-delta-table\\airfare")


delta_read_df = spark.read.format("delta").load("D:\\pythonProject\PySpark\\new-delta-table\\airfare")
delta_read_df.show()


