# Assignment 2: Sales Data Analysis Using SQL

## Project Overview

I worked on a project that looked at sales data from the Superstore dataset using SQL and PostgreSQL. The sales data was put into a database. I used different SQL queries to see how well sales were doing what customers were buying what products were popular and if the data was good.

This project showed me how to use SQL in a way like filtering adding up numbers, sorting, grouping and checking if the data is correct. I was able to get information from the sales data and see how SQL can help businesses make good decisions.

---

## Objective

The goal of this assignment was to look at sales data using SQL by trying out query techniques.

I did the tasks:

* I put the dataset into a SQL database.

* I looked at the table structure. Some sample records.

* I used filters with WHERE conditions.

* I added up numbers using GROUP BY.

* I. Limited the results.

* I solved queries that were related to business.

* I checked the data quality and record consistency.

* I got insights from the dataset.

---

## Tools Used

* PostgreSQL

* SQL

* Python

* Pandas

* SQLAlchemy

* PyCharm

---

## Dataset

The dataset used is called the Sample Superstore Dataset.

This dataset has information about:

* Customers

* Products

* Sales transactions

* Quantity sold

* Profit and discount values

* Region and state information

* Shipping details

The dataset has 9,994 sales records and many attributes that are useful for business analysis.

---

## Project Structure

Assignment_2_SQL_Sales_Analysis/

├── Sample. Superstore.csv

├── data_load.py

├── queries.sql

├── Assignment_2_SQL_Analysis_and_Insights.pdf

└── README.md

---

## Tasks Performed

### 1. Data Loading

* I imported the Superstore dataset using Pandas.

* I connected Python with PostgreSQL using SQLAlchemy.

* I put the dataset into PostgreSQL as a database table.

### 2. Data Exploration

* I looked at some sample records from the dataset.

* I checked how rows there were.

* I explored the table schema and column data types.

### 3. Data Filtering

I applied filters based on:

* Region

* Category

* Sales

* Profit

* Discount

### 4. Aggregation Analysis

I did calculations using:

* SUM

* AVG

* COUNT

I added up data based on:

* Category

* Region

* Segment

* Ship Mode

### 5. Sorting and Ranking

I found:

* The top selling products

* The top customers

* The top states

* The high performing categories

### 6. Business Analysis

I did queries to analyze:

* Sales trends

* Customer purchasing behavior

* Product performance

* sales contribution

### 7. Data Validation

I did quality checks including:

* Finding duplicate records

* Checking for values

* Counting customers

* Counting products

---

## How to Run

### Step 1: Install Required Libraries

```bash

pip install pandas sqlalchemy psycopg2-binary

```

### Step 2: Start PostgreSQL

Make sure the PostgreSQL server is running on your system.

### Step 3: Configure Database Credentials

Update the PostgreSQL username, password and database name in:

```python

data_load.py

```

### Step 4: Run Data Loading Script

```bash

python data_load.py

```

This will create the table. Put the dataset into PostgreSQL.

### Step 5: Execute SQL Queries

Open the PostgreSQL Query Console. Run the queries in:

```text

queries.sql

```

---

## Output Files

### queries.sql

This has all the SQL queries I used for data analysis and validation.

### Assignment_2_SQL_Analysis_and_Insights.pdf

This has:

* The results of the queries

* Screenshots of the output

* Some brief project insights

---

## Learning Outcomes

From this assignment I got hands-on experience in:

* Working with PostgreSQL databases

* Putting datasets into SQL databases using Python

* Writing SQL queries for data analysis

* Using WHERE, GROUP BY, ORDER BY and LIMIT clauses

* Applying aggregate functions like SUM, AVG and COUNT

* Doing data validation checks

* Getting information from business datasets

* Understanding how SQL is used for real-world data analysis tasks

---

## Conclusion

This project gave me experience with SQL-based data analysis using PostgreSQL. By working with a real sales dataset I was able to apply SQL concepts and do meaningful analysis, on customer, product and sales information. The assignment helped me understand database operations better. Showed me how SQL can help businesses make good decisions based on data.
