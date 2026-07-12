# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT customer_id, COUNT(*) FROM silver.customers
# MAGIC GROUP BY customer_id
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT product_id, COUNT(*) FROM silver.products
# MAGIC GROUP BY product_id
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT order_number, COUNT(*) FROM silver.sales
# MAGIC GROUP BY order_number
# MAGIC HAVING COUNT(*) > 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver.sales WHERE customer_id IS NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver.sales WHERE sales_amount < 0;