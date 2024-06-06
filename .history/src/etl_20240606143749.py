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

def extract_api(url: str) -> pd.DataFrame:
    """Extract data from API."""
    try:
        logging.info(f"Extracting data from API at {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        raise

def transform_GMMC(data: pd.DataFrame) -> pd.DataFrame:
    """Transform the dataset into the desired structure and filters."""
    logging.info(f"Transforming data, initial size: {data.shape}")
    # Example transformation: adding more realistic transformations
    # This is a placeholder. Actual transformations depend on the specific needs.
    df = data
    logging.info(f"Transformed data size: {df.shape}")
    return df

def load_GMMC(df: pd.DataFrame, name: str) -> None:
    """Load data into an SQLite database."""
    try:
        db_path = os.path.join('data_storage', 'contaminated_land_scotland', 'processed_data', f'{name}.db')
        logging.info(f"Loading data into SQLite database at {db_path}")
        disk_engine = create_engine(f'sqlite:///{db_path}')
        df.to_sql(name, disk_engine, if_exists='replace', index=False)
    except Exception as e:
        logging.error(f"Failed to load data into SQLite: {e}")
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
        # Save to data_storage/GMMC with name GMMC-2020-M.db
        load_GMMC(df, name)
        logging.info("ETL process completed successfully")
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()

# provide examples of how to run the script
# python src/etl.py --path data_storage/contaminated_land_scotland/raw_data/contaminated_land_scotland.csv --name contaminated_land_scotland
# python src/etl.py --path data_storage/GMMC/raw_data/GMMC-2020-M.csv --name GMMC-2020-M
# python src/etl.py --path data_storage/septic_tanks/raw_data/septic_tanks.csv --name septic_tanks