# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT customer_id, COUNT(*)
# MAGIC FROM silver.customers
# MAGIC GROUP BY customer_id
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT product_id, COUNT(*)
# MAGIC FROM silver.products
# MAGIC GROUP BY product_id
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT order_number, COUNT(*)
# MAGIC FROM silver.sales
# MAGIC GROUP BY order_number
# MAGIC HAVING COUNT(*) > 1;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver.sales
# MAGIC WHERE customer_id IS NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver.sales
# MAGIC WHERE sales_amount < 0;