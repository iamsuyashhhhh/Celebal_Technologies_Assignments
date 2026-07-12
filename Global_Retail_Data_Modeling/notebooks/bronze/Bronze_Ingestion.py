# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

BASE_PATH = "/Volumes/workspace/default/retail_data"


# COMMAND ----------

CRM_CUSTOMER_PATH = f"{BASE_PATH}/cust_info.csv"
CRM_PRODUCT_PATH = f"{BASE_PATH}/prd_info.csv"
CRM_SALES_PATH = f"{BASE_PATH}/sales_details.csv"


# COMMAND ----------

ERP_CUSTOMER_PATH = f"{BASE_PATH}/CUST_AZ12.csv"
ERP_LOCATION_PATH = f"{BASE_PATH}/LOC_A101.csv"
ERP_CATEGORY_PATH = f"{BASE_PATH}/PX_CAT_G1V2.csv"

# COMMAND ----------

crm_customer_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(CRM_CUSTOMER_PATH)
)

crm_product_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(CRM_PRODUCT_PATH)
)

crm_sales_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(CRM_SALES_PATH)
)

# COMMAND ----------

erp_customer_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(ERP_CUSTOMER_PATH)
)

erp_location_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(ERP_LOCATION_PATH)
)

erp_category_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(ERP_CATEGORY_PATH)
)

# COMMAND ----------

print("="*60)
print("CRM DATASETS")
print("="*60)

print(f"Customer Records : {crm_customer_df.count():,}")
print(f"Product Records  : {crm_product_df.count():,}")
print(f"Sales Records    : {crm_sales_df.count():,}")

print()

print("="*60)
print("ERP DATASETS")
print("="*60)

print(f"Customer Records : {erp_customer_df.count():,}")
print(f"Location Records : {erp_location_df.count():,}")
print(f"Category Records : {erp_category_df.count():,}")



# COMMAND ----------

display(crm_customer_df)

display(crm_product_df)

display(crm_sales_df)

display(erp_customer_df)

display(erp_location_df)

display(erp_category_df)

# COMMAND ----------

print("="*60)
print("CRM CUSTOMER SCHEMA")
print("="*60)

crm_customer_df.printSchema()

print("="*60)
print("CRM PRODUCT SCHEMA")
print("="*60)

crm_product_df.printSchema()

print("="*60)
print("CRM SALES SCHEMA")
print("="*60)

crm_sales_df.printSchema()

print("="*60)
print("ERP CUSTOMER SCHEMA")
print("="*60)

erp_customer_df.printSchema()

print("="*60)
print("ERP LOCATION SCHEMA")
print("="*60)

erp_location_df.printSchema()

print("="*60)
print("ERP CATEGORY SCHEMA")
print("="*60)

erp_category_df.printSchema()

# COMMAND ----------


spark.sql("CREATE DATABASE IF NOT EXISTS bronze")

# COMMAND ----------

crm_customer_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.crm_customers")

crm_product_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.crm_products")

crm_sales_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.crm_sales")


# COMMAND ----------

erp_customer_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.erp_customers")

erp_location_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.erp_locations")

erp_category_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.erp_categories")

# COMMAND ----------

print("="*60)
print("BRONZE TABLES CREATED SUCCESSFULLY")
print("="*60)

spark.sql("SHOW TABLES IN bronze").show(truncate=False)