# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# COMMAND ----------

customer_df = spark.table("silver.customers")
product_df = spark.table("silver.products")
sales_df = spark.table("silver.sales")

# COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS gold")

# COMMAND ----------

window_customer = Window.orderBy("customer_id")

dim_customer = (

    customer_df

    .withColumn(
        "customer_sk",
        row_number().over(window_customer)
    )

)

# COMMAND ----------

window_product = Window.orderBy("product_id")

dim_product = (

    product_df

    .withColumn(
        "product_sk",
        row_number().over(window_product)
    )

)


# COMMAND ----------

dim_customer.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold.dim_customer")

dim_product.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold.dim_product")

# COMMAND ----------

dim_customer = spark.table("gold.dim_customer")
dim_product = spark.table("gold.dim_product")

# COMMAND ----------

geo_df = spark.table("bronze.erp_locations")

# COMMAND ----------

geo_df = (
    geo_df
    .withColumnRenamed("CID", "customer_key")
    .withColumnRenamed("CNTRY", "country")
)

# COMMAND ----------

geo_df = geo_df.dropDuplicates(["customer_key"])

# COMMAND ----------

window_spec = Window.orderBy("customer_key")

geo_df = geo_df.withColumn(
    "geo_sk",
    row_number().over(window_spec)
)


# COMMAND ----------

geo_df = geo_df.select(
    "geo_sk",
    "customer_key",
    "country"
)


# COMMAND ----------

geo_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold.dim_geography")

print("Geography Dimension Created Successfully")

display(spark.table("gold.dim_geography"))

# COMMAND ----------

sales_df = spark.table("silver.sales")

# COMMAND ----------

date_df = sales_df.select("order_date").distinct()

# COMMAND ----------

date_df = (
    sales_df
    .filter(
        (col("order_date") >= 19000101) &
        (col("order_date") <= 21001231)
    )
    .select("order_date")
    .distinct()
)

# COMMAND ----------

date_df = (
    date_df
    .withColumn(
        "full_date",
        to_date(col("order_date").cast("string"), "yyyyMMdd")
    )
)


# COMMAND ----------

date_df = (
    date_df
    .withColumn("date_sk", col("order_date"))
    .withColumn("day", dayofmonth("full_date"))
    .withColumn("month", month("full_date"))
    .withColumn("month_name", date_format("full_date", "MMMM"))
    .withColumn("quarter", quarter("full_date"))
    .withColumn("year", year("full_date"))
    .withColumn("week", weekofyear("full_date"))
    .withColumn("day_name", date_format("full_date", "EEEE"))
    .withColumn(
        "is_weekend",
        when(dayofweek("full_date").isin(1, 7), True).otherwise(False)
    )
)



# COMMAND ----------

date_df = date_df.select(
    "date_sk",
    "full_date",
    "day",
    "month",
    "month_name",
    "quarter",
    "year",
    "week",
    "day_name",
    "is_weekend"
)


# COMMAND ----------

date_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold.dim_date")

display(spark.table("gold.dim_date"))

# COMMAND ----------

fact_sales = (

    sales_df.alias("s")

    .join(
        dim_customer.alias("c"),
        col("s.customer_id") == col("c.customer_id"),
        "left"
    )

    .join(
        dim_product.alias("p"),
        col("s.product_key") == col("p.product_key"),
        "left"
    )

    .select(

        col("order_number"),

        col("customer_sk"),

        col("product_sk"),

        col("order_date"),

        col("ship_date"),

        col("due_date"),

        col("quantity"),

        col("price"),

        col("sales_amount")

    )

)

# COMMAND ----------

fact_sales.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable("gold.fact_sales")

# COMMAND ----------

print("="*70)
print("Gold Tables Created Successfully")
print("="*70)

spark.sql("SHOW TABLES IN gold").show()

display(spark.table("gold.dim_customer"))
display(spark.table("gold.dim_product"))
display(spark.table("gold.dim_date"))
display(spark.table("gold.dim_geography"))
display(spark.table("gold.fact_sales"))

# COMMAND ----------

