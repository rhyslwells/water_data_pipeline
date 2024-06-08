import sqlite3
import pandas as pd
import os

# Define the path to the SQLite database
path = 'GMMC-2020-M.db'

# Check if the database file exists
if not os.path.exists(path):
    raise FileNotFoundError(f"The database file {path} does not exist.")

try:
    # Connect to SQLite database
    conn = sqlite3.connect(path)
    print(f"Connected to database: {path}")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    raise

try:
    # Get a cursor object
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables in the database: {tables}")

    # Check if any tables were found
    if not tables:
        raise ValueError("No tables were found in the database.")
except sqlite3.Error as e:
    print(f"Error retrieving table names: {e}")
    raise
finally:
    # Close the connection
    conn.close()

# Create a Pandas Excel writer using openpyxl as the engine
writer = pd.ExcelWriter('database.xlsx', engine='openpyxl')

# Track if any sheet is added
sheet_added = False

# Iterate over tables and write to separate sheets in the XLSX file
for table_name in tables:
    table_name = table_name[0]
    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        if not df.empty:
            df.to_excel(writer, sheet_name=table_name, index=False)
            sheet_added = True
        else:
            print(f"Table {table_name} is empty and will not be added to the Excel file.")
    except Exception as e:
        print(f"Error reading table {table_name}: {e}")

# Check if at least one sheet was added
if not sheet_added:
    raise ValueError("No data was written to the Excel file because all tables were empty.")

# Close the Pandas Excel writer and save the Excel file
writer.close()
