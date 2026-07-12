# Assignment 8 : E-Commerce Order Analytics System

## About the Project

This project is an end-to-end **E-Commerce Order Analytics System** developed using **Python, Pandas, SQLite, and SQL**.

The main objective of this project is to understand the complete data analytics workflow. Starting from generating raw data, cleaning it, storing it in a database, performing SQL analysis, and finally generating reports using a Python Command Line Interface.

While building this project, I tried to simulate a real e-commerce system by creating realistic datasets and introducing common data quality issues like duplicate records, invalid emails, missing values, and incorrect dates.

---

# Technologies Used

- Python
- Pandas
- Faker
- SQLite
- SQL
- Git & GitHub

## Development Tools

- PyCharm Community Edition
- DB Browser for SQLite

I used **DB Browser for SQLite** to execute all SQL queries and verify the output of each query.

---

# Project Structure

```
E-Commerce-Analytics-System
│
├── data
│   ├── raw
│   └── cleaned
│
├── scripts
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_database.py
│   └── report_cli.py
│
├── sql
│   ├── schema.sql
│   ├── aggregations.sql
│   ├── window_functions.sql
│   └── cohort_analysis.sql
│
├── output
│   └── sample_reports
│
├── ecommerce.db
│
└── README.md
```

---

# Features

### Dataset Generation

The project generates four datasets:

- Customers
- Products
- Orders
- Order Items

To make the project more realistic, I intentionally introduced some common data issues like:

- Duplicate records
- Invalid email addresses
- Missing customer IDs
- Invalid dates

All datasets are exported as CSV files.

---

### Data Cleaning

The generated datasets are cleaned using **Pandas**.

The cleaning process includes:

- Removing duplicate records
- Handling missing customer IDs
- Converting date columns
- Normalizing product names
- Validating customer email addresses
- Checking referential integrity
- Creating an issues report

After cleaning, all datasets are saved again as cleaned CSV files.

---

# Database

After cleaning the data, it is loaded into a **SQLite database**.

The database contains four tables:

- customers
- products
- orders
- order_items

The database schema includes:

- Primary Keys
- Foreign Keys
- NOT NULL Constraints

---

# SQL Analysis

The SQL part of this project is divided into three files.

### aggregations.sql

This file contains queries related to:

- Revenue by category
- Top customers
- Monthly order count
- Return analysis
- Average Order Value

### window_functions.sql

This file demonstrates:

- Running Total
- DENSE_RANK()
- LAG()
- NTILE()
- Year-over-Year Comparison
- Customer Segmentation
- Revenue Distribution

### cohort_analysis.sql

This file contains:

- Customer Cohort Analysis
- Products Frequently Bought Together

---

# Command Line Reporting Tool

A simple CLI application is created using Python.

The user can enter:

- Report Type (Daily / Weekly / Monthly)
- Start Date
- End Date

The report displays:

- Total Orders
- Total Revenue
- Unique Customers
- Top 3 Products

The application also validates user inputs and handles invalid cases gracefully.

---

# Edge Cases Handled

While developing the project, I handled a few common edge cases such as:

- Invalid report type
- Invalid date format
- Start date greater than end date
- Empty result set
- Database connection errors
- Invalid email addresses
- Invalid order references

---

# How to Run the Project

### Step 1

Generate the datasets.

```bash
python scripts/generate_data.py
```

### Step 2

Clean the generated datasets.

```bash
python scripts/clean_data.py
```

### Step 3

Load the cleaned data into SQLite.

```bash
python scripts/load_database.py
```

### Step 4

Open **DB Browser for SQLite**.

Open the `ecommerce.db` database.

Go to **Execute SQL** and execute the following files:

- aggregations.sql
- window_functions.sql
- cohort_analysis.sql

### Step 5

Run the reporting tool.

```bash
python scripts/report_cli.py
```

Enter:

- Report Type
- Start Date
- End Date

The report will be generated based on the selected date range.

---

# Sample Outputs

Screenshots of the generated reports and SQL query outputs are available inside:

```
output/sample_reports
```

The folder contains:

- Daily Report
- Weekly Report
- Monthly Report
- SQL Query Outputs
- Cohort Analysis
- Customer Ranking
- Running Total
- Revenue Analysis

---

# What I Learned

This project helped me understand:

- Data generation using Python
- Data cleaning using Pandas
- SQLite database creation
- Writing SQL queries
- Window Functions
- Common Table Expressions (CTEs)
- Cohort Analysis
- Customer Segmentation
- Building a simple CLI application
- Handling different edge cases

---

# Future Improvements

Some improvements that can be added later are:

- Interactive dashboard using Streamlit
- Data visualization
- Export reports as PDF or Excel
- Cloud database integration
- Scheduled report generation

---

# Project Summary

This project was completed as part of an assignment to understand and implement an end-to-end e-commerce order analytics system using Python and SQL. The objective was to follow the given requirements and build a complete workflow starting from dataset generation to business reporting.

The project begins with generating realistic e-commerce datasets for customers, products, orders, and order items using the **Faker** library and Python's **random** module, as specified in the assignment. The generated data also includes intentional inconsistencies such as duplicate records, invalid email addresses, missing customer IDs, and invalid dates to simulate common real-world data quality issues.

The generated datasets were then cleaned using **Pandas**. During this stage, duplicate records were removed, missing customer IDs were handled, product names were standardized, date formats were validated, invalid email addresses were identified, and referential integrity between the Orders and Order Items tables was verified. An issues report was also generated to summarize the data quality checks performed.

After cleaning the datasets, the cleaned CSV files were loaded into a **SQLite** database. A database schema was created using Primary Keys, Foreign Keys, and appropriate constraints to maintain data integrity. The inserted data was verified before performing further analysis.

The SQL portion of the project was divided into multiple sections based on the assignment requirements. It includes business queries using joins and aggregate functions, advanced queries using Window Functions and Common Table Expressions (CTEs), customer segmentation, ranking, running totals, year-over-year comparisons, and cohort analysis. These queries demonstrate how SQL can be used to analyze business performance and customer behavior.

A simple Command Line Interface (CLI) was also developed using Python. The application accepts the report type and date range from the user, connects to the SQLite database, and generates summary reports containing total orders, total revenue, unique customers, and the top three selling products. The application also validates user input and handles common edge cases such as invalid report types, incorrect date formats, empty result sets, and database connection errors.

Python development for this project was carried out using **PyCharm Community Edition**, while **DB Browser for SQLite** was used to execute SQL scripts and verify query outputs. Git and GitHub were used for version control throughout the project.

Overall, this project provided practical experience in implementing the complete workflow of a data analytics system by following the assignment requirements. It strengthened my understanding of Python, Pandas, SQLite, SQL, database design, data cleaning, window functions, common table expressions, cohort analysis, and building a simple reporting application.---

# Author
**Suyash Saxena**
B.Tech Computer Engineering
Poornima University