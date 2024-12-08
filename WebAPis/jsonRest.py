import requests
import json

#Create a script to parse JSON data from a REST API response.
# URL of the REST API
url = 'https://fakestoreapi.com/products/1'

# Send a GET request to the API
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Print the parsed data
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to retrieve data: {response.status_code}")