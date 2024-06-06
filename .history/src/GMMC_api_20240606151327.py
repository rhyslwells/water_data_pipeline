import requests

# Base URL for the Water Quality Archive API
base_url = "http://environment.data.gov.uk/water-quality"

# Function to list sampling points
def list_sampling_points():
    url = f"{base_url}/id/sampling-point"
    response = requests.get(url)
    if response.status_code == 200:
        sampling_points = response.json()
        for sampling_point in sampling_points["items"]:
            print(f"Sampling Point: {sampling_point['label']}")
            print(f"Area: {sampling_point['area']['label']}")
            print(f"Comment: {sampling_point['comment']}")
            print("-----")
    else:
        print("Failed to retrieve sampling points")

# Function to get details of a specific sampling point
def get_sampling_point_details(sampling_point_id):
    url = f"{base_url}/id/sampling-point/{sampling_point_id}"
    response = requests.get(url)
    if response.status_code == 200:
        sampling_point_details = response.json()
        print("Sampling Point Details:")
        print(f"Label: {sampling_point_details['label']}")
        print(f"Area: {sampling_point_details['area']['label']}")
        print(f"Comment: {sampling_point_details['comment']}")
        print(f"Latitude: {sampling_point_details['lat']}")
        print(f"Longitude: {sampling_point_details['long']}")
        print("-----")
    else:
        print("Failed to retrieve sampling point details")

# Example usage
if __name__ == "__main__":
    # List sampling points
    print("Sampling Points:")
    list_sampling_points()

    # Get details of a specific sampling point
    sampling_point_id = "AN-WOODTON"  # Replace with the ID of the sampling point you want to retrieve details for
    print(f"Retrieving details for sampling point {sampling_point_id}:")
    get_sampling_point_details(sampling_point_id)
