import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')


        with open('products_info.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Rating"])

            products = soup.find_all("div", class_="product-item")
            for product in products:
                name = product.find("h2", class_="product-name").text.strip()
                price = product.find("span", class_="product-price").text.strip()
                rating = product.find("div", class_="product-rating").text.strip()

                writer.writerow([name, price, rating])
        
        print("Product information extracted and stored in 'products_info.csv'.")
    else:
        print("Failed to fetch the page. Status code:", response.status_code)

# Replace this URL with the actual e-commerce site you want to scrape
ecommerce_url = "https://example.com/products"  # Replace with the actual URL

scrape_product_info(ecommerce_url)


