import requests
import pandas as pd
from sqlalchemy import create_engine

def extract_csv(path)-> pd.DataFrame:
    """ load saved csv to pandas dataframe"""
    return pd.read_csv(path)

def extract_api(url:str)-> pd.DataFrame:
    """ Extract data from API"""
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)


def transform_GMMC(data:pd.DataFrame) -> pd.DataFrame:
    """ Transforms the dataset into desired structure and filters"""
    print(f"Size {data.shape}")

    df=data
    return df

def load(df:pd.DataFrame,name)-> None:
    """ Load data into an SQLite database """
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    df.to_sql(name, disk_engine, if_exists='replace')

# Given 
path= "data_storage\raw_data\GMMC_monitoring\GMMC-2020-M.csv"
total_path="..\\"+ path
name="GMMC-2020-M"
data = extract_csv(path)
df = transform_GMMC(data)
# Save to data_storage\GMMC with name GMMC-2020-M.db
load(df)



