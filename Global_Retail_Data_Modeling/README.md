# 🏬 Global Retail Data Modeling Platform

![Databricks](https://img.shields.io/badge/Platform-Databricks-red?style=for-the-badge)
![Apache Spark](https://img.shields.io/badge/Engine-Apache%20Spark-orange?style=for-the-badge)
![Delta Lake](https://img.shields.io/badge/Storage-Delta%20Lake-blue?style=for-the-badge)
![PySpark](https://img.shields.io/badge/Language-PySpark-yellow?style=for-the-badge)
![Spark SQL](https://img.shields.io/badge/SQL-SparkSQL-green?style=for-the-badge)

---

# 📖 Project Overview

This project demonstrates the design and implementation of a modern **Retail Data Platform** using **Databricks**, **Apache Spark**, **PySpark**, **Spark SQL**, and **Delta Lake**.

The objective was to transform raw CRM and ERP datasets into a centralized, analytics-ready Data Warehouse following the **Medallion Architecture (Bronze → Silver → Gold)**.

The final platform integrates customer, product, sales, and ERP data into a clean Star Schema that supports business reporting, analytical queries, and scalable data processing.

---

# 🎯 Problem Statement

Retail organizations often receive data from multiple operational systems such as CRM and ERP. These datasets usually contain:

- Duplicate records
- Missing values
- Invalid sales records
- Different date formats
- Inconsistent categorical values
- Fragmented customer information

These issues make business reporting inaccurate and difficult.

This project solves the problem by building a centralized Data Engineering pipeline that cleans, validates, standardizes, and models the data into an analytics-ready warehouse.

---

# 🏗️ Solution Architecture

```

CRM Data ERP Data
│ │
└────────┬────────┘
│
Bronze Layer
(Raw Delta Tables)
│
▼
Silver Layer
(Data Cleaning & Standardization)
│
▼
Gold Layer
(Star Schema)
│
▼
Business Analytics
│
▼
Incremental Data Processing

```

---

# 🏢 Medallion Architecture

The project follows the Medallion Architecture to progressively improve data quality.

## 🥉 Bronze Layer

The Bronze Layer stores raw CRM and ERP datasets exactly as received from the source systems.

### What we did

- Loaded raw CSV files
- Stored data as Delta Tables
- Preserved original source data
- No transformations applied

### Bronze Tables

### CRM

- crm_customers
- crm_products
- crm_sales

### ERP

- erp_customers
- erp_locations
- erp_categories

---

## 🥈 Silver Layer

The Silver Layer cleans, validates, and standardizes the raw data.

### Customer Transformation

Implemented:

- Customer key cleaning
- Gender standardization
- Marital status standardization
- Duplicate removal
- CRM & ERP customer integration

### Product Transformation

Implemented:

- Product data cleaning
- Product cost validation
- Product line standardization
- Duplicate removal

### Sales Transformation

Implemented:

- Sales record validation
- Invalid sales filtering
- Duplicate removal
- Date validation
- Numeric field validation

---

## 🥇 Gold Layer

The Gold Layer contains the final dimensional model for reporting.

### Dimension Tables

- dim_customer
- dim_product
- dim_date
- dim_geography

### Fact Table

- fact_sales

The Gold layer follows a **Star Schema** suitable for BI tools and business reporting.

---

# ⭐ Star Schema

```

dim_customer
│
│
dim_product ─────── fact_sales
│
│
dim_date

                    │

             dim_geography

```

---

# ⚡ Technologies Used

- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Python
- SQL

---

# 📂 Project Structure

```

Global_Retail_Data_Modeling/

├── datasets/
│
├── notebooks/
│ ├── bronze/
│ ├── silver/
│ ├── gold/
│ ├── incremental/
│ └── analytics/
│
├── sql/
│ ├── business_queries.sql
│ ├── data_validation.sql
│ └── star_schema.sql
│
├── docs/
│ ├── architecture.md
│ ├── data_dictionary.md
│ └── project_workflow.md
│
│
└── README.md

```

---

# 📁 Dataset Storage

During development, all datasets were stored inside **Databricks Volumes**.

Example path:

```

/Volumes/workspace/default/retail_data/

```

The Bronze ingestion notebooks directly read data from the Databricks Volume.

For this GitHub repository, the same datasets have been placed inside the **datasets/** folder so the project can be reproduced without requiring access to the original Databricks workspace.

Dataset Folder

```

datasets/

├── cust_info.csv
├── cust_az12.csv
├── loc_a101.csv
├── px_cat_g1v2.csv
├── prd_info.csv
└── sales_details.csv

```

---

# ⚙️ How the Project Works

## Step 1

Raw CRM and ERP datasets are loaded into the Bronze Layer.

↓

## Step 2

The Silver Layer performs data cleaning and validation.

Tasks performed:

- Remove duplicates
- Standardize gender
- Standardize marital status
- Clean customer keys
- Validate dates
- Validate sales
- Merge CRM & ERP customer information

↓

## Step 3

The Gold Layer builds the Star Schema.

Created tables:

- dim_customer
- dim_product
- dim_date
- dim_geography
- fact_sales

↓

## Step 4

Business queries generate analytical reports.

↓

## Step 5

Incremental datasets simulate daily business updates using Delta Lake MERGE.

---

# 🔄 Incremental Data Processing

To simulate real-world business scenarios, the project implements **incremental data loading** using **Delta Lake MERGE**.

Instead of reloading the entire dataset, only newly arrived or modified records are processed.

### Implemented Operations

- Insert new records
- Update existing records
- Avoid duplicate records
- Maintain consistent Delta Tables

This approach improves efficiency and reduces unnecessary processing.

---

# 🗄️ Delta Lake Implementation

Delta Lake is used throughout the project as the storage format for all Bronze, Silver, and Gold tables.

### Benefits

- ACID Transactions
- Reliable Updates
- Incremental MERGE Operations
- Faster Query Performance
- Schema Enforcement
- Scalable Storage
- Better Data Reliability

---

# 🔑 Surrogate Keys

To improve analytical performance, surrogate keys were generated for all dimension tables.

Generated Keys

- customer_sk
- product_sk
- geo_sk
- date_sk

These keys simplify joins between fact and dimension tables while keeping the warehouse design scalable.

---

# 📊 Business Analytics

The Gold Layer enables business users to answer common analytical questions.

### Implemented Reports

- Total Revenue
- Total Orders
- Total Customers
- Total Products
- Average Order Value
- Top Customers
- Top Selling Products
- Revenue by Product Line
- Highest Value Orders
- Quantity Sold

These reports are written using Spark SQL and operate directly on the Gold Layer.

---

# ✅ Data Validation

Data quality checks were performed after the Silver Layer transformations.

Validation includes:

- Duplicate Customer Check
- Duplicate Product Check
- Duplicate Order Check
- Null Customer Validation
- Product Validation
- Invalid Sales Validation

Successful validation queries return **no rows**, indicating that the transformed data satisfies the expected quality rules.

---

# 🚀 Features Implemented

- Medallion Architecture
- CRM & ERP Data Integration
- Apache Spark Processing
- Delta Lake Storage
- Bronze → Silver → Gold Pipeline
- Data Cleaning
- Data Validation
- Standardization of Categorical Values
- Star Schema Modeling
- Surrogate Keys
- Incremental Data Processing
- Business Analytics
- SQL-based Reporting
- Scalable Data Warehouse Design

---

# 📈 Business Insights

The final warehouse enables analysis of:

- Sales Trends
- Customer Behaviour
- Product Performance
- Revenue Analysis
- Country-wise Customer Distribution
- Order Performance
- Business KPIs

---


# 📚 Learning Outcomes

Through this project, the following concepts were implemented and explored:

- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Databricks
- ETL Pipeline Development
- Data Cleaning & Validation
- Data Warehousing
- Star Schema Design
- Medallion Architecture
- Incremental Data Processing
- Business Data Modeling

---

# ▶️ How to Run

1. Upload the datasets to a **Databricks Volume** (recommended) or use the datasets provided in the `datasets/` folder.

2. Execute the notebooks in the following order:

```
bronze/
    bronze_ingestion

↓

silver/
    customer_transformation
    product_transformation
    sales_transformation

↓

gold/
    gold_layer

↓

incremental/
    generate_incremental_data
    incremental_load

↓

analytics/
    business_queries
```

3. Run the SQL validation scripts located in the `sql/` directory.

4. Execute the business analytics notebook to generate reports.

---

# 🤝 Repository Contents

```
datasets/
│
├── CRM & ERP source datasets

notebooks/
│
├── Bronze Layer
├── Silver Layer
├── Gold Layer
├── Incremental Loading
└── Analytics
sql/
│
├── Business Queries
├── Data Validation
├── Star Schema
docs/
│
├── Architecture
├── Data Dictionary
└── Project Workflow

README.md
```

---

# 👨‍ Author

**Suyash Saxena**

B.Tech Computer Engineering

Poornima University

---