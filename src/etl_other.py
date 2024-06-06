# def extract_api(url: str) -> pd.DataFrame:
#     """Extract data from API."""
#     try:
#         logging.info(f"Extracting data from API at {url}")
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         return pd.DataFrame(data)
#     except requests.RequestException as e:
#         logging.error(f"API request failed: {e}")
#         raise