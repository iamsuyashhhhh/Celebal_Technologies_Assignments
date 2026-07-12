import pandas as pd


# Read Raw Data

customers_df = pd.read_csv("../data/raw/customers.csv")
products_df = pd.read_csv("../data/raw/products.csv")
orders_df = pd.read_csv("../data/raw/orders.csv")
order_items_df = pd.read_csv("../data/raw/order_items.csv")



#Clean Orders

def clean_orders(df):

    print("\nCleaning Orders...")
    issues = []
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        issues.append(f"Duplicate Orders Removed : {duplicate_count}")

    df = df.drop_duplicates()

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce",
    )

    invalid_dates = df["order_date"].isnull().sum()

    if invalid_dates > 0:
        issues.append(f"Invalid Dates Found : {invalid_dates}")

    # Fill NULL customer IDs
    null_customers = df["customer_id"].isnull().sum()

    if null_customers > 0:
        issues.append(f"NULL Customer IDs : {null_customers}")

    df["customer_id"] = df["customer_id"].fillna("UNKNOWN")

    return df, issues




#Clean Products

def clean_products(df):

    print("\nCleaning Products...")
    issues = []
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        issues.append(f"Duplicate Products Removed : {duplicate_count}")

    df = df.drop_duplicates()

    df["product_name"] = (
        df["product_name"]
        .str.strip()
        .str.title()
    )

    return df, issues




#Validate Emails

def validate_emails(df):

    print("\nChecking Emails...")

    invalid_customer_ids = df.loc[
        ~df["email"].str.contains("@", na=False),
        "customer_id"
    ].tolist()

    return invalid_customer_ids





# 4. Check Referential Integrity

def check_referential_integrity(orders_df, order_items_df):

    print("\nChecking Referential Integrity...")

    invalid_order_items = order_items_df[
        ~order_items_df["order_id"].isin(
            orders_df["order_id"]
        )
    ]

    return invalid_order_items




def main():

    orders_clean, order_issues = clean_orders(orders_df)
    products_clean, product_issues = clean_products(products_df)
    invalid_customer_ids = validate_emails(customers_df)
    invalid_order_items = check_referential_integrity(
        orders_clean,
        order_items_df
    )

     # Save cleaned files
    customers_df.to_csv(
        "../data/cleaned/customers_clean.csv",
        index=False
    )

    products_clean.to_csv(
        "../data/cleaned/products_clean.csv",
        index=False
    )

    orders_clean.to_csv(
        "../data/cleaned/orders_clean.csv",
        index=False
    )

    order_items_df.to_csv(
        "../data/cleaned/order_items_clean.csv",
        index=False
    )

    # Save Issues Report
    with open("../data/cleaned/issues_report.txt", "w") as report:

        report.write("DATA CLEANING REPORT\n")
        report.write("=" * 20 + "\n\n")

        report.write("ORDER ISSUES\n")

        for issue in order_issues:
            report.write(issue + "\n")

        report.write("\nPRODUCT ISSUES\n")

        for issue in product_issues:
            report.write(issue + "\n")

        report.write("\nINVALID EMAIL CUSTOMER IDs\n")

        for customer in invalid_customer_ids:
            report.write(customer + "\n")

        report.write("\nINVALID ORDER REFERENCES\n")

        if len(invalid_order_items) == 0:
            report.write("No Invalid Order References Found\n")
        else:
            report.write(
                invalid_order_items.to_string(index=False)
            )

    print("\nCleaning Completed Successfully")
    print(f"\nInvalid Emails : {len(invalid_customer_ids)}")
    print(f"\nInvalid Order References : {len(invalid_order_items)}")


if __name__ == "__main__":
    main()