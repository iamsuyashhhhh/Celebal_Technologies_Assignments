# Spark Assignment

## Overview

This assignment demonstrates the basic concepts of Apache Spark using PySpark. The objective is to understand Spark architecture, perform data processing on a real-world dataset, apply transformations and actions, build a simple data pipeline, and save the processed data.
The dataset used in this assignment contains information about students' academic performance and AI tool usage.

---

## Objectives/Steps

Steps:

- Understand Spark architecture (Driver, Cluster Manager, Executors) and execution modes.
- Learn Lazy Evaluation and how it optimizes execution using DAG (Lineage Graph).
- Read data from files (CSV, Parquet) with proper schema handling.
- Perform filtering and selection of required columns.
- Modify DataFrames (rename columns, cast data types, add new columns).
- Apply transformations and actions appropriately.
- Understand wide transformations and performance concepts (Shuffle, Predicate Pushdown).
- Work with different file formats (CSV vs Parquet) and their impact on performance.
- Handle null values and filter datasets efficiently.
- Build data pipelines (read → transform → filter → write).
- Save processed data into required formats (CSV/Parquet).

---

## Technologies Used

- Python
- Apache Spark (PySpark)
- Hadoop WinUtils (Windows)
- Jupyter Notebook

---

## Dataset

**Dataset Name:AI Student Impact Dataset**

The dataset contains information such as:

- Student ID
- Major Category
- Pre Semester GPA
- Post Semester GPA
- Weekly GenAI Hours
- Traditional Study Hours
- Skill Retention Score
- Burnout Risk Level
- Anxiety Level During Exams

---
## Theory Part

Export processed data into:

- CSV
- Parquet

Parquet is preferred because it:

- Uses columnar storage
- Compresses data efficiently
- Reads only required columns
- Improves query performance

---

### Spark Concepts Covered

### Spark Architecture

- Driver Program
- Cluster Manager
- Executors
- Worker Nodes

---

### Lazy Evaluation

Spark records transformations but executes them only when an action is called.

Example actions:

- show()
- count()
- collect()
- write()

---

### Narrow Transformations

Examples:

- select()
- filter()
- withColumn()

No data shuffle occurs.

---

### Wide Transformations

Examples:

- groupBy()
- join()
- distinct()

Data shuffle occurs across partitions.

---

### Predicate Pushdown

Filters are pushed to the data source so that unnecessary data is not read, improving performance.

## Tasks Performed

### Read CSV File

Loaded the dataset into a Spark DataFrame.

### Data Exploration

- Displayed the schema
- Displayed sample records
- Selected required columns

### Filtering

Filtered records based on different conditions.

### Aggregation

Performed:

- `groupBy()`
- `count()`
- `avg()`

to analyze the dataset.

### Column Operations

- Renamed columns
- Casted data types
- Created new calculated columns

Example:

- GPA Improvement

### Null Handling

- Checked for missing values
- Removed rows containing null values using `dropna()`


### Output

- Successfully processed dataset
- Cleaned and transformed DataFrame
- CSV output
- Parquet output

---

## Learning Outcomes

After completing this assignment, I learned:

- Spark DataFrame operations
- Data filtering
- Aggregation functions
- Column transformations
- Data type casting
- Null value handling
- Building a basic Spark ETL pipeline
- Reading and writing different file formats

---

## Project Structure

```
Assignment_06/
│
├── data/
│   └── ai_student_impact_dataset.csv
├── notebook/
│   └── spark1.ipynb
├── output/
│   └── output_csv
│   └── output_parquet
└── README.md
    
```

---

## Conclusion

This assignment helped me understand the fundamentals of Apache Spark and PySpark. I gained hands-on experience with DataFrame operations, transformations, aggregations, null handling, and building a simple end-to-end data processing pipeline.