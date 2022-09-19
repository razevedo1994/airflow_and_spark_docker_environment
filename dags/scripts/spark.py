from pyspark.sql import SparkSession


def spark_function():
    spark = SparkSession.builder.appName("spark_session").getOrCreate()
    df = spark.createDataFrame([("Scala", 25000), ("Spark", 35000), ("PHP", 21000)])

    df.show()
    # df.write.mode("overwrite").csv("/opt/spark-apps/saida123")

    spark.stop()


if __name__ == "__main__":
    spark_function()
