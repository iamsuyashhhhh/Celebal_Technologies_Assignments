# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT SUM(sales_amount) AS total_revenue FROM gold.fact_sales;


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_orders FROM gold.fact_sales;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_customers FROM gold.dim_customer;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     c.first_name,c.last_name,SUM(f.sales_amount) AS revenue
# MAGIC FROM gold.fact_sales f
# MAGIC JOIN gold.dim_customer c ON f.customer_sk = c.customer_sk
# MAGIC GROUP BY c.first_name,c.last_name
# MAGIC ORDER BY revenue DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     p.product_name,SUM(f.quantity) AS total_quantity
# MAGIC FROM gold.fact_sales f
# MAGIC JOIN gold.dim_product p ON f.product_sk = p.product_sk
# MAGIC GROUP BY p.product_name
# MAGIC ORDER BY total_quantity DESC;