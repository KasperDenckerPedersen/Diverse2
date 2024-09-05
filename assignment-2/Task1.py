import requests
import json

Products = []

def get_data(start):
    url = "https://www.pricerunner.dk/public/search/category/v3/DK/250"
    querystring = {"size": "48", "device": "desktop", "sorting": "RANK_asc", "offset": start, "quickFilterSize": "3"}
    response = requests.request("GET", url, params=querystring)
    data = json.loads(response.text)
    return data
AllProducts = []
for i in range(1, 40):
    data = get_data(i)
    for item in data['products']:
        product = {
            "id": item['id'],
            "name": item['name'],
            "lowestPrice": item['lowestPrice']
            }
    AllProducts.append(product)

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


print_product_details(AllProducts[0])

print_all_product_names(AllProducts)