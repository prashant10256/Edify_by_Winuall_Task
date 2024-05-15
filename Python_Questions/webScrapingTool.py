import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the data you want to extract
        data = []
        for item in soup.find_all('div', class_='item'):
            title = item.find('h2').text.strip()
            price = item.find('span', class_='price').text.strip()
            data.append({'title': title, 'price': price})
        return data
    else:
        print("Failed to retrieve data from the website")
        return None

def save_to_csv(data, filename):
    # Specify the field names for the CSV file
    fieldnames = ['title', 'price']

    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == '__main__':
    # URL of the website to scrape
    url = 'https://example.com'

    # Scrape the website
    scraped_data = scrape_website(url)

    if scraped_data:
        # Save the scraped data to a CSV file
        save_to_csv(scraped_data, 'scraped_data.csv')
        print("Data has been scraped and saved to 'scraped_data.csv'")
    else:
        print("No data scraped")
