






import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazon_products(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

    with open('amazon_products.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Rating"])

            products = soup.find_all("div", class_="a-section a-spacing-none p13n-asin")
            for product in products:
                name = product.find("span", class_="zg-text-center-align").text.strip()
                price = product.find("span", class_="p13n-sc-price").text.strip()
                rating = product.find("span", class_="a-icon-alt").text.strip()

                writer.writerow([name, price, rating])
        
        print("Product information extracted and stored in 'amazon_products.csv'.")
    else:
        print("Failed to fetch the page. Status code:", response.status_code)

   # Amazon Best Sellers in Electronics URL
amazon_url = "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"

scrape_amazon_products(amazon_url)
