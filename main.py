import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from urllib.parse import urljoin

# URL and headers
base_url = 'https://www.isro.gov.in'
url = base_url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# Fetch the webpage
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with class 'accordion-body'
accordion_bodies = soup.find_all('div', class_='accordion-body')

# Extract all a tags inside the accordion-body divs
a_tags = [a_tag for body in accordion_bodies for a_tag in body.find_all('a')]

# Generate a unique filename with the current date and time
now = datetime.now()
filename = f'isro_links_{now.strftime("%Y%m%d_%H%M%S")}.csv'

# Save the data to a CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Text', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for a_tag in a_tags:
        text_content = a_tag.get_text(strip=True)
        relative_link = a_tag.get('href', '')
        # Use urljoin to create an absolute URL
        link = urljoin(base_url, relative_link)

        writer.writerow({'Text': text_content, 'Link': link})
