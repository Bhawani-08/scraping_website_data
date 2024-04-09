# # import requests
# # from bs4 import BeautifulSoup
# # import csv

# # # List of URLs for different pages
# # page_urls = [
# #     "https://www.kjmotorsports.com/utv/body/cargo-boxes-and-storage"
# #     "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/doors"
# #     "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/door-bags"
# #     "https://www.kjmotorsports.com/utv/body/fuel-packs-mounts",
# #     "https://www.kjmotorsports.com/utv/body/gas-caps",
# #     "https://www.kjmotorsports.com/utv/body/grilles",
# #     "https://www.kjmotorsports.com/utv/body/roofs",
# #     "https://www.kjmotorsports.com/utv/body/seats-and-harnesses",
# #     "https://www.kjmotorsports.com/utv/body/windshields",
# #     "https://www.kjmotorsports.com/utv/body/windshields?p=2",
# #     "https://www.kjmotorsports.com/utv/body/windshields?p=3",
# #     "https://www.kjmotorsports.com/utv/body/windshields?p=4"
# #     "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single",
# #     "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=2",
# #     "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=3",
# #     "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/full-sets",
# #     "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
# #     "https://www.kjmotorsports.com/utv/drivetrain/clutching",
# #     "https://www.kjmotorsports.com/utv/drivetrain/drive-belts",
# #     "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2",
# #     "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=3",
# #     "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=4"
# #     "https://www.kjmotorsports.com/utv/electrical/batteries-accessories/batteries",
# #     "https://www.kjmotorsports.com/utv/electrical/batteries-accessories/battery-accessories",
# #     "https://www.kjmotorsports.com/utv/electrical/horns",
# #     "https://www.kjmotorsports.com/utv/electrical/lighting/headlight-bulbs?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=3&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=4&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/lighting/lighted-whips?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/lighting/lighted-whips?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/lighting/mounts-clamps",
# #     "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=3&product_list_limit=32"
# #     "https://www.kjmotorsports.com/utv/electrical/sound-systems?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winches?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winches?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-mounts?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-mounts?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=3&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=4&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/exhaust-systems-and-parts/slip-on-exhausts?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=2",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=3",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=4",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=5",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=6",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=7",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=8",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=9",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=10",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=6&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/bumpers?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/bumpers?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/cages",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/nerf-bars",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/power-steering-kits",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/rack-and-pinion",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/skid-plates-guards",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/suspension?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/suspension?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/suspension?p=3&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods?p=2",
# #     "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods?p=3",
# #     "https://www.kjmotorsports.com/utv/intake-fuel",
# #     "https://www.kjmotorsports.com/utv/interior/bags-storage",
# #     "https://www.kjmotorsports.com/utv/interior/dash-accessories/dash-accessories/rocker-switches",
# #     "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
# #     "https://www.kjmotorsports.com/utv/drivetrain/clutching",
# #     "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/grab-bars-handles",
# #     "https://www.kjmotorsports.com/utv/interior/mirrors/rear-view-mirrors?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mirrors/rear-view-mirrors?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?p=3&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/clamps",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/fire-extinguisher-mounts",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/go-pro-camera-mounts",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?p=3&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/universal-mounts",
# #     "https://www.kjmotorsports.com/utv/interior/shift-knobs-levers?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/smartphone-tablet-accessories?product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/smartphone-tablet-accessories?p=2&product_list_limit=32",
# #     "https://www.kjmotorsports.com/utv/interior/steering-wheels",
# #     "https://www.kjmotorsports.com/utv/outdoor-gear/coolers",
# #     "https://www.kjmotorsports.com/utv/outdoor-gear/drinkware",
# #     "https://www.kjmotorsports.com/atv/snow-plows-accessories/snow-plows",
# #     "https://www.kjmotorsports.com/atv/snow-plows-accessories/plow-mounts",
# #     "https://www.kjmotorsports.com/atv/snow-plows-accessories/plow-accessories",
# #     "https://www.kjmotorsports.com/atv/snow-plows-accessories/winches-accessories",
# #     "https://www.kjmotorsports.com/utv/tires/single",
# #     "https://www.kjmotorsports.com/utv/tires/pairs",
# #     "https://www.kjmotorsports.com/utv/tires/full-sets",
# #     "https://www.kjmotorsports.com/utv/wheels/single",
# #     "https://www.kjmotorsports.com/utv/wheels/wheel-accessories",
# #     "https://www.kjmotorsports.com/utv/winches-accessories/winches",
# #     "https://www.kjmotorsports.com/utv/winches-accessories/winch-mounts",
# #     "https://www.kjmotorsports.com/utv/winches-accessories/winch-accessories"
# # ]


