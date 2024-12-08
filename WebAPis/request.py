import requests

def make_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    url = "https://fakestoreapi.com/products"  # Replace with your target URL
    data = make_get_request(url)
    if data:
        print(data)