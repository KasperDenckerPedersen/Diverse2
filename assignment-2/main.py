import random
import numpy as np
import requests

def get_data(category_id, start):
    url = f"https://www.pricerunner.dk/public/search/category/v3/DK/{category_id}"
    querystring = {"size": "48", "device": "desktop", "sorting": "RANK_asc", "offset": start, "quickFilterSize": "3"}
    response = requests.get(url, params=querystring)
    response.raise_for_status()
    data = response.json()
    return data

def get_choice(Catagories):
    for category in Catagories:
        print(f"  - {category}")
    catagoryChoice = input("What catagory do you wanna see?\n>")
    return catagoryChoice


def get_products():
    for i in range(len(data['products'])):
        ProductName = data['products'][i]['name']
        LowestPrice = data['products'][i]['lowestPrice']['amount']
        ID = data['products'][i]['id']
        AverageRating = data['products'][i]['rating']['averageRating']
        Merchant = data['products'][i]['cheapestOffer']['merchant']['name']
        
        ProductsInCategory['name'] = ProductName
        ProductsInCategory[ProductName] = {'lowestPrice': LowestPrice, 'ID': ID, 'rating': AverageRating, 'merchant': Merchant}
        print(ProductName)

def get_summary():
    Choice = input("What product do you want details about?\n>")
    print(f"\nHere is the details about {Choice}:")
    print(f"ID: {ProductsInCategory[Choice]['ID']}")
    print(f"Lowest Price: {ProductsInCategory[Choice]['lowestPrice']}")
    print(f"Average Rating: {ProductsInCategory[Choice]['rating']}")
    print(f"Store: {ProductsInCategory[Choice]['merchant']}")

Catagories = {
    'Ismaskiner': '250', 
    'Frituregyrder': '81', 
    'Kaffemaskiner': '82', 
    'Blendere': '84'
    }

ProductsInCategory = {}

catagoryChoice = get_choice(Catagories)
data = get_data(Catagories[catagoryChoice], 1)
get_products()
get_summary()