# # all_data = []


# # fieldnames = ["name", "price", "SKU","images"]

# # # Function to filter data based on price 
# # def filter_data(data, min_price, max_price):
# #     filtered_data = []

# #     for item in data:
        
# #         item_price_str = ''.join(c for c in item['price'] if c.isdigit() or c == '.')
        
# #         try:
# #             item_price = float(item_price_str)
# #         except ValueError:
            
# #             print(f"Skipping item due to invalid price: {item['name']} - {item['price']}")
# #             continue

# #         if min_price <= item_price <= max_price:
# #             filtered_data.append(item)

# #     return filtered_data



# # for url in page_urls:
    
# #     current_page_data = []

# #     r = requests.get(url)
# #     soup = BeautifulSoup(r.text, "lxml")

# #     product_containers = soup.find_all("div", class_="product-item-info")

# #     for container in product_containers:
# #         product_name = container.find("a", class_="product-item-link").get_text(strip=True)
# #         product_price = container.find("span", class_="price").get_text(strip=True)
# #         product_sku = container.find("div", class_="cat-sku").get_text(strip=True)

# #         current_page_data.append({"name": product_name, "price": product_price, "SKU": product_sku})


# #     all_data += current_page_data


# # previous_csv_file_path = "/home/lenovo/Desktop/filtered_data1.csv"


# # try:
# #     with open(previous_csv_file_path, mode='r') as previous_file:
# #         previous_data = list(csv.DictReader(previous_file))
# # except FileNotFoundError:
# #     previous_data = []

# # all_data = previous_data + all_data

# # min_price = 0.0
# # max_price = 100.0
# # filtered_data = filter_data(all_data, min_price, max_price)

# # filtered_data.sort(key=lambda x: float(''.join(c for c in x['price'] if c.isdigit() or c == '.')))


# # filtered_csv_file_path = "/home/lenovo/Desktop/filtered_data1.csv"


# # with open(filtered_csv_file_path, mode='w', newline='') as filtered_csv_file:
# #     writer = csv.DictWriter(filtered_csv_file, fieldnames=fieldnames)
# #     writer.writeheader()
# #     for product in filtered_data:
# #         writer.writerow(product)

# # print(f"Filtered and sorted data has been saved to {filtered_csv_file_path}")



# import requests
# from bs4 import BeautifulSoup
# import csv

