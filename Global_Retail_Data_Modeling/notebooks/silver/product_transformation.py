# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

crm_product_df = spark.table("bronze.crm_products")

# COMMAND ----------

display(crm_product_df.limit(10))

# COMMAND ----------

product_df = (
    crm_product_df
    .withColumnRenamed("prd_id", "product_id")
    .withColumnRenamed("prd_key", "product_key")
    .withColumnRenamed("prd_nm", "product_name")
    .withColumnRenamed("prd_cost", "product_cost")
    .withColumnRenamed("prd_line", "product_line")
    .withColumnRenamed("prd_start_dt", "start_date")
    .withColumnRenamed("prd_end_dt", "end_date")
)

# COMMAND ----------

product_df = (
    product_df
    .withColumn(
        "product_name",
        initcap(trim(col("product_name")))
    )
)

# COMMAND ----------

product_df = (
    product_df
    .withColumn(
        "product_line",
        when(col("product_line") == "M", "Mountain")
        .when(col("product_line") == "R", "Road")
        .when(col("product_line") == "S", "Other Sales")
        .when(col("product_line") == "T", "Touring")
        .otherwise("Unknown")
    )
)

# COMMAND ----------

product_df = (
    product_df
    .withColumn(
        "product_cost",
        col("product_cost").cast("double")
    )
)

# COMMAND ----------

product_df = (
    product_df
    .withColumn(
        "start_date",
        to_date(col("start_date"))
    )

    .withColumn(
        "end_date",
        to_date(col("end_date"))
    )
)

# COMMAND ----------

product_df = product_df.dropDuplicates(["product_id"])

# COMMAND ----------

product_df = product_df.orderBy("product_id")

# COMMAND ----------

print("PRODUCT TRANSFORMATION SUMMARY")
print(f"Total Products : {product_df.count():,}")
print(f"Total Columns  : {len(product_df.columns)}")

print("\nSchema")

product_df.printSchema()

# COMMAND ----------

display(product_df.limit(10))

# COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS silver")

# COMMAND ----------


product_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("silver.products")

# COMMAND ----------

spark.sql("SHOW TABLES IN silver").show()
display(spark.table("silver.products"))