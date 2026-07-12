# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT SUM(sales_amount) AS Total_Revenue FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT SUM(sales_amount) AS Total_Revenue FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS Customers FROM gold.dim_customer;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS Products FROM gold.dim_product;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT ROUND(AVG(sales_amount),2) FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT customer_sk, SUM(sales_amount) Revenue
# MAGIC FROM gold.fact_sales
# MAGIC GROUP BY customer_sk
# MAGIC ORDER BY Revenue DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT product_sk,
# MAGIC SUM(sales_amount) Revenue
# MAGIC FROM gold.fact_sales
# MAGIC GROUP BY product_sk
# MAGIC ORDER BY Revenue DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT p.product_line, SUM(f.sales_amount) Revenue
# MAGIC FROM gold.fact_sales f
# MAGIC JOIN gold.dim_product p ON f.product_sk=p.product_sk
# MAGIC GROUP BY p.product_line
# MAGIC ORDER BY Revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gold.fact_sales ORDER BY sales_amount DESC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT SUM(quantity) FROM gold.fact_sales;