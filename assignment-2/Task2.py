import requests
import json

def get_data(category_id, start):
    url = f"https://www.pricerunner.dk/public/search/category/v3/DK/{category_id}"
    querystring = {"size": "48", "device": "desktop", "sorting": "RANK_asc", "offset": start, "quickFilterSize": "3"}
    response = requests.get(url, params=querystring)
    response.raise_for_status()
    data = response.json()
    return data

def collect_products_for_category(category_id):
    products = []
    for i in range(1, 10):  # Adjust the range as needed
        data = get_data(category_id, i)
        if 'products' in data:
            for item in data['products']:
                product = {
                    "id": item['id'],
                    "name": item['name'],
                    "lowestPrice": item['lowestPrice']
                }
                products.append(product)
    return products

def print_product_details(product):
    print("Product Details:")
    for key, value in product.items():
        if isinstance(value, dict):
            print(f"  {key}:")
            for sub_key, sub_value in value.items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {value}")

def print_all_product_names(products):
    print("Product Names:")
    for product in products:
        print(f"  {product['name']}")

def find_product_by_name(products, name):
    for product in products:
        if product['name'].lower() == name.lower():
            return product
    return None

categories = {
    "ice_makers": "250",
    "blenders": "84",
    "vacuum_cleaners": "19"
}

print("Available categories:")
for category in categories:
    print(f"  - {category}")

user_input = input("\nEnter a category name: ").strip().lower()

if user_input in categories:
    category_id = categories[user_input]
    print(f"\nCollecting products for category: {user_input}")
    products = collect_products_for_category(category_id)

    print(f"\nProduct names in category '{user_input}':")
    print_all_product_names(products)
else:
    print("Invalid category. Please try again.")

if products:
    product_name = input("\nWhat product do you want the details of? ").strip()
    product = find_product_by_name(products, product_name)
    if product:
        print(f"\nDetails of the product '{product_name}':")
        print_product_details(product)
    else:
        print(f"No product found with the name '{product_name}'.")
else:
    print("No products found in this category.")