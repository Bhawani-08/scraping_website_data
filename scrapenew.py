import requests
from bs4 import BeautifulSoup
import csv

def extract_image_link(container):
    image_container = container.find("img", class_="product-image-photo")
    if image_container:
        return image_container["src"]
    else:
        return None

page_urls = [
    "https://www.kjmotorsports.com/utv/body/cargo-boxes-and-storage"
    "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/doors"
    "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/door-bags"
    "https://www.kjmotorsports.com/utv/body/fuel-packs-mounts",
    "https://www.kjmotorsports.com/utv/body/gas-caps",
    "https://www.kjmotorsports.com/utv/body/grilles",
    "https://www.kjmotorsports.com/utv/body/roofs",
    "https://www.kjmotorsports.com/utv/body/seats-and-harnesses",
    "https://www.kjmotorsports.com/utv/body/windshields",
    "https://www.kjmotorsports.com/utv/body/windshields?p=2",
    "https://www.kjmotorsports.com/utv/body/windshields?p=3",
    "https://www.kjmotorsports.com/utv/body/windshields?p=4"
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=2",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=3",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/full-sets",
    "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
    "https://www.kjmotorsports.com/utv/drivetrain/clutching",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=3",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=4"
    "https://www.kjmotorsports.com/utv/electrical/batteries-accessories/batteries",
    "https://www.kjmotorsports.com/utv/electrical/batteries-accessories/battery-accessories",
    "https://www.kjmotorsports.com/utv/electrical/horns",
    "https://www.kjmotorsports.com/utv/electrical/lighting/headlight-bulbs?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=3&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=4&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/lighting/lighted-whips?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/lighting/lighted-whips?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/lighting/mounts-clamps",
    "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=3&product_list_limit=32"
    "https://www.kjmotorsports.com/utv/electrical/sound-systems?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winches?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winches?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-mounts?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-mounts?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=3&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=4&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/exhaust-systems-and-parts/slip-on-exhausts?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=2",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=3",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=4",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=5",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=6",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=7",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=8",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=9",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=10",
    "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=6&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/bumpers?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/bumpers?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/cages",
    "https://www.kjmotorsports.com/utv/frame-chassis/nerf-bars",
    "https://www.kjmotorsports.com/utv/frame-chassis/power-steering-kits",
    "https://www.kjmotorsports.com/utv/frame-chassis/rack-and-pinion",
    "https://www.kjmotorsports.com/utv/frame-chassis/skid-plates-guards",
    "https://www.kjmotorsports.com/utv/frame-chassis/suspension?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/suspension?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/suspension?p=3&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods",
    "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods?p=2",
    "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods?p=3",
    "https://www.kjmotorsports.com/utv/intake-fuel",
    "https://www.kjmotorsports.com/utv/interior/bags-storage",
    "https://www.kjmotorsports.com/utv/interior/dash-accessories/dash-accessories/rocker-switches",
    "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
    "https://www.kjmotorsports.com/utv/drivetrain/clutching",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/grab-bars-handles",
    "https://www.kjmotorsports.com/utv/interior/mirrors/rear-view-mirrors?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mirrors/rear-view-mirrors?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?p=3&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/clamps",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/fire-extinguisher-mounts",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/go-pro-camera-mounts",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?p=3&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/universal-mounts",
    "https://www.kjmotorsports.com/utv/interior/shift-knobs-levers?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/smartphone-tablet-accessories?product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/smartphone-tablet-accessories?p=2&product_list_limit=32",
    "https://www.kjmotorsports.com/utv/interior/steering-wheels",
    "https://www.kjmotorsports.com/utv/outdoor-gear/coolers",
    "https://www.kjmotorsports.com/utv/outdoor-gear/drinkware",
    "https://www.kjmotorsports.com/atv/snow-plows-accessories/snow-plows",
    "https://www.kjmotorsports.com/atv/snow-plows-accessories/plow-mounts",
    "https://www.kjmotorsports.com/atv/snow-plows-accessories/plow-accessories",
    "https://www.kjmotorsports.com/atv/snow-plows-accessories/winches-accessories",
    "https://www.kjmotorsports.com/utv/tires/single",
    "https://www.kjmotorsports.com/utv/tires/pairs",
    "https://www.kjmotorsports.com/utv/tires/full-sets",
    "https://www.kjmotorsports.com/utv/wheels/single",
    "https://www.kjmotorsports.com/utv/wheels/wheel-accessories",
    "https://www.kjmotorsports.com/utv/winches-accessories/winches",
    "https://www.kjmotorsports.com/utv/winches-accessories/winch-mounts",
    "https://www.kjmotorsports.com/utv/winches-accessories/winch-accessories",

]

all_data = []
fieldnames = ["name", "price", "SKU", "image"]

for url in page_urls:
    product_data1 = []

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    product_containers = soup.find_all("div", class_="product-item-info")

    for container in product_containers:
        product_name = container.find("a", class_="product-item-link").get_text(strip=True)
        product_price = container.find("span", class_="price").get_text(strip=True)
        product_sku = container.find("div", class_="cat-sku").get_text(strip=True)

        # Define the extract_image_link function here
        def extract_image_link(container):
            image_container = container.find("img", class_="product-image-photo")
            if image_container:
                return image_container["src"]
            else:
                return None

        product_image = extract_image_link(container)

        product_data1.append({
            "name": product_name,
            "price": product_price,
            "SKU": product_sku,
            "image": product_image
        })

    all_data += product_data1

csv_file_path = "/home/lenovo/Desktop/product_data1.csv"

try:
    with open(csv_file_path, mode='r') as existing_file:
        existing_data = list(csv.DictReader(existing_file))
except FileNotFoundError:
    existing_data = []

all_data = existing_data + all_data

with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for product in all_data:
        writer.writerow(product)

print(f"Data has been saved to {csv_file_path}")
