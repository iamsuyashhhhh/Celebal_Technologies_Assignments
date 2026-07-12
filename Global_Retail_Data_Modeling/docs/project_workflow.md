# Project Workflow

## Step 1

Load CRM and ERP datasets into the Bronze Layer.

---

## Step 2

Clean and standardize data in the Silver Layer.

Tasks performed:

- Remove duplicates
- Standardize gender
- Standardize marital status
- Validate dates
- Validate sales records
- Join CRM and ERP data

---

## Step 3

Build Gold Layer.

Created:

- Customer Dimension
- Product Dimension
- Date Dimension
- Geography Dimension
- Fact Sales

---

## Step 4

Generate Business Reports.

Implemented:

- Revenue Analysis
- Customer Analysis
- Product Analysis
- Order Analysis

---

## Step 5

Perform Incremental Loading using Delta MERGE.