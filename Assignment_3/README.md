# Customer Sales Analysis Using Subqueries, CTEs, and Window Functions

## Project Overview

This project focuses on analyzing the Superstore Sales dataset using advanced SQL concepts such as Subqueries, Common Table Expressions (CTEs), Window Functions, and Joins. The dataset was imported into a SQLite database using Python and then analyzed through SQL queries to generate customer and sales insights.

The project demonstrates how SQL can be used to transform raw sales data into meaningful business information. It also provides hands-on experience with data modeling, query optimization, ranking techniques, and analytical reporting.

---

## Objective

The objective of this assignment was to explore advanced SQL concepts and apply them to a real-world sales dataset.

The tasks completed include:

* Importing the Superstore dataset into SQLite using Python.
* Creating normalized tables from raw sales data.
* Applying Subqueries for data filtering and comparisons.
* Using Common Table Expressions (CTEs) for reusable calculations.
* Implementing Window Functions for ranking and row-level analysis.
* Combining JOINs, CTEs, and Window Functions in analytical queries.
* Generating customer sales insights from transactional data.

---

## Tools and Technologies

* Python
* Pandas
* SQLite
* SQL
* SQLAlchemy
* PyCharm

---

## Dataset

Dataset Used: Sample Superstore Dataset

The dataset contains information related to:

* Orders
* Customers
* Products
* Sales
* Profit
* Quantity
* Categories
* Regions
* Order Dates

The dataset consists of thousands of sales transactions and is commonly used for business analytics and SQL practice.

---

## Project Structure

```text
Assignment_3/
│
├── data_import.py
├── queries.sql
├── query results.pdf
├── Sample - Superstore.csv
├── Superstore.db
│
└── README.md
```

---

## Data Import Process

The dataset was imported into SQLite using Python and Pandas.

### Steps Performed

* Loaded the CSV file using Pandas.
* Created a SQLite database connection.
* Imported the dataset into a table named `superstore_raw`.
* Verified successful data insertion.

---

## Database Design

To improve organization and query efficiency, the raw dataset was divided into separate tables.

### Customers Table

Contains:

* Customer ID
* Customer Name
* Segment

### Products Table

Contains:

* Product ID
* Product Name
* Category
* Sub-Category

### Orders Table

Contains:

* Order ID
* Customer ID
* Product ID
* Sales
* Quantity
* Profit
* Region
* Order Date

---

## SQL Concepts Implemented

### Subqueries

Subqueries were used to perform advanced filtering and comparison operations.

Examples:
* Orders with sales greater than average sales.
* Highest sales order for each customer.

---

### Common Table Expressions (CTEs)

CTEs were used to simplify complex calculations and improve query readability.

Examples:
* Calculating total sales for each customer.
* Identifying customers with above-average sales.

---

### Window Functions

Window Functions were used for ranking and analytical operations.

Functions Used:
* RANK()
* ROW_NUMBER()

Applications:

* Ranking customers by total sales.
* Assigning row numbers to orders within customer groups.
* Identifying top-performing customers.

---

### Join Operations

JOIN statements were used to combine information from multiple tables.

Examples:

* Customer sales reports.
* Customer ranking analysis.
* Final sales summary reports.

---

## Business Questions Solved

The project answered the following business questions:

### Top Customers Analysis

Identified the top 5 customers generating the highest revenue.

### Bottom Customers Analysis

Identified the lowest-performing customers based on total sales.

### Single-Order Customers

Found customers who placed only one order.

### Above-Average Customers

Identified customers whose sales exceeded the overall customer average.

### Highest Order Value

Determined the highest-value order placed by each customer.

---

## Key SQL Features Demonstrated

* CREATE TABLE
* SELECT DISTINCT
* GROUP BY
* ORDER BY
* LIMIT
* Aggregate Functions
* Subqueries
* Common Table Expressions (CTEs)
* Window Functions
* RANK()
* ROW_NUMBER()
* JOIN Operations
* Data Normalization

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Working with SQLite databases.
* Loading datasets using Python and Pandas.
* Creating structured database tables.
* Writing advanced SQL queries.
* Using Subqueries and CTEs effectively.
* Applying Window Functions for analytical reporting.
* Performing customer-focused business analysis.
* Generating insights from transactional sales data.

---

## Conclusion

This project demonstrates how advanced SQL techniques can be used to analyze real-world sales data and generate valuable business insights. By combining Subqueries, CTEs, Window Functions, and Joins, customer purchasing behavior and sales performance can be analyzed efficiently.

The assignment strengthened my SQL problem-solving skills and provided hands-on experience with analytical query writing, data modeling, and business intelligence concepts.
