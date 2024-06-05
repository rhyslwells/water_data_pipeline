3. **Data Cleaning*:
   - Write Python scripts to extract data from the database.
   - Cleanse the data by handling missing values, outliers, and inconsistent formats.
   - Process the data to aggregate consumption by different time intervals (daily, weekly, monthly).


### Steps:

Data cleaning is a critical step before analyzing any dataset. Below are common steps for data cleaning, which I will demonstrate on the provided dataset:

1. **Checking for Missing Values**:
    - Identify and handle any missing values.
2. **Checking for Duplicates**:
    - Identify and remove duplicate rows.
3. **Data Type Validation**:
    - Ensure that each column contains data of the expected type.
4. **Consistency Checks**:
    - Ensure that related columns have consistent and correct values.
5. **Handling Invalid Data**:
    
    - Identify and correct or remove any invalid data entries.

Let's perform an initial examination and data cleaning on the dataset provided.

### Steps:

1. Load the dataset.
2. Inspect for missing values.

```python
# Load the dataset and check for missing values and duplicates
data.info(), data.isnull().sum(), data.duplicated().sum()
```

### [[GMMC]] Initial Analysis:

1. **Missing Values**:
    - `resultQualifier.notation`: 16577 missing values out of 19044.
    - `codedResultInterpretation.interpretation`: All values are missing (19044 out of 19044).
2. **Duplicates**:
    - No duplicate rows found.
3. **Data Types**:
    
    - Columns have appropriate data types, except for `sample.sampleDateTime`, which should be converted to a `datetime` type.

1. Check for duplicate rows.
2. Validate data types.
3. Perform consistency checks.

Implement Cleaning in Python

