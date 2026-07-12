--1. Total revenue per category (revenue = quantity × unit_price × (1 - discount_percent/100))
SELECT pr.category, ROUND( SUM(
    oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)), 2 ) AS total_revenue
FROM products AS pr
JOIN order_items AS oits ON pr.product_id = oits.product_id
GROUP BY pr.category
ORDER BY total_revenue DESC;



--2. Top 10 customers by total order value
SELECT c.customer_id, c.customer_name, ROUND( SUM(
    oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)), 2 ) AS total_order_value
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id
JOIN order_items AS oits ON o.order_id = oits.order_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_order_value DESC
LIMIT 10;



--3. Month-wise order count for the last 12 months
SELECT strftime('%Y-%m', o.order_date) AS order_month, COUNT(o.order_id) AS total_orders
FROM orders AS o
WHERE DATE(o.order_date) >= DATE('now', '-12 months')
GROUP BY strftime('%Y-%m', o.order_date)
ORDER BY order_month;



--4. Find customers who placed orders but never had any item delivered
SELECT c.customer_id, c.customer_name
FROM customers AS c
JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(
    CASE
        WHEN o.status = 'DELIVERED' THEN 1 ELSE 0
        END
    ) = 0;

--5. Products that were ordered but had more returns than purchases
SELECT pr.product_id, pr.product_name, SUM(
    CASE
        WHEN o.status = 'RETURNED' THEN oits.quantity ELSE 0
    END
) AS returned_quantity, SUM(
    CASE
        WHEN o.status <> 'RETURNED' THEN oits.quantity ELSE 0
    END
) AS purchased_quantity
FROM products AS pr
JOIN order_items AS oits ON pr.product_id = oits.product_id
JOIN orders AS o ON oits.order_id = o.order_id
GROUP BY pr.product_id, pr.product_name
HAVING returned_quantity > purchased_quantity;



--6. Calculate the return rate (returned items / total items) per category
SELECT pr.category, SUM(
    CASE
        WHEN o.status = 'RETURNED' THEN oits.quantity ELSE 0
    END
) AS returned_items, SUM(oits.quantity) AS total_items, ROUND(( SUM(
    CASE
        WHEN o.status = 'RETURNED' THEN oits.quantity ELSE 0
    END
) * 100.0 ) / SUM(oits.quantity), 2 ) AS return_rate_percent
FROM products AS pr
JOIN order_items AS oits ON pr.product_id = oits.product_id
JOIN orders AS o ON oits.order_id = o.order_id
GROUP BY pr.category
ORDER BY return_rate_percent DESC;