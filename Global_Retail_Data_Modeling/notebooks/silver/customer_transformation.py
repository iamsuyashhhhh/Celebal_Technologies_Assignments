# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

crm_customer_df = spark.table("bronze.crm_customers")

erp_customer_df = spark.table("bronze.erp_customers")

erp_location_df = spark.table("bronze.erp_locations")

# COMMAND ----------

display(crm_customer_df.limit(5))

display(erp_customer_df.limit(5))

display(erp_location_df.limit(5))

# COMMAND ----------

crm_customer = (

    crm_customer_df

    .withColumnRenamed("cst_id","customer_id")

    .withColumnRenamed("cst_key","customer_key")

    .withColumnRenamed("cst_firstname","first_name")

    .withColumnRenamed("cst_lastname","last_name")

    .withColumnRenamed("cst_marital_status","marital_status")

    .withColumnRenamed("cst_gndr","gender")

    .withColumnRenamed("cst_create_date","create_date")

)

# COMMAND ----------

crm_customer = (

    crm_customer

    .withColumn("first_name",initcap(trim(col("first_name"))))

    .withColumn("last_name",initcap(trim(col("last_name"))))

)

# COMMAND ----------

crm_customer = (

    crm_customer

    .withColumn(

        "gender",

        when(upper(col("gender"))=="M","Male")

        .when(upper(col("gender"))=="F","Female")

        .otherwise("Unknown")

    )

)

# COMMAND ----------

crm_customer = (

    crm_customer

    .withColumn(

        "marital_status",

        when(upper(col("marital_status"))=="M","Married")

        .when(upper(col("marital_status"))=="S","Single")

        .otherwise("Unknown")

    )

)

# COMMAND ----------

crm_customer = (

    crm_customer

    .withColumn(

        "create_date",

        to_date(col("create_date"))

    )

)

# COMMAND ----------


erp_customer = (

    erp_customer_df

    .withColumnRenamed("CID","customer_key")

    .withColumnRenamed("BDATE","birth_date")

    .withColumnRenamed("GEN","erp_gender")

)

# COMMAND ----------

erp_customer = (

    erp_customer

    .withColumn(

        "customer_key",

        regexp_replace(

            col("customer_key"),

            "^NAS",

            ""

        )

    )

)

# COMMAND ----------

erp_customer = (

    erp_customer

    .withColumn(

        "erp_gender",

        initcap(trim(col("erp_gender")))

    )

)

# COMMAND ----------

erp_customer = (

    erp_customer

    .withColumn(

        "birth_date",

        to_date(col("birth_date"))

    )

)

# COMMAND ----------

erp_location = (

    erp_location_df

    .withColumnRenamed("CID","customer_key")

    .withColumnRenamed("CNTRY","country")

)

# COMMAND ----------

erp_location = (

    erp_location

    .withColumn(

        "customer_key",

        regexp_replace(

            col("customer_key"),

            "-",

            ""

        )

    )

)

# COMMAND ----------

customer_df = (

    crm_customer.alias("crm")

    .join(

        erp_customer.alias("erp"),

        "customer_key",

        "left"

    )

)

# COMMAND ----------

customer_df = (

    customer_df.alias("cust")

    .join(

        erp_location.alias("loc"),

        "customer_key",

        "left"

    )

)

# COMMAND ----------

customer_df = (

    customer_df

    .withColumn(

        "gender",

        coalesce(

            col("gender"),

            col("erp_gender")

        )

    )

)

# COMMAND ----------

customer_df = (

    customer_df

    .dropDuplicates(

        ["customer_id"]

    )

)

# COMMAND ----------

customer_df = customer_df.select(

    "customer_id",

    "customer_key",

    "first_name",

    "last_name",

    "birth_date",

    "gender",

    "marital_status",

    "country",

    "create_date"

)

# COMMAND ----------

print("="*70)

print("CUSTOMER TABLE SUMMARY")

print("="*70)

print("Rows :",customer_df.count())

print("Columns :",len(customer_df.columns))

display(customer_df.limit(10))

# COMMAND ----------

# COMMAND ----------

spark.sql(

    "CREATE DATABASE IF NOT EXISTS silver"

)

# COMMAND ----------

spark.sql(

    "CREATE DATABASE IF NOT EXISTS silver"

)

# COMMAND ----------

(

customer_df.write

.format("delta")

.mode("overwrite")

.saveAsTable(

"silver.customers"

)

)

# COMMAND ----------

spark.sql(

"SHOW TABLES IN silver"

).show()

display(

spark.table(

"silver.customers"

)

)