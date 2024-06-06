import requests

BASE_URL = "http://environment.data.gov.uk/water-quality"

class WaterQualityAPI:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_dates_modified(self, limit=None):
        url = f"{self.base_url}/data/modified"
        params = {"_limit": limit} if limit else {}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_dates_rebuilt(self):
        url = f"{self.base_url}/data/rebuilt"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def list_sampling_points(self, search=None, lat=None, long=None, dist=None, easting=None, northing=None, area=None, sub_area=None, sampling_point_type=None, sampling_point_status=None):
        url = f"{self.base_url}/id/sampling-point"
        params = {
            "search": search,
            "lat": lat,
            "long": long,
            "dist": dist,
            "easting": easting,
            "northing": northing,
            "area": area,
            "subArea": sub_area,
            "samplingPointType": sampling_point_type,
            "samplingPointStatus": sampling_point_status
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_sampling_point_details(self, sampling_point_id):
        url = f"{self.base_url}/id/sampling-point/{sampling_point_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    api = WaterQualityAPI()

    # Example usage
    try:
        # Get the dates the data has been modified
        modified_dates = api.get_dates_modified(limit=1)
        print("Modified Dates:", modified_dates)

        # Get the date the data has been rebuilt
        rebuilt_date = api.get_dates_rebuilt()
        print("Rebuilt Date:", rebuilt_date)

        # List sampling points with search term "clifton"
        sampling_points = api.list_sampling_points(search="clifton")
        print("Sampling Points:", sampling_points)

        # Get details for a specific sampling point
        sampling_point_id = "AN-WOODTON"
        sampling_point_details = api.get_sampling_point_details(sampling_point_id)
        print("Sampling Point Details:", sampling_point_details)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
