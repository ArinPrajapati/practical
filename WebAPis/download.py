import requests

# Create a program to download a file from a URL using Python.
def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# Example usage
url = 'https://getsamplefiles.com/download/zip/sample-1.zip'
local_filename = 'WebAPis/files.zip'
download_file(url, local_filename)