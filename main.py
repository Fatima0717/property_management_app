import requests
from bs4 import BeautifulSoup
import csv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the Yahoo Japan weather URL
url = 'https://weather.yahoo.co.jp/weather/jp/15/5440.html'  # Replace with a specific URL

# Request the webpage
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    logging.info("Successfully fetched the Yahoo Japan weather webpage.")
except requests.exceptions.HTTPError as err:
    logging.error(f"HTTP error occurred: {err}")
    exit()
except Exception as err:
    logging.error(f"Other error occurred: {err}")
    exit()

# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the weather information (adjust this depending on the site structure)
weather_info = soup.find_all('div', class_='forecastCity')  # Adjust to the correct class or element

# Save the data to a CSV file
try:
    with open('yahoo_weather.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Date', 'Condition', 'High Temp', 'Low Temp'])  # Adjust headers as needed

        for info in weather_info:
            # Extract desired information, modify as per the HTML structure
            date = info.find('p', class_='date').span.text.strip()
            condition = info.find('p', class_='pict').text.strip()
            high_temp = info.find('li', class_='high').em.text
            low_temp = info.find('li', class_='low').em.text

            writer.writerow([date, condition, high_temp, low_temp])  # Write to CSV

    logging.info("Weather data successfully saved to yahoo_weather.csv.")
except Exception as e:
    logging.error(f"Error while writing to CSV: {e}")
