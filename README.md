# Assignment_Data_Cleaning_Project

## Objective

Perform data exploration and cleaning using Pandas on an e-commerce dataset.

---

## Technologies Used

- Python
- Pandas
- Jupyter Notebook

---


---

## Tasks Performed

1. Loaded CSV dataset into Pandas DataFrame
2. Explored dataset structure
3. Handled missing values
4. Filtered rows and selected columns
5. Removed duplicate records
6. Created derived column:
   total_amount = final_price * quantity
7. Saved cleaned dataset as a new CSV file

---

## Sample Code

```python
import pandas as pd

df = pd.read_csv("Combined_dataset.csv")

df["discount"] = df["discount"].fillna(df["discount"].mean())

df = df.drop_duplicates()

df["quantity"] = 1

df["total_amount"] = df["final_price"] * df["quantity"]

df.to_csv("cleaned_ecommerce_dataset.csv", index=False)
```

---
## How to Run the Project

#### Using Jupyter Notebook

1. Install Python or Anaconda on your system.
2. Open Jupyter Notebook.
3. Place the dataset file (`Combined_dataset.csv`) inside the project folder.
4. Open the notebook file (`Assignment_1.ipynb`).
5. Run all the cells one by one.
6. After execution, the cleaned dataset file will be generated automatically.

---

#### Using PyCharm

1. Open the project folder in PyCharm.
2. Install the required library using:
---

```bash
pip install pandas
```

## Output Files

- Assignment.ipynb
- cleaned_dataset.csv

---

## Brief Summary

```

In this project, 
I worked on an ecommerce dataset using Pandas in Python. 
I explored the dataset.
Checked for missing values.
Cleaned the data.
Removed duplicate rows. 
Performed some basic operations like filtering and selecting data. 
I also created a new column called total_amount. 
Finally saved the cleaned dataset as a new CSV file.


```
---
## Learning Outcomes

Through this project, I learned:

- Basics of Pandas DataFrames 
- Loading and exploring CSV datasets 
- Handling missing values 
- Filtering and selecting data 
- Removing duplicate records 
- Creating derived columns 
- Exporting cleaned datasets
---
