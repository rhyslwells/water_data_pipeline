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

    def get_monitoring_data(self, area=None, year=None, limit=None):
        url = f"{self.base_url}/data/measurement"
        params = {
            "area": area,
            "year": year,
            "_limit": limit
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_compliance_data(self, area=None, year=None, limit=None):
        url = f"{self.base_url}/data/sample"
        params = {
            "area": area,
            "year": year,
            "_limit": limit
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_measurements(self, lat=None, long=None, dist=None, easting=None, northing=None, area=None, sub_area=None, year=None, start_date=None, end_date=None, is_compliance_sample=None, purpose=None, sampling_point=None, sampling_point_type=None, determinand=None, determinand_group=None, limit=None, sorted_=None):
        url = f"{self.base_url}/data/measurement"
        params = {
            "lat": lat,
            "long": long,
            "dist": dist,
            "easting": easting,
            "northing": northing,
            "area": area,
            "subArea": sub_area,
            "year": year,
            "startDate": start_date,
            "endDate": end_date,
            "isComplianceSample": is_compliance_sample,
            "purpose": purpose,
            "samplingPoint": sampling_point,
            "samplingPointType": sampling_point_type,
            "determinand": determinand,
            "determinandGroup": determinand_group,
            "_limit": limit,
            "_sorted": sorted_
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def save_to_csv(data, filename):
        headers = [
            "@id", "sample.samplingPoint", "sample.samplingPoint.notation", "sample.samplingPoint.label",
            "sample.sampleDateTime", "determinand.label", "determinand.definition", "determinand.notation",
            "resultQualifier.notation", "result", "codedResultInterpretation.interpretation", "determinand.unit.label",
            "sample.sampledMaterialType.label", "sample.isComplianceSample", "sample.purpose.label",
            "sample.samplingPoint.easting", "sample.samplingPoint.northing"
        ]
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for entry in data:
                row = {
                    "@id": entry.get("@id"),
                    "sample.samplingPoint": entry.get("sample", {}).get("samplingPoint", {}).get("@id"),
                    "sample.samplingPoint.notation": entry.get("sample", {}).get("samplingPoint", {}).get("notation"),
                    "sample.samplingPoint.label": entry.get("sample", {}).get("samplingPoint", {}).get("label"),
                    "sample.sampleDateTime": entry.get("sample", {}).get("sampleDateTime"),
                    "determinand.label": entry.get("determinand", {}).get("label"),
                    "determinand.definition": entry.get("determinand", {}).get("definition"),
                    "determinand.notation": entry.get("determinand", {}).get("notation"),
                    "resultQualifier.notation": entry.get("resultQualifier", {}).get("notation"),
                    "result": entry.get("result"),
                    "codedResultInterpretation.interpretation": entry.get("codedResultInterpretation", {}).get("interpretation"),
                    "determinand.unit.label": entry.get("determinand", {}).get("unit", {}).get("label"),
                    "sample.sampledMaterialType.label": entry.get("sample", {}).get("sampledMaterialType", {}).get("label"),
                    "sample.isComplianceSample": entry.get("sample", {}).get("isComplianceSample"),
                    "sample.purpose.label": entry.get("sample", {}).get("purpose", {}).get("label"),
                    "sample.samplingPoint.easting": entry.get("sample", {}).get("samplingPoint", {}).get("easting"),
                    "sample.samplingPoint.northing": entry.get("sample", {}).get("samplingPoint", {}).get("northing")
                }
                writer.writerow(row)


if __name__ == "__main__":
    api = WaterQualityAPI()

    try:
        # Get list of sampling points
        sampling_points_data = api.list_sampling_points()
        print("List of Sampling Points:", sampling_points_data)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


"""
# I want to use the Water Quality API to retrieve water quality data for Greater Manchester, Merseyside, and Cheshire 
# for the year 2020 . Specifically, I will collect monitoring data and measurements data for these areas and for that year.

# The retrieved data will be printed to the console for each area and data type. Additionally, I want to store
#     this data in a CSV file. The CSV file will have the following headers of the downloadable csv file: 
# from https://environment.data.gov.uk/water-quality/view/download/new

if __name__ == "__main__":
    api = WaterQualityAPI()

    # Define the areas of interest and year
    # areas = ["Greater Manchester", "Merseyside", "Cheshire"]
    areas = ["Greater Manchester"]
    year = 2020
    all_data = []

    # Example usage
    try:
        # Get monitoring data for the specified areas and year
        for area in areas:
            monitoring_data = api.get_monitoring_data(area=area, year=year, limit=50)  # Adjust limit as needed
            all_data.extend(monitoring_data.get('items', []))


        # Get measurements data for the specified areas and year
        for area in areas:
            measurements_data = api.get_measurements(area=area, year=year, limit=50)  # Adjust limit as needed
            all_data.extend(measurements_data.get('items', []))

        # Save all data to CSV
        save_to_csv(all_data, 'water_quality_data.csv')
        print("Data saved to water_quality_data.csv")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")"""