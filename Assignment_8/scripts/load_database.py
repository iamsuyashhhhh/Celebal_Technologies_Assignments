import sqlite3
import pandas as pd

connection = sqlite3.connect("../ecommerce.db")
cursor = connection.cursor()
print("Connected to SQLite Database.")

with open("../sql/schema.sql", "r") as file:
    schema = file.read()

cursor.executescript(schema)

customers_df = pd.read_csv("../data/cleaned/customers_clean.csv")
products_df = pd.read_csv("../data/cleaned/products_clean.csv")
orders_df = pd.read_csv("../data/cleaned/orders_clean.csv")
order_items_df = pd.read_csv("../data/cleaned/order_items_clean.csv")

customers_df.to_sql(
    "customers",
    connection,
    if_exists="append",
    index=False
)

products_df.to_sql(
    "products",
    connection,
    if_exists="append",
    index=False
)

orders_df.to_sql(
    "orders",
    connection,
    if_exists="append",
    index=False
)

order_items_df.to_sql(
    "order_items",
    connection,
    if_exists="append",
    index=False
)

print("Data Insertion Done ")

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

print("\nROW COUNT VERIFICATION")

for table in tables:
    query = f"SELECT COUNT(*) AS total_rows FROM {table}"
    count = pd.read_sql(query, connection)
    print(f"\n{table.upper()}")

    print(count)

connection.commit()
connection.close()



