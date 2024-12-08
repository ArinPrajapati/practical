import requests
from bs4 import BeautifulSoup # type: ignore

#Write a Python program to scrape data from a webpage using BeautifulSoup.
# URL of the webpage to scrape
url = 'https://www.omgubuntu.co.uk/2017/11/best-gtk-themes-for-ubuntu'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the content of the request with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data from the webpage
title = soup.title.string
print(f'Title: {title}')

# Example: Extract all paragraph texts
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())