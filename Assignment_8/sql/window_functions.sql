--7. Running Totals with Window Functions
WITH DailyRevenue AS (
    SELECT o.region_code, DATE(o.order_date) AS order_date,
        ROUND( SUM(
            oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)
        ), 2) AS daily_revenue
    FROM orders AS o
    JOIN order_items AS oits ON o.order_id = oits.order_id
    GROUP BY o.region_code, DATE(o.order_date)
)

SELECT region_code, order_date, daily_revenue, SUM(daily_revenue)
    OVER(
        PARTITION BY region_code
        ORDER BY order_date
    ) AS running_total
FROM DailyRevenue;




--8.Ranking with DENSE_RANK
WITH CustomerLifetimeValue AS (
    SELECT c.customer_id, c.customer_name, ROUND( SUM(
        oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)
    ), 2) AS lifetime_value
    FROM customers AS c
    JOIN orders AS o ON c.customer_id = o.customer_id
    JOIN order_items AS oits ON o.order_id = oits.order_id
    GROUP BY c.customer_id, c.customer_name
)

SELECT customer_id, customer_name, lifetime_value, DENSE_RANK()
    OVER(
        ORDER BY lifetime_value DESC
    ) AS customer_rank
FROM CustomerLifetimeValue;



--9. LAG/LEAD Analysis
WITH CustomerOrders AS (
    SELECT customer_id, DATE(order_date) AS order_date, LAG(DATE(order_date))
        OVER(
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
),

OrderGap AS (
    SELECT customer_id, order_date, previous_order_date,
        JULIANDAY(order_date) - JULIANDAY(previous_order_date) AS days_gap
    FROM CustomerOrders
)

SELECT customer_id, order_date, previous_order_date, ROUND(days_gap,2) AS days_gap,
    CASE
        WHEN AVG(days_gap) OVER(PARTITION BY customer_id) > 30 THEN 'At Risk' ELSE 'Active'
    END AS customer_status
FROM OrderGap;




--10. CTE with Multiple Levels
WITH MonthlyRevenue AS (
    SELECT o.customer_id, strftime('%Y-%m',o.order_date) AS revenue_month, SUM(
        oits.quantity * oits.unit_price * (1-oits.discount_percent/100.0)
    ) AS monthly_revenue
    FROM orders AS o
    JOIN order_items AS oits ON o.order_id=oits.order_id
    GROUP BY o.customer_id, revenue_month
),

CustomerCategory AS (
    SELECT revenue_month, customer_id, monthly_revenue,
        CASE
            WHEN monthly_revenue > 10000 THEN 'High'
            WHEN monthly_revenue >=5000 THEN 'Medium'
            ELSE 'Low'
        END AS spend_category
    FROM MonthlyRevenue
)

SELECT revenue_month, spend_category, COUNT(customer_id) AS total_customers
FROM CustomerCategory
GROUP BY revenue_month, spend_category
ORDER BY revenue_month;




--11. NTILE for Segmentation
WITH CustomerRevenue AS (
    SELECT c.customer_id, ROUND( SUM(
        oits.quantity *  oits.unit_price * (1-oits.discount_percent/100.0)
    ), 2) AS total_value
    FROM customers AS c
    JOIN orders AS o ON c.customer_id=o.customer_id
    JOIN order_items AS oits ON o.order_id=oits.order_id
    GROUP BY c.customer_id
)

SELECT customer_id, total_value, NTILE(4)
    OVER(
        ORDER BY total_value DESC
    ) AS quartile,
    CASE
        WHEN NTILE(4) OVER(ORDER BY total_value DESC)=1 THEN 'Platinum'
        WHEN NTILE(4) OVER(ORDER BY total_value DESC)=2 THEN 'Gold'
        WHEN NTILE(4) OVER(ORDER BY total_value DESC)=3 THEN 'Silver'
        ELSE 'Bronze'
    END AS quartile_label
FROM CustomerRevenue;




--12. Year-over-Year Comparison
WITH MonthlyRevenue AS (
    SELECT strftime('%Y', o.order_date) AS year, strftime('%m', o.order_date) AS month, ROUND( SUM(
        oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)), 2
        ) AS revenue
    FROM orders AS o
    JOIN order_items AS oits ON o.order_id = oits.order_id
    GROUP BY year, month
)

SELECT year, month, revenue, LAG(revenue)
    OVER(
        PARTITION BY month
        ORDER BY year
    ) AS prev_year_revenue, ROUND((
        revenue - LAG(revenue)
            OVER(
                PARTITION BY month
                ORDER BY year
            )
    ) * 100.0 / LAG(revenue)
    OVER(
        PARTITION BY month
        ORDER BY year
    ), 2) AS yoy_growth_percent
FROM MonthlyRevenue;



--13. First/Last Value Analysis
WITH CustomerPurchaseHistory AS (
    SELECT o.customer_id, pr.category, DATE(o.order_date) AS order_date
    FROM orders AS o
    JOIN order_items AS oits ON o.order_id = oits.order_id
    JOIN products AS pr ON oits.product_id = pr.product_id
)

SELECT DISTINCT customer_id, FIRST_VALUE(category)
    OVER(
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS first_category, LAST_VALUE(category)
    OVER(
        PARTITION BY customer_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_category,
    CASE
        WHEN FIRST_VALUE(category)
            OVER(
                PARTITION BY customer_id
                ORDER BY order_date
            ) = LAST_VALUE(category)
            OVER(
                PARTITION BY customer_id
                ORDER BY order_date
                ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
            )
        THEN 'No' ELSE 'Yes'
    END AS category_shift
FROM CustomerPurchaseHistory;



--14. Cumulative Distribution
WITH CustomerRevenue AS (
    SELECT c.customer_id, ROUND( SUM(
        oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)), 2) AS revenue
    FROM customers AS c
    JOIN orders AS o ON c.customer_id = o.customer_id
    JOIN order_items AS oits ON o.order_id = oits.order_id
    GROUP BY c.customer_id
)

SELECT customer_id, revenue, SUM(revenue)
    OVER(
        ORDER BY revenue DESC
    ) AS cumulative_revenue, ROUND( SUM(revenue)
        OVER(
            ORDER BY revenue DESC
        ) * 100.0 / SUM(revenue)
        OVER(), 2
    ) AS cumulative_percent
FROM CustomerRevenue
ORDER BY revenue DESC;