import sqlite3
import pandas as pd

# Connect to SQLite database
path = 'GMMC-2020-M.db'
conn = sqlite3.connect(path)

# Get a cursor object
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Create a Pandas Excel writer using openpyxl as the engine
writer = pd.ExcelWriter('database.xlsx', engine='openpyxl')

# Iterate over tables and write to separate sheets in the XLSX file
for table_name in tables:
    table_name = table_name[0]
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    df.to_excel(writer, sheet_name=table_name, index=False)

# Close the Pandas Excel writer and save the Excel file
writer.close()

# Close the connection
conn.close()
