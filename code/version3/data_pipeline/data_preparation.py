# Ensure PySpark is installed: pip install pyspark
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("DataPreparation").getOrCreate()

# Load data
data = spark.read.csv("input_data.csv", header=True, inferSchema=True)

# Data cleansing
data_cleaned = data.dropna()

# Save cleaned data
data_cleaned.write.csv("cleaned_data.csv", header=True)

spark.stop()