# # List of URLs for different pages
# page_urls = [
    # "https://www.kjmotorsports.com/utv/body/cargo-boxes-and-storage",
    # "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/doors",
    # "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/door-bags",
    # "https://www.kjmotorsports.com/utv/body/fuel-packs-mounts",
    # "https://www.kjmotorsports.com/utv/body/gas-caps",
    # "https://www.kjmotorsports.com/utv/body/grilles",
    # "https://www.kjmotorsports.com/utv/body/roofs",
    # "https://www.kjmotorsports.com/utv/body/seats-and-harnesses",
    # "https://www.kjmotorsports.com/utv/body/windshields",
    # "https://www.kjmotorsports.com/utv/body/windshields?p=2",
    # "https://www.kjmotorsports.com/utv/body/windshields?p=3",
    # "https://www.kjmotorsports.com/utv/body/windshields?p=4",
    # "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single",
    # "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=2",
    # "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=3",
    # "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/full-sets",
    # "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
    # "https://www.kjmotorsports.com/utv/drivetrain/clutching",
    # "https://www.kjmotorsports.com/utv/drivetrain/drive-belts",
    # "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2",
    # "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=3",
    # "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=4",
    # "https://www.kjmotorsports.com/utv/electrical/batteries-accessories/batteries",
    # "https://www.kjmotorsports.com/utv/electrical/batteries-accessories/battery-accessories",
    # "https://www.kjmotorsports.com/utv/electrical/horns",
    # "https://www.kjmotorsports.com/utv/electrical/lighting/headlight-bulbs?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=3&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/lighting/light-bars?p=4&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/lighting/lighted-whips?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/lighting/lighted-whips?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/lighting/mounts-clamps",
    # "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=3&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/sound-systems?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winches?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winches?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-mounts?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-mounts?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=3&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/electrical/winches-accessories/winch-accessories?p=4&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/exhaust-systems-and-parts/slip-on-exhausts?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=2",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=3",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=4",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=5",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=6",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=7",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=8",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=9",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=10",
    # "https://www.kjmotorsports.com/utv/frame-chassis/a-arms-and-radius-rods?p=6&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/bumpers?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/bumpers?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/cages",
    # "https://www.kjmotorsports.com/utv/frame-chassis/nerf-bars",
    # "https://www.kjmotorsports.com/utv/frame-chassis/power-steering-kits",
    # "https://www.kjmotorsports.com/utv/frame-chassis/rack-and-pinion",
    # "https://www.kjmotorsports.com/utv/frame-chassis/skid-plates-guards",
    # "https://www.kjmotorsports.com/utv/frame-chassis/suspension?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/suspension?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/suspension?p=3&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods",
    # "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods?p=2",
    # "https://www.kjmotorsports.com/utv/frame-chassis/tie-rods?p=3",
    # "https://www.kjmotorsports.com/utv/intake-fuel",
    # "https://www.kjmotorsports.com/utv/interior/bags-storage",
    # "https://www.kjmotorsports.com/utv/interior/dash-accessories/dash-accessories/rocker-switches",
    # "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
    # "https://www.kjmotorsports.com/utv/drivetrain/clutching",
    # "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/grab-bars-handles",
    # "https://www.kjmotorsports.com/utv/interior/mirrors/rear-view-mirrors?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mirrors/rear-view-mirrors?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mirrors/side-view-mirrors?p=3&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/clamps",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/fire-extinguisher-mounts",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/go-pro-camera-mounts",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/light-bar-mounts?p=3&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/mounts-clamps/mounts/universal-mounts",
    # "https://www.kjmotorsports.com/utv/interior/shift-knobs-levers?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/smartphone-tablet-accessories?product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/smartphone-tablet-accessories?p=2&product_list_limit=32",
    # "https://www.kjmotorsports.com/utv/interior/steering-wheels",
    # "https://www.kjmotorsports.com/utv/outdoor-gear/coolers",
    # "https://www.kjmotorsports.com/utv/outdoor-gear/drinkware",
    # "https://www.kjmotorsports.com/atv/snow-plows-accessories/snow-plows",
    # "https://www.kjmotorsports.com/atv/snow-plows-accessories/plow-mounts",
    # "https://www.kjmotorsports.com/atv/snow-plows-accessories/plow-accessories",
    # "https://www.kjmotorsports.com/atv/snow-plows-accessories/winches-accessories",
    # "https://www.kjmotorsports.com/utv/tires/single",
    # "https://www.kjmotorsports.com/utv/tires/pairs",
    # "https://www.kjmotorsports.com/utv/tires/full-sets",
    # "https://www.kjmotorsports.com/utv/wheels/single",
    # "https://www.kjmotorsports.com/utv/wheels/wheel-accessories",
    # "https://www.kjmotorsports.com/utv/winches-accessories/winches",
    # "https://www.kjmotorsports.com/utv/winches-accessories/winch-mounts",
    # "https://www.kjmotorsports.com/utv/winches-accessories/winch-accessories"
# ]
# all_data = []
# fieldnames = ["name", "price", "SKU", "images"]  # Added "images" to fieldnames

# # Function to filter data based on price
# def filter_data(data, min_price, max_price):
#     filtered_data = []

#     for item in data:
#         item_price_str = ''.join(c for c in item['price'] if c.isdigit() or c == '.')

#         try:
#             item_price = float(item_price_str)
#         except ValueError:
#             print(f"Skipping item due to invalid price: {item['name']} - {item['price']}")
#             continue

#         if min_price <= item_price <= max_price:
#             filtered_data.append(item)

#     return filtered_data

# # Function to extract image link from product container
# def extract_image_link(container):
#     image_element = container.find("img", class_="product-image-photo")
#     if image_element:
#         return image_element.get("src")
#     return None

# for url in page_urls:
#     current_page_data = []

#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, "lxml")

#     product_containers = soup.find_all("div", class_="product-item-info")

#     for container in product_containers:
#         product_name = container.find("a", class_="product-item-link").get_text(strip=True)
#         product_price = container.find("span", class_="price").get_text(strip=True)
#         product_sku = container.find("div", class_="cat-sku").get_text(strip=True)

#         # Extract image link using the defined function
#         product_image = extract_image_link(container)

#         current_page_data.append({
#             "name": product_name,
#             "price": product_price,
#             "SKU": product_sku,
#             "images": product_image
#         })

#     all_data += current_page_data

# previous_csv_file_path = "/home/lenovo/Desktop/filtered_data1.csv"

# try:
#     with open(previous_csv_file_path, mode='r') as previous_file:
#         previous_data = list(csv.DictReader(previous_file))
# except FileNotFoundError:
#     previous_data = []

# all_data = previous_data + all_data

