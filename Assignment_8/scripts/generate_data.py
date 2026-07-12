import pandas as pd
import random
from faker import Faker

fake=Faker()

random.seed(56)
Faker.seed(56)

#CUSTOMERS
Total_Customers = 1000

Customer_Types =  [
    "REGULAR",
    "PREMIUM",
    "VIP"
]

#PRODUCTS
Total_Products = 500

Product_Categories = {
    "Electronics": [
        "Mobile",
        "Laptop",
        "Headphones",
        "Smart Watch"
    ],

    "Clothing": [
        "Shirt",
        "Jeans",
        "Jacket",
        "Shoes"
    ],

    "Home": [
        "Chair",
        "Table",
        "Sofa",
        "Lamp"
    ],

    "Books": [
        "Novel",
        "Biography",
        "Programming",
        "Comics"
    ],

    "Sports": [
        "Cricket Bat",
        "Football",
        "Badminton",
        "Gym Equipment"
    ]
}

#ORDERS
Total_Orders = 5000

Order_Status = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

Regions = [
    "North",
    "South",
    "East",
    "West"
]

#ORDER_iTEMS
TOTAL_ORDER_ITEMS = 12000


def generate_customers():

    customer_records = []

    for customer_number in range(1, Total_Customers + 1):
        customer_id = f"C{customer_number:04d}"
        customer_name = fake.name()
        email = fake.email()

        registration_date = fake.date_between(
            start_date="-3y",
            end_date="today"
        )

        customer_type = random.choice(Customer_Types)

        customer_record = {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "email": email,
            "registration_date": registration_date,
            "customer_type": customer_type
        }

        customer_records.append(customer_record)

    customers_df = pd.DataFrame(customer_records)

    #2% Invalid Emails part
    invalid_count = int(0.02 * Total_Customers)

    invalid_rows = random.sample(
        list(customers_df.index),
        invalid_count
    )

    for row in invalid_rows:

        invalid_email = customers_df.loc[row, "email"]

        if "@" in invalid_email:
            invalid_email = invalid_email.replace("@", "")

        customers_df.loc[row, "email"] = invalid_email

    return customers_df


def generate_products():

    product_records = []

    for product_number in range(1, Total_Products + 1):

        product_id = f"P{product_number:04d}"

        category = random.choice(
            list(Product_Categories.keys())
        )

        subcategory = random.choice(
            Product_Categories[category]
        )

        brand = fake.company()
        product_name = f"{brand} {subcategory}"

        cost_price = random.randint(500, 100000)

        product_record = {
            "product_id": product_id,
            "product_name": product_name,
            "category": category,
            "subcategory": subcategory,
            "cost_price": cost_price
        }

        product_records.append(product_record)

    products_df = pd.DataFrame(product_records)

    #5% products w error
    dirty_count = int(0.05 * Total_Products)

    dirty_rows = random.sample(
        list(products_df.index),
        dirty_count
    )

    for row in dirty_rows:
        product_name = products_df.loc[row, "product_name"]
        product_name = "   " + product_name.upper() + "   "
        products_df.loc[row, "product_name"] = product_name

    return products_df

#orders

def generate_orders(customers_df):

    order_records = []

    customer_ids = customers_df["customer_id"].tolist()

    for order_number in range(1, Total_Orders + 1):
        order_id = f"O{order_number:05d}"
        customer_id = random.choice(customer_ids)

        order_date = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        status = random.choice(Order_Status)
        region = random.choice(Regions)

        order_record = {
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date,
            "status": status,
            "region_code": region
        }

        order_records.append(order_record)

    orders_df = pd.DataFrame(order_records)

    #5% Missing Ids
    null_count = int(0.05 * Total_Orders)

    null_rows = random.sample(
        list(orders_df.index),
        null_count
    )

    for row in null_rows:
        orders_df.loc[row, "customer_id"] = None

    #3% Wrong Date
    wrong_date_count = int(0.03 * Total_Orders)

    wrong_date_rows = random.sample(
        list(orders_df.index),
        wrong_date_count
    )

    for row in wrong_date_rows:

        date = orders_df.loc[row, "order_date"]

        orders_df.loc[row, "order_date"] = date.strftime("%d-%m-%Y")

    #Duplicate Orders
    duplicate_orders = orders_df.sample(20)

    orders_df = pd.concat(
        [orders_df, duplicate_orders],
        ignore_index=True
    )

    return orders_df


#Order Items
def generate_order_items(orders_df, products_df):

    item_records = []

    order_ids = orders_df["order_id"].tolist()

    product_ids = products_df["product_id"].tolist()

    for item_number in range(1, TOTAL_ORDER_ITEMS + 1):
        item_id = f"I{item_number:05d}"
        order_id = random.choice(order_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        unit_price = random.randint(500, 100000)
        discount_percent = random.randint(0, 40)

        item_record = {
            "item_id": item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "discount_percent": discount_percent
        }

        item_records.append(item_record)

    order_items_df = pd.DataFrame(item_records)

    #3% Negative Quantity
    negative_count = int(0.03 * TOTAL_ORDER_ITEMS)

    negative_rows = random.sample(
        list(order_items_df.index),
        negative_count
    )

    for row in negative_rows:
        order_items_df.loc[row, "quantity"] *= -1


    return order_items_df

def main():

    customers_df = generate_customers()
    products_df = generate_products()
    orders_df = generate_orders(customers_df)
    order_items_df = generate_order_items(
        orders_df,
        products_df
    )

    customers_df.to_csv("../data/raw/customers.csv", index=False)
    products_df.to_csv("../data/raw/products.csv", index=False)
    orders_df.to_csv("../data/raw/orders.csv", index=False)
    order_items_df.to_csv("../data/raw/order_items.csv", index=False)


if __name__ == "__main__":
    main()