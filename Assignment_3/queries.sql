-- Create Customers Table
CREATE TABLE customers AS
SELECT DISTINCT
"Customer ID" AS customer_id,
"Customer Name" AS customer_name,
Segment
FROM superstore_raw;

SELECT * FROM customers;

-- Create Products Table
CREATE TABLE products AS
SELECT DISTINCT
"Product ID" AS product_id,
"Product Name" AS product_name,
Category,
"Sub-Category" AS sub_category
FROM superstore_raw;

SELECT * FROM products;

-- Create Orders Table
CREATE TABLE orders AS
SELECT
"Order ID" AS order_id,
"Customer ID" AS customer_id,
"Product ID" AS product_id,
Sales,
Quantity,
Profit,
Region,
"Order Date" AS order_date
FROM superstore_raw;

SELECT * FROM orders;


--Step 2: Perform Required Queries
-- 1. Find all orders where sales are greater than the average sales
SELECT *
FROM orders
WHERE sales >
(SELECT AVG(sales)
FROM orders);

-- 2. Find the highest sales order for each customer.
SELECT *
FROM orders
WHERE sales =
(SELECT MAX(sales)
FROM orders
WHERE customer_id = orders.customer_id);

-- 3. Calculate total sales for each customer.
WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
customer_id,
total_sales
FROM sales_summary
ORDER BY total_sales DESC;


-- 4. Find customers whose total sales are above average
WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
customer_id,
total_sales
FROM sales_summary
WHERE total_sales >
(SELECT AVG(total_sales)
FROM sales_summary)
ORDER BY total_sales DESC;

-- 5.Rank all customers based on total sales.
WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
customer_id,
total_sales,
RANK() OVER (ORDER BY total_sales DESC) AS rank_position
FROM sales_summary
ORDER BY rank_position;


-- 6. Assign row numbers to each order within a customer.
SELECT
customer_id,
order_id,
sales,
ROW_NUMBER() OVER
(PARTITION BY customer_id
ORDER BY sales DESC) AS row_number
FROM orders
ORDER BY customer_id, row_number;

-- 7. Display top 3 customers based on total sales.
WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id),
customer_ranking AS
(SELECT
customer_id,
total_sales,
RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
FROM sales_summary)

SELECT
customer_id,
total_sales,
sales_rank
FROM customer_ranking
WHERE sales_rank <= 3;

---

-- STEP 3 : FINAL COMBINED QUERY

WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
cust.customer_name,
ss.total_sales,
RANK() OVER (ORDER BY ss.total_sales DESC) AS customer_rank
FROM sales_summary ss
JOIN customers cust
ON ss.customer_id = cust.customer_id
ORDER BY customer_rank;

---

-- MINI PROJECT : CUSTOMER SALES INSIGHTS

-- 1. Top 5 Customers

WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
cust.customer_name,
ss.total_sales
FROM sales_summary ss
JOIN customers cust
ON ss.customer_id = cust.customer_id
ORDER BY ss.total_sales DESC
LIMIT 5;

-- 2. Bottom 5 Customers

WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
cust.customer_name,
ss.total_sales
FROM sales_summary ss
JOIN customers cust
ON ss.customer_id = cust.customer_id
ORDER BY ss.total_sales ASC
LIMIT 5;

-- 3. Customers made only one order

SELECT
cust.customer_name,
COUNT(ord.order_id) AS total_orders
FROM orders ord
JOIN customers cust
ON ord.customer_id = cust.customer_id
GROUP BY ord.customer_id, cust.customer_name
HAVING COUNT(ord.order_id) = 1;

-- 4. Customers with above-average sales

WITH sales_summary AS
(SELECT
customer_id,
SUM(sales) AS total_sales
FROM orders
GROUP BY customer_id)

SELECT
cust.customer_name,
ss.total_sales
FROM sales_summary ss
JOIN customers cust
ON ss.customer_id = cust.customer_id
WHERE ss.total_sales >
(SELECT AVG(total_sales)
FROM sales_summary)
ORDER BY ss.total_sales DESC;

-- 5. Highest order value for each customer
SELECT
cust.customer_name,
MAX(ord.sales) AS highest_order_value
FROM orders ord
JOIN customers cust
ON ord.customer_id = cust.customer_id
GROUP BY ord.customer_id, cust.customer_name
ORDER BY highest_order_value DESC;
