--15. Complex CTE: Cohort Analysis
WITH CustomerCohort AS (
    SELECT c.customer_id, DATE(c.registration_date) AS registration_date,
        strftime('%Y-%m', c.registration_date) AS cohort_month,
        DATE(o.order_date) AS order_date
    FROM customers AS c
    JOIN orders AS o ON c.customer_id = o.customer_id
),

CustomerActivity AS (
    SELECT customer_id, cohort_month, (
        CAST(strftime('%Y', order_date) AS INTEGER) - CAST(strftime('%Y', registration_date) AS INTEGER)) * 12 + (
            CAST(strftime('%m', order_date) AS INTEGER) - CAST(strftime('%m', registration_date) AS INTEGER)
        ) AS month_number
    FROM CustomerCohort
)

SELECT cohort_month, COUNT(
        DISTINCT CASE
            WHEN month_number = 0 THEN customer_id
        END
    ) AS month_0, COUNT(
        DISTINCT CASE
            WHEN month_number = 1 THEN customer_id
        END
    ) AS month_1, COUNT(
        DISTINCT CASE
            WHEN month_number = 2 THEN customer_id
        END
    ) AS month_2, COUNT(
        DISTINCT CASE
            WHEN month_number = 3 THEN customer_id
        END
    ) AS month_3,
    CASE
        WHEN COUNT(
            DISTINCT CASE
                WHEN month_number = 0 THEN customer_id
            END
        ) = 0 THEN 0
        ELSE
            ROUND( COUNT(
                DISTINCT CASE
                    WHEN month_number = 1 THEN customer_id
                END
            ) * 100.0 / COUNT(
                DISTINCT CASE
                    WHEN month_number = 0 THEN customer_id
                END
            ), 2)
    END AS retention_rate
FROM CustomerActivity
GROUP BY cohort_month
ORDER BY cohort_month;


--16. Self-Join with Window Function
SELECT oits1.product_id AS product_a, oits2.product_id AS product_b,
    COUNT(*) AS times_bought_together
FROM order_items AS oits1
JOIN order_items AS oits2
    ON oits1.order_id = oits2.order_id AND oits1.product_id < oits2.product_id
GROUP BY oits1.product_id, oits2.product_id
ORDER BY times_bought_together DESC;