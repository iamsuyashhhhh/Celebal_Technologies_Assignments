# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT
# MAGIC SUM(sales_amount) AS Total_Revenue
# MAGIC FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC SUM(sales_amount) AS Total_Revenue
# MAGIC FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC COUNT(*) AS Customers
# MAGIC FROM gold.dim_customer;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC COUNT(*) AS Products
# MAGIC FROM gold.dim_product;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC ROUND(AVG(sales_amount),2)
# MAGIC FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC customer_sk,
# MAGIC SUM(sales_amount) Revenue
# MAGIC FROM gold.fact_sales
# MAGIC GROUP BY customer_sk
# MAGIC ORDER BY Revenue DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC product_sk,
# MAGIC SUM(sales_amount) Revenue
# MAGIC FROM gold.fact_sales
# MAGIC GROUP BY product_sk
# MAGIC ORDER BY Revenue DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC p.product_line,
# MAGIC
# MAGIC SUM(f.sales_amount) Revenue
# MAGIC
# MAGIC FROM gold.fact_sales f
# MAGIC
# MAGIC JOIN gold.dim_product p
# MAGIC
# MAGIC ON f.product_sk=p.product_sk
# MAGIC
# MAGIC GROUP BY p.product_line
# MAGIC
# MAGIC ORDER BY Revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC
# MAGIC FROM gold.fact_sales
# MAGIC
# MAGIC ORDER BY sales_amount DESC
# MAGIC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC SUM(quantity)
# MAGIC
# MAGIC FROM gold.fact_sales;