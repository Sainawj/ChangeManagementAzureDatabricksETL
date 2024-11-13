from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, col

def run_etl():
    spark = SparkSession.builder.appName("ETL_Pipeline_Job").getOrCreate()

    # Step 1: Load data from MySQL
    jdbc_url = "jdbc:mysql://your-mysql-server:3306/yourdatabase"
    jdbc_properties = {
        "user": "etluser",
        "password": "angukanayo24",
        "driver": "com.mysql.jdbc.Driver"
    }

    df = spark.read.jdbc(url=jdbc_url, table="change_records", properties=jdbc_properties)
    
    # Step 2: Clean and Transform Data
    df_cleaned = df.na.drop(subset=["change_id", "description"])
    df_cleaned = df_cleaned.withColumn("status", upper(col("status")))

    # Step 3: Save Data as Parquet
    df_cleaned.write.format("parquet").save("/mnt/cleaned_data/change_records")

if __name__ == "__main__":
    run_etl()
