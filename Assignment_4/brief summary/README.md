# Azure Cloud Fundamentals and Data Pipeline Implementation using Azure Data Factory

## Project Overview

This project demonstrates the implementation of an end-to-end data pipeline using Microsoft Azure services. The pipeline reads a CSV file from Azure Blob Storage, validates file metadata using Azure Data Factory (ADF), and copies the data to a destination container.

The project covers fundamental Azure cloud concepts, including Resource Groups, Storage Accounts, Blob Containers, Azure Data Factory, Linked Services, Datasets, Pipeline Activities, Monitoring, and Identity & Access Management (IAM).

---

## Objective

The objective of this project is to:

* Understand Azure cloud fundamentals.
* Create and manage Azure resources.
* Store and manage data in Azure Blob Storage.
* Build an ETL-style pipeline using Azure Data Factory.
* Validate source file metadata before processing.
* Copy data from a source container to a destination container.
* Configure IAM roles for secure access between Azure services.
* Monitor and validate successful pipeline execution.

---

## Architecture

```text
+----------------------+
| Azure Blob Storage   |
| superstore.csv       |
+----------+-----------+
           |
           |
           v
+----------------------+
| Get Metadata         |
| (File Validation)    |
+----------+-----------+
           |
           |
           v
+----------------------+
| Copy Data Activity   |
+----------+-----------+
           |
           |
           v
+----------------------+
| Destination Blob     |
| superstore_copy.csv  |
+----------------------+
```

---

## Azure Services Used

* Azure Resource Group
* Azure Storage Account
* Azure Blob Storage
* Azure Data Factory (ADF)
* Azure Identity and Access Management (IAM)

---

## Project Steps

### 1. Resource Group Creation

A Resource Group was created to organize and manage all Azure resources associated with the project.

**Resource Group:**

```text
Assignment-Resource-Group

```

---

### 2. Storage Account Setup

A Storage Account was created to store the source and destination data files.

**Components Created:**

* Storage Account
* Blob Container (raw-data)
* Blob Container (processed-data)

The Superstore dataset (`Sample - Superstore.csv`) was uploaded to the `raw-data` container.

---

### 3. Azure Data Factory Configuration

An Azure Data Factory instance was created and configured.

The following components were developed:

#### Linked Service

Connection established between Azure Data Factory and Azure Blob Storage.

#### Source Dataset

Configured to access:

```text
raw-data/superstore.csv
```

#### Destination Dataset

Configured to store processed data in:

```text
processed-data/
```

---

### 4. Metadata Validation

A **Get Metadata** activity was added to the pipeline to validate the source file before processing.

Metadata fields checked:

* Exists
* Size
* Last Modified

This ensures the source file is available and ready for processing.

---

### 5. Pipeline Development

A pipeline named:

```text
pipeline_superstore
```

was created using:

* Get Metadata Activity
* Copy Data Activity

Pipeline Flow:

```text
Get Metadata
      ↓
Copy Data
```

---

### 6. IAM Configuration

Role assignments were configured to allow Azure Data Factory to access Blob Storage.

Roles Assigned:

* Reader
* Storage Blob Data Contributor

These permissions enable ADF to read, validate, and copy files within Azure Storage.

---

### 7. Pipeline Execution

The pipeline was executed using the **Debug** feature in Azure Data Factory.

Execution Status:

```text
Get Metadata  : Succeeded
Copy Data     : Succeeded
Pipeline Run  : Succeeded
```

---

### 8. Output Validation

The pipeline successfully copied:

```text
Sample - Superstore.csv
```

from:

```text
raw-data
```

to:

```text
processed-data
```

Output File:

```text
Sample - Superstore(1).csv
```

Metadata validation was completed successfully before the copy operation.

---

## Screenshots

The following screenshots are included in the project:

* Resource Group
* Storage Account
* Blob Container with uploaded CSV
* Linked Service Configuration
* Source and Destination Datasets
* Get Metadata Activity
* Pipeline Design
* IAM Role Assignments
* Successful Pipeline Execution
* Monitor Dashboard

---

## Results

* Successfully created Azure cloud resources.
* Uploaded and managed data using Azure Blob Storage.
* Built an end-to-end data pipeline using Azure Data Factory.
* Implemented metadata validation using Get Metadata activity.
* Copied data from source to destination container.
* Configured IAM permissions for secure resource access.
* Monitored and verified successful pipeline execution.

---

## Conclusion

This project provided hands-on experience with Azure cloud services and modern data engineering workflows. By integrating Azure Blob Storage with Azure Data Factory, an automated pipeline was created to validate and transfer data efficiently. The project demonstrates foundational cloud and ETL skills that are widely used in real-world data engineering environments.
