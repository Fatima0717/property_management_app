import requests
from bs4 import BeautifulSoup
import pandas as pd

# Web Scraping Section
url = "https://keisuke-honda.com"
response = requests.get(url)

if response.status_code == 200:
    print("Page fetched successfully!")
    page_content = response.text
else:
    print("Failed to fetch the page. Status code:", response.status_code)
    exit()

soup = BeautifulSoup(page_content, "html.parser")

# This will fetch all 'a' tags to see if you are getting any results
articles = soup.find_all("a")

print(f"Found {len(articles)} links on the page.")
for article in articles[:10]:  # Print the first 10 links to inspect
    print(article)

# Replace 'article-link' with the actual class name you identified
class_name = "post-title"  # Update this with the correct class name
articles = soup.find_all("a", class_=class_name)

data = []
for article in articles:
    title = article.text.strip()
    link = article.get("href")  # Use .get() to avoid KeyError if href is missing
    if link:
        print(f"Title: {title}, Link: {link}")  # This will display the titles and links in the terminal
        data.append({"Title": title, "Link": link})

# Print the scraped data to verify
print("Scraped Data:", data)

if data:
    # Convert the list to a DataFrame
    df = pd.DataFrame(data)

    # Save
