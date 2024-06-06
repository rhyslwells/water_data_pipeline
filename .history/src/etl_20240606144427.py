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

def transform_GMMC(data: pd.DataFrame) -> pd.DataFrame:
    """Transform the dataset into the desired structure and filters."""
    logging.info(f"Transforming data, initial size: {data.shape}")
    # Example transformation: adding more realistic transformations
    # This is a placeholder. Actual transformations depend on the specific needs.
    df = data
    logging.info(f"Transformed data size: {df.shape}")
    return df

def load(df: pd.DataFrame, path: str) -> None:
    """Load data into a file."""
    try:
        logging.info(f"Saving data to {path}")
        df.to_csv(path, index=False)
    except Exception as e:
        logging.error(f"Failed to save data: {e}")
        raise

def main():
    # Add command-line argument parser
    parser = argparse.ArgumentParser(description='ETL Process')
    parser.add_argument('--path', type=str, help='Path to the CSV file')
    parser.add_argument('--name', type=str, help='Name of the dataset')
    args = parser.parse_args()

    # Example path to CSV file
    path = args.path
    name = args.name

    # Current path: src/etl.py
    try:
        data = extract_csv(path)
        df = transform_GMMC(data)
        # Save to specified path with given name
        save_path = os.path.join('data_storage', name, 'processed_data', f'{name}.csv')
        load(df, save_path)
        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()
