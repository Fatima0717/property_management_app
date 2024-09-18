import requests
from bs4 import BeautifulSoup
import csv

def scrape_data():
    # Replace with the website you want to scrape
    url = 'https://example.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Adjust the tag and class to match the structure of the page you are scraping
        headlines = soup.find_all('h1')  # For example, scraping headlines

        # Create and open a CSV file to save the scraped data
        with open('scraped_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Headline'])

            for headline in headlines:
                writer.writerow([headline.text])

        print("Data successfully scraped and saved to 'scraped_data.csv'.")
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    scrape_data()