# min_price = 0.0
# max_price = 100.0
# filtered_data = filter_data(all_data, min_price, max_price)

# filtered_data.sort(key=lambda x: float(''.join(c for c in x['price'] if c.isdigit() or c == '.')))

# filtered_csv_file_path = "/home/lenovo/Desktop/filtered_data1.csv"

# with open(filtered_csv_file_path, mode='w', newline='') as filtered_csv_file:
#     writer = csv.DictWriter(filtered_csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for product in filtered_data:
#         writer.writerow(product)

# print(f"Filtered and sorted data with image links has been saved to {filtered_csv_file_path}")

# ----------------------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import csv

# List of URLs for different pages
page_urls = [
    "https://www.kjmotorsports.com/utv/body/cargo-boxes-and-storage",
    "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/doors",
    "https://www.kjmotorsports.com/utv/body/doors-and-door-bags/door-bags",
    "https://www.kjmotorsports.com/utv/body/fuel-packs-mounts",
    "https://www.kjmotorsports.com/utv/body/gas-caps",
    "https://www.kjmotorsports.com/utv/body/grilles",
    "https://www.kjmotorsports.com/utv/body/roofs",
    "https://www.kjmotorsports.com/utv/body/seats-and-harnesses",
    "https://www.kjmotorsports.com/utv/body/windshields",
    "https://www.kjmotorsports.com/utv/body/windshields?p=2",
    "https://www.kjmotorsports.com/utv/body/windshields?p=3",
    "https://www.kjmotorsports.com/utv/body/windshields?p=4",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=2",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/single?p=3",
    "https://www.kjmotorsports.com/utv/drivetrain/axles-and-accessories/axles/full-sets",
    "https://www.kjmotorsports.com/utv/drivetrain/carrier-bearings",
    "https://www.kjmotorsports.com/utv/drivetrain/clutching",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=2",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=3",
    "https://www.kjmotorsports.com/utv/drivetrain/drive-belts?p=4",
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
    "https://www.kjmotorsports.com/utv/lighting/mounts-clamps?p=3&product_list_limit=32",
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
    "https://www.kjmotorsports.com/utv/winches-accessories/winch-accessories"
]

all_data = []
fieldnames = ["name", "price", "SKU", "images"]  # Added "images" to fieldnames

# Function to filter data based on price
def filter_data(data, min_price, max_price):
    filtered_data = []

    for item in data:
        item_price_str = ''.join(c for c in item['price'] if c.isdigit() or c == '.')

        try:
            item_price = float(item_price_str)
        except ValueError:
            print(f"Skipping item due to invalid price: {item['name']} - {item['price']}")
            continue

        if min_price <= item_price <= max_price:
            filtered_data.append(item)

    return filtered_data

# Function to extract image link from product container
def extract_image_link(container):
    image_element = container.find("img", class_="product-image-photo")
    if image_element:
        return image_element.get("src")
    return None

for url in page_urls:
    current_page_data = []

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    product_containers = soup.find_all("div", class_="product-item-info")

    for container in product_containers:
        product_name = container.find("a", class_="product-item-link").get_text(strip=True)
        product_price = container.find("span", class_="price").get_text(strip=True)
        product_sku = container.find("div", class_="cat-sku").get_text(strip=True)

        # Extract image link using the defined function
        product_image = extract_image_link(container)

        current_page_data.append({
            "name": product_name,
            "price": product_price,
            "SKU": product_sku,
            "images": product_image
        })

    all_data += current_page_data

previous_csv_file_path = "/home/lenovo/Desktop/filtered_data1.csv"

try:
    with open(previous_csv_file_path, mode='r') as previous_file:
        previous_data = list(csv.DictReader(previous_file))
except FileNotFoundError:
    previous_data = []

all_data = previous_data + all_data

# Change the min_price and max_price as needed
min_price = 100.0
max_price = 200.0
filtered_data = filter_data(all_data, min_price, max_price)

filtered_data.sort(key=lambda x: float(''.join(c for c in x['price'] if c.isdigit() or c == '.')))

filtered_csv_file_path = "/home/lenovo/Desktop/filtered_data1.csv"

with open(filtered_csv_file_path, mode='a', newline='') as filtered_csv_file:
    writer = csv.DictWriter(filtered_csv_file, fieldnames=fieldnames)
    
    # Write only the header if the file is empty
    if filtered_csv_file.tell() == 0:
        writer.writeheader()
    
    for product in filtered_data:
        writer.writerow(product)

print(f"Filtered and sorted data with image links has been appended to {filtered_csv_file_path}")
