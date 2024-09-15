import requests
from bs4 import BeautifulSoup
import csv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define URL
url = 'https://www.bbc.com/news'

# Request the webpage
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    logging.info("Successfully fetched the webpage.")
except requests.exceptions.HTTPError as err:
    logging.error(f"HTTP error occurred: {err}")
    exit()
except Exception as err:
    logging.error(f"Other error occurred: {err}")
    exit()

# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the headlines
headlines = soup.find_all('h3')  # Modify this depending on the website structure

# Save the data to a CSV file
with open('bbc_headlines.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Headline', 'URL'])  # Write headers for CSV

    for headline in headlines:
        text = headline.text.strip()  # Clean the text
        link = headline.find('a')['href'] if headline.find('a') else 'No link'
        full_link = f"https://www.bbc.com{link}" if link.startswith('/') else link
        
        # Write to CSV
        writer.writerow([text, full_link])

logging.info("Data successfully saved to bbc_headlines.csv.")
