# System Architecture

## Data Sources

The project uses two source systems:

- CRM
  - Customers
  - Products
  - Sales

- ERP
  - Customer Information
  - Locations
  - Categories

---

## Data Flow

CRM & ERP Data
        │
        ▼
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
Incremental Data Loading

---

## Gold Layer

Dimension Tables

- dim_customer
- dim_product
- dim_date
- dim_geography

Fact Table

- fact_sales