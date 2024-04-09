import requests
from bs4 import BeautifulSoup
import csv
import os

# Sitemap URL of the website
sitemap_url = "https://www.kjmotorsports.com/sitemap.xml"

# Fetch the sitemap content
sitemap_response = requests.get(sitemap_url)
sitemap_soup = BeautifulSoup(sitemap_response.text, "xml")

# Extract URLs from the sitemap
page_urls = [loc.text for loc in sitemap_soup.find_all("loc")]

# List to store all the product data
all_data = []

# Common fieldnames for the CSV file
fieldnames = ["name", "price", "SKU"]

# ...

for url in page_urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    product_containers = soup.find_all("div", class_="product-item-info")

    if not product_containers:
        print(f"No product containers found for URL: {url}")
        continue

    for container in product_containers:
        product_name_elem = container.find("a", class_="product-item-link")
        product_price_elem = container.find("span", class_="price")
        product_sku_elem = container.find("div", class_="cat-sku")

        if not product_name_elem or not product_price_elem or not product_sku_elem:
            print(f"Skipping incomplete product information for URL: {url}")
            continue

        product_name = product_name_elem.get_text(strip=True)
        product_price = product_price_elem.get_text(strip=True)
        product_sku = product_sku_elem.get_text(strip=True)

        all_data.append({"name": product_name, "price": product_price, "SKU": product_sku})

# ...

# Path to the CSV file
csv_file_path = "/home/lenovo/Desktop/pd1.csv"

# ...

# Check if the CSV file already exists
if os.path.isfile(csv_file_path):
    with open(csv_file_path, mode='r') as existing_file:
        existing_data = list(csv.DictReader(existing_file))

    print(f"Existing data loaded from {csv_file_path}. Total rows: {len(existing_data)}")
    if existing_data:
        for row in existing_data:
            print(row)
    else:
        print("Existing file is empty.")

    all_data += existing_data
else:
    existing_data = []
    print("No existing data found.")

# ...


with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for product in all_data:
        writer.writerow(product)

print(f"Total rows after writing to CSV: {len(all_data)}")

print(f"Data has been saved to {csv_file_path}")
