# Delta Lake Incremental Data Processing

## Objective

The objective of this assignment is to understand and implement **incremental data processing** using **Delta Lake** in Databricks. The assignment demonstrates how to load data into Delta tables, clean the data, simulate incremental data, perform MERGE operations, and validate the final results.

---

## Technologies Used

- Apache Spark (PySpark)
- Delta Lake
- Databricks
- CSV Dataset (superstore)

---

## Dataset

This project uses the **superstore** dataset.

### Files

```
data/
├── superstore.csv
└── superstore_incremental.csv
```

- **superstore.csv** : Original dataset used to create the main Delta table.
- **superstore_incremental.csv** : Simulated incremental dataset containing updated and new records (generated using superstore).

---

## Workflow

### 1. Load Master Dataset
- Load the original CSV file into a Spark DataFrame.
- Display the dataset.

### 2. Data Cleaning
- Remove null values.
- Remove duplicate rows.
- Rename column names by replacing spaces with underscores to make them compatible with Delta tables.

### 3. Create Main Delta Table
- Store the cleaned master dataset as a Delta table named:

```
superstore_delta
```

### 4. Load Incremental Dataset
- Load the incremental CSV file.
- Perform the same cleaning process.
- Store it as another Delta table named:

```
superstore_incremental
```

### 5. Perform Incremental MERGE
Merge the incremental Delta table into the main Delta table.

- Existing records are updated.
- New records are inserted.

### 6. Validate Results
- Verify total record count.
- Check for duplicate records.
- Display the final merged dataset.

---

## Project Flow

```
  superstore.csv
        │
        ▼
   Data Cleaning
        │
        ▼
 Main Delta Table
(superstore_delta)
        ▲
        │
      MERGE
        │
 Incremental Delta Table
(superstore_incremental)
        ▲
        │
superstore_incremental.csv
```

---

## Key Concepts

### Delta Lake

Delta Lake is an open-source storage layer that provides ACID transactions, schema enforcement, and efficient data processing on top of data lakes.

### Incremental Data

Incremental data contains only the newly added or modified records instead of the complete dataset.

### MERGE Operation

The MERGE operation combines update and insert operations into a single command.

- Existing records are updated.
- New records are inserted automatically.

---

## Validation

The following validations were performed after the MERGE operation:

- Total row count verification
- Duplicate record verification
- Final dataset display

---

## Learning Outcomes

After completing this assignment, I learned how to:

- Load CSV files into Spark DataFrames.
- Clean datasets using PySpark.
- Create Delta tables.
- Simulate incremental datasets.
- Perform MERGE operations using Delta Lake.
- Validate merged datasets.
- Understand the importance of incremental processing in ETL pipelines.

---

## Conclusion

This assignment shows how Delta Lake makes incremental data processing easier by using the MERGE operation to handle updates and new records efficiently. Instead of processing the entire dataset every time, it only processes newly added or changed data, which helps make ETL pipelines faster, more efficient, and easier to scale.