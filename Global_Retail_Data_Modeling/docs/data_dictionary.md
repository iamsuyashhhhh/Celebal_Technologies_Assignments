# Data Dictionary

## gold.dim_customer

| Column | Description |
|---------|-------------|
| customer_sk | Surrogate Key |
| customer_id | Customer ID |
| customer_key | CRM Customer Key |
| first_name | Customer First Name |
| last_name | Customer Last Name |
| gender | Standardized Gender |
| marital_status | Standardized Marital Status |
| country | Customer Country |

---

## gold.dim_product

| Column | Description |
|---------|-------------|
| product_sk | Surrogate Key |
| product_id | Product ID |
| product_key | Product Key |
| product_name | Product Name |
| category | Product Category |
| cost | Product Cost |

---

## gold.dim_date

| Column | Description |
|---------|-------------|
| date_sk | Date Key |
| full_date | Calendar Date |
| month | Month |
| quarter | Quarter |
| year | Year |

---

## gold.dim_geography

| Column | Description |
|---------|-------------|
| geo_sk | Geography Key |
| customer_key | Customer Key |
| country | Customer Country |

---

## gold.fact_sales

| Column | Description |
|---------|-------------|
| order_number | Sales Order |
| customer_sk | Customer Foreign Key |
| product_sk | Product Foreign Key |
| sales_amount | Revenue |
| quantity | Quantity Sold |
| price | Unit Price |