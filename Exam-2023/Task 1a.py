import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SizeList = {1: "small", 2: "medium", 3: "large"}
MilkList = {1: "regular", 2: "soy", 3: "almond"}
SweetnessList = {1: "no sugar", 2: "regular", 3: "extra sweet"}
WeatherList = {1: "sunny", 2: "cloudy", 3: "rainy"}
PossibleOrders = {'Size': SizeList, "Milk": MilkList, "Sweetness": SweetnessList, "Weather": WeatherList}
order = {}

def print_menu():
    print("Welcome to the coffeshop\nWe sell only one type of coffe")

def get_info():
    name = input("What is your name?\n>")
    Size = int(input(f"What size coffe would you like?\n1. for {SizeList[1]}\n2. for {SizeList[2]}\n3. for {SizeList[3]}\n>"))
    Milk = int(input(f"What milk type would you like?\n1. for regular\n2. for soy\n3. for almond\n>"))
    Sweetness = int(input(f"How sweet would you like it?\n1. for no sugar\n2. for regular sugar\n3. for extra sweet\n>"))
    Weather = int(input(f"What is the weather like outside?\n1. for sunny\n2. for cloudy\n3. for rainy\n>"))
    return Size, Milk, Sweetness, Weather, name

def order_info():
    order['Size'] = SizeList[Size]
    order['Milk'] = MilkList[Milk]
    order['Sweetness'] = SweetnessList[Sweetness]
    order['Weather'] = WeatherList[Weather]

    print(f"The order of {name} is:")
    print(f"Size: {order['Size']}")
    print(f"Milk Type: {order['Milk']}")
    print(f"Sweetness: {order['Sweetness']}")
    print(f"Weather: {order['Weather']}")

def calculate_price(order):
    Price = 0

    if order['Size'] == "small":
        base_price = 2
    elif order['Size'] == "medium":
        base_price = 2 * 1.5
    elif order['Size'] == "large":
        base_price = 2 * 2

    if order['Milk'] == "regular":
        Price = base_price
    elif order['Milk'] == "soy":
        Price = base_price + 0.5
    elif order['Milk'] == "almond":
        Price = base_price + 1

    if order['Sweetness'] == "no sugar":
        Price += 0
    elif order['Sweetness'] == "regular":
        Price += 0.5
    elif order['Sweetness'] == "extra sweet":
        Price += 1

    if order['Weather'] == "sunny":
        Price *= 1.1
    elif order['Weather'] == "cloudy":
        Price += 0
    elif order['Weather'] == "rainy":
        Price *= 0.9
    return Price

print_menu()
Size, Milk, Sweetness, Weather, name = get_info()
order_info()
Price = calculate_price(order)
print(f"The total price is: {Price}$")



