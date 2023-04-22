import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL and headers
url = 'https://www.isro.gov.in'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# Fetch the webpage
response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements with class attributes
elements_with_classes = soup.find_all(lambda tag: tag.has_attr('class'))

# Generate a unique filename with the current date and time
now = datetime.now()
filename = f'isro_elements_{now.strftime("%Y%m%d_%H%M%S")}.csv'

# Save the data to a CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Tag', 'Class', 'Text', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for element in elements_with_classes:
        tag_name = element.name
        class_names = ' '.join(element['class'])
        text_content = element.get_text(strip=True)
        link = element.get('href') if element.has_attr('href') else ''

        writer.writerow({'Tag': tag_name, 'Class': class_names, 'Text': text_content, 'Link': link})
