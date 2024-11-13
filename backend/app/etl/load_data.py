import pandas as pd
from pyspark.sql import SparkSession

def load_to_databricks(df):
    spark = SparkSession.builder.appName("ChangeETL").getOrCreate()
    spark_df = spark.createDataFrame(df)
    spark_df.write.format("parquet").save("dbfs:/mnt/change_data")
