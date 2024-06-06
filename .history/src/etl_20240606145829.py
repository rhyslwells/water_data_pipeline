import argparse
import requests
import pandas as pd
from sqlalchemy import create_engine
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_csv(path: str) -> pd.DataFrame:
    """Load saved CSV to pandas dataframe."""
    try:
        logging.info(f"Extracting data from CSV at {path}")
        return pd.read_csv(path)
    except Exception as e:
        logging.error(f"Failed to extract CSV: {e}")
        raise

def load(df: pd.DataFrame, name: str,folder_name:str) -> None:
    # Load will be depednat on the user input.

    """Load data into an SQLite database."""
    try:
        #The line below needs to change
        db_path = os.path.join('data_storage', folder_name, 'processed_data', f'{name}.db')
        logging.info(f"Loading data into SQLite database at {db_path}")
        disk_engine = create_engine(f'sqlite:///{db_path}')
        df.to_sql(name, disk_engine, if_exists='replace', index=False)
    except Exception as e:
        logging.error(f"Failed to load data into SQLite: {e}")
        raise

# The following functions will be different for each folder_name

def transform_GMMC(data: pd.DataFrame) -> pd.DataFrame:
    """Transform the dataset into the desired structure and filters."""
    logging.info(f"Transforming data, initial size: {data.shape}")
    # Example transformation: adding more realistic transformations
    # This is a placeholder. Actual transformations depend on the specific needs.
    df = data
    logging.info(f"Transformed data size: {df.shape}")
    return df

def transform_septic_tanks_scotland(data: pd.DataFrame) -> pd.DataFrame:
    """Transform the dataset into the desired structure and filters."""
    logging.info(f"Transforming data, initial size: {data.shape}")
    # Example transformation: adding more realistic transformations
    # This is a placeholder. Actual transformations depend on the specific needs.
    df = data
    logging.info(f"Transformed data size: {df.shape}")
    return df

def contaiminated_land_scotland(data: pd.DataFrame) -> pd.DataFrame:
    """Transform the dataset into the desired structure and filters."""
    logging.info(f"Transforming data, initial size: {data.shape}")
    # Example transformation: adding more realistic transformations
    # This is a placeholder. Actual transformations depend on the specific needs.
    df = data
    logging.info(f"Transformed data size: {df.shape}")
    return df


def main():
    # Add command-line argument parser
    parser = argparse.ArgumentParser(description='ETL Process')
    parser.add_argument('--path', type=str, help='Path to the CSV file')
    parser.add_argument('--name', type=str, help='Name of the dataset')
    parser.add_argument('--folder_name', type=str, help='Name of the folder to save the data')
    args = parser.parse_args()

    # Example path to CSV file
    path = args.path
    name = args.name
    folder_name = args.folder_name

    try:
        data = extract_csv(path)
        if folder_name == 'GMMC':
            df = transform_GMMC(data)
            load(df, name, folder_name)
            logging.info("ETL process completed successfully")
        else:
            logging.error(f"1 No transformations defined for folder {folder_name}. Skipping ETL process.")
        if folder_name == 'septic_tanks_scotland':
            df = transform_septic_tanks_scotland(data)
            load(df, name, folder_name)
            logging.info("ETL process completed successfully")
        else:
            logging.error(f"2 No transformations defined for folder {folder_name}. Skipping ETL process.")    
        if folder_name == 'contaiminated_land_scotland':
            df = contaiminated_land_scotland(data)
            load(df, name, folder_name)
            logging.info("ETL process completed successfully")
        else:
            logging.error(f"3 No transformations defined for folder {folder_name}. Skipping ETL process.")
        
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()

# provide examples of how to run the script
# python src/etl.py --path data_storage/GMMC/raw_data/GMMC-2020-M.csv --name GMMC-2020-M --folder_name GMMC
# python src/etl.py --path data_storage\septic_tanks_scotland\raw_data\Septic_Tanks_-_Scotland.csv --name septic_tanks_scotland --folder_name septic_tanks_scotland
