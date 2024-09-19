import requests
from bs4 import BeautifulSoup
import csv

def fetch_data(url):
    """Fetches data from the given URL.
    
    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        bytes: The content of the webpage if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.content
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None

def parse_data(content):
    """Parses the webpage content and extracts headlines.
    
    Args:
        content (bytes): The HTML content of the webpage.

    Returns:
        list: A list of BeautifulSoup elements containing the headlines.
    """
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find_all('h1')

def save_data(headlines):
    """Saves the extracted headlines to a CSV file.
    
    Args:
        headlines (list): A list of BeautifulSoup elements containing the headlines.
    """
    if not headlines:
        print("No headlines found on the page.")
        return

    with open('scraped_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])
        for headline in headlines:
            writer.writerow([headline.text.strip()])  # Strip leading/trailing whitespace
    print("Data successfully scraped and saved to 'scraped_data.csv'.")

def scrape_data():
    """Main function to scrape data from a webpage.
    
    The function fetches data from the URL, parses it to extract headlines, and saves the results to a CSV file.
    """
    print("Starting scrape...")
    url = 'https://example.com'  # Replace with the actual URL you want to scrape
    content = fetch_data(url)

    if content:
        headlines = parse_data(content)
        print(f"Found {len(headlines)} headlines")
        save_data(headlines)

if __name__ == "__main__":
    scrape_data()
