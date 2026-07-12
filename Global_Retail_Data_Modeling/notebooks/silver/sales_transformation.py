# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

sales_df = spark.table("bronze.crm_sales")

# COMMAND ----------

sales_df = (
    sales_df
    .withColumnRenamed("sls_ord_num", "order_number")
    .withColumnRenamed("sls_prd_key", "product_key")
    .withColumnRenamed("sls_cust_id", "customer_id")
    .withColumnRenamed("sls_order_dt", "order_date")
    .withColumnRenamed("sls_ship_dt", "ship_date")
    .withColumnRenamed("sls_due_dt", "due_date")
    .withColumnRenamed("sls_sales", "sales_amount")
    .withColumnRenamed("sls_quantity", "quantity")
    .withColumnRenamed("sls_price", "price")
)

# COMMAND ----------

sales_df = (
    sales_df
    .withColumn("sales_amount", col("sales_amount").cast("double"))
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("price", col("price").cast("double"))
)

# COMMAND ----------

sales_df = sales_df.dropDuplicates()

# COMMAND ----------

sales_df = sales_df.filter(
    (col("customer_id").isNotNull()) &
    (col("product_key").isNotNull()) &
    (col("quantity") > 0) &
    (col("price") >= 0)
)


# COMMAND ----------

print("Rows:", sales_df.count())
print("Columns:", len(sales_df.columns))

display(sales_df.limit(20))

# COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS silver")

# COMMAND ----------

sales_df.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("silver.sales")

# COMMAND ----------

display(spark.table("silver.sales"))