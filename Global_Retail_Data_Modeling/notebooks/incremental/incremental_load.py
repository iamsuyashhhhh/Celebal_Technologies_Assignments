# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

incremental_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Volumes/workspace/default/retail_data/sales_incremental.csv")
)

# COMMAND ----------

incremental_df = (
    incremental_df
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

display(incremental_df)

incremental_df.createOrReplaceTempView("incremental_sales")

# COMMAND ----------

spark.sql("""
MERGE INTO silver.sales AS target
USING incremental_sales AS source
ON target.order_number = source.order_number

WHEN MATCHED THEN
UPDATE SET
    target.product_key = source.product_key,
    target.customer_id = source.customer_id,
    target.order_date = source.order_date,
    target.ship_date = source.ship_date,
    target.due_date = source.due_date,
    target.sales_amount = source.sales_amount,
    target.quantity = source.quantity,
    target.price = source.price

WHEN NOT MATCHED THEN
INSERT (
    order_number,
    product_key,
    customer_id,
    order_date,
    ship_date,
    due_date,
    sales_amount,
    quantity,
    price
)
VALUES (
    source.order_number,
    source.product_key,
    source.customer_id,
    source.order_date,
    source.ship_date,
    source.due_date,
    source.sales_amount,
    source.quantity,
    source.price
)
""")

# COMMAND ----------
# Validation

print("="*70)
print("Incremental Load Completed Successfully")
print("="*70)

print("Total Records After MERGE :",
      spark.table("silver.sales").count())

# COMMAND ----------

display(
    spark.sql("""
    SELECT *
    FROM silver.sales
    WHERE order_number IN (
        'SO999901',
        'SO999902',
        'SO999903',
        'SO999904'
    )
    ORDER BY order_number
    """)
)

# COMMAND ----------

display(spark.table("silver.sales"))