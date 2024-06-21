import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.iqoo.com/in"
response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')
    unique_links = set()  # Use a set to store unique links

    print("Links:")
    for link in links:
        href = link.get('href')
        if href and href.startswith(('http', '/')):  # Ensure it's a proper URL
            full_url = urljoin(base_url, href)
            if full_url not in unique_links:  # Check if the link is already processed
                unique_links.add(full_url)  # Add the link to the set of unique links
                print(full_url)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")