# web_scraping_analysis.py

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

# Parse the HTML content
soup = BeautifulSoup(page_content, "html.parser")

# Replace 'actual-class-name' with the correct class name found from the website
articles = soup.find_all("a", class_="actual-class-name")  

# Extract and store the data
data = []
for article in articles:
    title = article.text.strip()  # Extract title and remove whitespace
    link = article["href"]  # Extract the link
    data.append({"Title": title, "Link": link})  # Append data to the list

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('scraped_data.csv', index=False)
print("Data saved to 'scraped_data.csv'")

# Data Analysis Section
df = pd.read_csv('scraped_data.csv')

# Print the first few rows of the DataFrame
print(df.head())

# Display information about the DataFrame
print(df.info())

# Show basic statistics
print(df.describe())

# Count unique titles
print(df['Title'].value_counts())

# Filter rows containing a specific keyword in the title
keyword = "Honda"
filtered_df = df[df['Title'].str.contains(keyword, case=False)]
print(filtered_df)
