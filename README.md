``` text
Please find the correct version @ :https://github.com/Shri10/ISRO_LatestNews_Scraper
This is only development version
```

# ISRO Links Scraper

This Python script scrapes the ISRO website (https://www.isro.gov.in) and extracts links inside div elements with the class 'accordion-body'. The extracted data is saved in a CSV file with a unique filename, including the current date and time.

## Requirements

- Python 3.x
- `beautifulsoup4`
- `requests`

## Installation

1. Install the required Python libraries:

```bash
pip install beautifulsoup4 requests
```

## Usage

1. Save the provided script as `isro_links_scraper.py`.
2. Run the script:

```bash
python isro_links_scraper.py
```

The script will fetch the webpage, parse the HTML content, find all div elements with the class 'accordion-body', and extract the a tags inside these divs. It will then generate a unique CSV filename with the current date and time and save the extracted data in the file. The resulting CSV file will contain two columns: 'Text' and 'Link', containing the text content and the absolute link, respectively.

## Output

The script generates a CSV file with the following format:

```
Text,Link
Text content 1,https://www.isro.gov.in/link1
Text content 2,https://www.isro.gov.in/link2
...
```

The filename will have the format `isro_links_YYYYMMDD_HHMMSS.csv`, where `YYYYMMDD` is the current date and `HHMMSS` is the current time.