# Assignment 2: Webscraping

## Scenario
In this assignment, you will write a webscraper for the website [www.pricerunner.dk](https://www.pricerunner.dk). PriceRunner is a comparison shopping service that allows users to compare prices on a wide range of products from different retailers. It provides detailed product information, reviews, and price history to help consumers make informed purchasing decisions. 

## Tasks:

### 1. Collect Product Information
Your first task is to figure out how to scrape the (high-level) information (e.g., product id, name, price, description, url, number of ratings, average rating) from a given category. For example, you can start with the ice cream machines [www.pricerunner.dk/cl/250/Ismaskiner](https://www.pricerunner.dk/cl/250/Ismaskiner). Hint: You can organize your code in a way that the webscraper stores the information on the products in a list of dictionaries (each dictionary describes one product). Subsequently write two functions: One that receives one product as input and prints all information on the product and one that receives the list of products as an input and prints only the names of all available products in the list.

### 2. Collect different categories
In the next step you should improve your program so it is able to collect the products from different categories. To this end you want to modify your code above so that it takes an identifier for a category as input and returns the products of this category.
Hint: You can manually identify the identifiers for some different categories and store them in your code.

### 3. Optional
If you want to improve you program here are a couple of ideas:
- Try to find a way to find all the available categories and subcategories automatically
- Provide a user interface (menu) to the user to navigate between the categories and ask for product information