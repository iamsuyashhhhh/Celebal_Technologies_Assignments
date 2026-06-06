import pandas as pd
import sqlite3

df = pd.read_csv("D:\\New\\Assignment_3\\Sample - Superstore.csv", encoding='cp1252')

conn = sqlite3.connect("Superstore.db")

df.to_sql(
    "superstore_raw",
    conn,
    if_exists="replace",
    index=False
)
print("Data is successfully Loaded!")
conn.close()