import requests
from bs4 import BeautifulSoup

product_names = []
product_data = []

url = "https://graysonmotorsports.com/product-category/wheels-tires/full-sets/single-wheel/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

# Find elements with class "woocommerce-loop-product__title"
names_elements = soup.find_all("h2", class_="woocommerce-loop-product__title")

# Extract product names from the found elements
# for element in names_elements:
#     product_name = element.get_text(strip=True)
#     product_names.append(product_name)

# # Print or use the extracted product names
# print(product_names)

prices_elements = soup.find_all("span", class_="price")

# Extract product names and prices from the found elements
for name_element, price_element in zip(names_elements, prices_elements):
    product_name = name_element.get_text(strip=True)
    product_price = price_element.get_text(strip=True)
    product_data.append({"name": product_name, "price": product_price})

# Print or use the extracted product data
for product in product_data:
    print(f"Name: {product['name']}, Price: {product['price']}")