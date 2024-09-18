from django.core.management.base import BaseCommand
from yourapp.models import Headline
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Scrapes data from a webpage and loads it into the database'

    def handle(self, *args, **kwargs):
        url = 'https://example.com'  # Replace with the actual URL
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = soup.find_all('h1')  # Adjust according to the website structure

            # Clear existing headlines if needed
            Headline.objects.all().delete()

            for headline in headlines:
                text = headline.text.strip()
                link = headline.find('a')['href'] if headline.find('a') else 'No link'
                full_link = f"https://www.example.com{link}" if link.startswith('/') else link
                Headline.objects.create(title=text, link=full_link)

            self.stdout.write(self.style.SUCCESS('Data successfully scraped and saved to the database.'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve the webpage.'))
