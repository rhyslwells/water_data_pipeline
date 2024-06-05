   import pandas as pd
   import sqlite3

   # Connect to the database
   conn = sqlite3.connect('water_consumption.db')
   
   # Load data
   df = pd.read_sql_query("SELECT * FROM WaterConsumption", conn)
   
   # Clean and process data
   df['Date'] = pd.to_datetime(df['Date'])
   df['ConsumptionVolume'] = pd.to_numeric(df['ConsumptionVolume'], errors='coerce')
   df.dropna(inplace=True)
   
   # Aggregate data
   daily_consumption = df.groupby(df['Date'].dt.date)['ConsumptionVolume'].sum().reset_index()
   
   # Save processed data
   daily_consumption.to_sql('DailyConsumption', conn, if_exists='replace', index=False)