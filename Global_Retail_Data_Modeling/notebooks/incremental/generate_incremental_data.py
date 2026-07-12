# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

existing_orders = (
    spark.table("silver.sales")
    .select("order_number", "product_key", "customer_id")
    .limit(2)
    .collect()
)

# COMMAND ----------

incremental_data = [

    (
        existing_orders[0]["order_number"],
        existing_orders[0]["product_key"],
        existing_orders[0]["customer_id"],
        20140101,
        20140103,
        20140106,
        5000,
        2,
        2500
    ),

    (
        existing_orders[1]["order_number"],
        existing_orders[1]["product_key"],
        existing_orders[1]["customer_id"],
        20140102,
        20140104,
        20140107,
        4200,
        3,
        1400
    ),

    (
        "SO999901",
        "BK-R93R-44",
        25001,
        20140102,
        20140104,
        20140107,
        3200,
        2,
        1600
    ),

    (
        "SO999902",
        "BK-R93R-48",
        25002,
        20140105,
        20140107,
        20140110,
        1800,
        1,
        1800
    ),

    (
        "SO999903",
        "BK-M82S-44",
        25003,
        20140106,
        20140108,
        20140111,
        4100,
        2,
        2050
    ),

    (
        "SO999904",
        "BK-R50R-52",
        25004,
        20140108,
        20140110,
        20140113,
        2800,
        1,
        2800
    )

]


# COMMAND ----------

columns = [

    "sls_ord_num",
    "sls_prd_key",
    "sls_cust_id",
    "sls_order_dt",
    "sls_ship_dt",
    "sls_due_dt",
    "sls_sales",
    "sls_quantity",
    "sls_price"

]

# COMMAND ----------

incremental_df = spark.createDataFrame(incremental_data,columns)

# COMMAND ----------

display(incremental_df)


# COMMAND ----------

incremental_df.write \
.mode("overwrite") \
.option("header", True) \
.csv("/Volumes/workspace/default/retail_data/sales_incremental.csv")


# COMMAND ----------


print("Incremental Dataset Generated Successfully")
print(f"Total Records : {incremental_df.count()}")
display(incremental_df)