import sqlite3
from datetime import datetime

#Db config
DATABASE_PATH = "../ecommerce.db"


#Database Connection
def create_connection():
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        return connection
    except sqlite3.Error as error:
        print("\nUnable to connect to database.")
        print(error)
        return None



#Validating Report Type
def validate_report_type(report_type):
    valid_reports = [
        "daily",
        "weekly",
        "monthly"
    ]
    if report_type.lower() in valid_reports:
        return True
    return False




#Validating Date
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False




#User Input
def get_user_input():
    print("=" * 55)
    print(" E-Commerce Analytics Reporting System ")
    print("=" * 55)
    report_type = input(
        "Enter Report Type (daily / weekly / monthly): "
    ).strip().lower()
    if not validate_report_type(report_type):
        print("\nInvalid Report Type.")
        print("Please choose daily, weekly or monthly.")
        return None
    start_date = input(
        "Enter Start Date (YYYY-MM-DD): "
    )
    end_date = input(
        "Enter End Date (YYYY-MM-DD): "
    )
    if not validate_date(start_date):
        print("\nInvalid Start Date Format.")
        return None
    if not validate_date(end_date):
        print("\nInvalid End Date Format.")
        return None
    if start_date > end_date:
        print("\nStart Date cannot be greater than End Date.")
        return None
    return report_type, start_date, end_date




#Generate Summary Report
def generate_summary( connection, start_date, end_date ):
    cursor = connection.cursor()
    query = """
    SELECT COUNT(DISTINCT o.order_id), ROUND( SUM(
        oits.quantity *
        oits.unit_price *
        (1 - oits.discount_percent / 100.0)),2), COUNT(DISTINCT o.customer_id)
    FROM orders AS o
    JOIN order_items AS oits
        ON o.order_id = oits.order_id
    WHERE DATE(o.order_date)
    BETWEEN ? AND ?
    """

    cursor.execute( query,( start_date, end_date ))
    result = cursor.fetchone()
    if result is None:
        return None
    summary = {
        "total_orders": result[0] if result[0] else 0,
        "total_revenue": result[1] if result[1] else 0,
        "unique_customers": result[2] if result[2] else 0
    }
    return summary



#Displaying Summary
def display_summary( report_type, start_date, end_date, summary):
    print("\n")
    print("=" * 55)
    print("E-Commerce Summary Report")
    print("=" * 55)
    print(f"Report Type: {report_type.title()}")
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print("-" * 55)
    print(f"Total Orders: {summary['total_orders']}")
    print(f"Total Revenue: {summary['total_revenue']}")
    print(f"Unique Customers  : {summary['unique_customers']}")
    print("-" * 55)



#Top 3 Products
def get_top_products( connection, start_date, end_date ):
    cursor = connection.cursor()
    query = """
    SELECT pr.product_name, SUM(oits.quantity) AS total_quantity, ROUND(SUM(
        oits.quantity * oits.unit_price * (1 - oits.discount_percent / 100.0)), 2 ) AS total_revenue
    FROM products AS pr
    JOIN order_items AS oits
        ON pr.product_id = oits.product_id
    JOIN orders AS o
        ON oits.order_id = o.order_id
    WHERE DATE(o.order_date)
    BETWEEN ? AND ?
    GROUP BY pr.product_id, pr.product_name
    ORDER BY total_revenue DESC
    LIMIT 3;
    """
    cursor.execute( query, ( start_date, end_date ))
    return cursor.fetchall()


#Displaying Top Products
def display_top_products(products):
    print("\nTop 3 Products")
    print("-" * 55)
    if len(products) == 0:
        print("No products found.")
        return
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product[0]}")
        print(f"Quantity Sold: {product[1]}")
        print(f"Revenue: {product[2]}")
        print()


# Main
def main():
    user_input = get_user_input()
    if user_input is None:
        return
    report_type, start_date, end_date = user_input
    connection = create_connection()
    if connection is None:
        return
    try:
        summary = generate_summary( connection, start_date, end_date )
        if summary["total_orders"] == 0:
            print("\nNo records found for the selected date range.")
            connection.close()
            return
        display_summary( report_type, start_date, end_date, summary )
        products = get_top_products( connection, start_date, end_date )
        display_top_products(products)
        print("=" * 55)
        print("Report Generated Successfully")
        print("=" * 55)
    except sqlite3.Error as error:
        print("\nDatabase Error")
        print(error)
    finally:
        connection.close()


if __name__ == "__main__":
    main()