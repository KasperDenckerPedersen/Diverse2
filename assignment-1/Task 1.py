import random
#- Create three separate lists to store product information:
#   - `items`: List of product names.
#   - `prices`: List of product prices.
#   - `inventories`: List of product inventories.

items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]

sales_list = [0, 0, 0]
id_list = []
n = 400

#- Create a function `simulate_customers`:
#   - Simulate a given number of students arriving in the university.
#   - For each student, the chance of buying an item at the cafeteria is 50%.
#   - For the students that buy an item, randomly select which item it is.
#   - Check if there is still inventory for the item available and process the transaction (reduce the inventory, store the sale)
#   - The function should return a list `sales` storing all item ids of the performed transactions

def simulate_customers(n):
    for i in range(n):
        number = random.randint(0,1)
        if number == 1:
            number2 = random.randint(0, 2)
            if number2 == 0 and inventories[0] > 0:
                sales_list[0] += 1
                id_list.append(items[0])
                inventories[0] -= 1
            elif number2 == 1 and inventories[1] > 0:
                sales_list[1] += 1
                id_list.append(items[1])
                inventories[1] -= 1
            elif number2 == 2 and inventories[2] > 0:
                sales_list[2] += 1
                id_list.append(items[2])
                inventories[2] -= 1
    return sales_list

sales_list = simulate_customers(n)

#- Create a function `process_sales`:
#- Calculate the total revenue from the list of customer transactions (`sales`).

def process_sales():
    total_revenue = [prices[i] * sales_list[i] for i in range(len(prices))]
    return total_revenue

total_revenue = process_sales()

# - Create a function `generate_report`:
#   - Print a summary of the day's sales, including total revenue and remaining inventory.

def generate_report():
    print(f"{sales_list[0]} Sandwiches sold\n{sales_list[1]} Salads sold\n{sales_list[2]} Cakes sold\n")
    print(f"Revenue:\nSandwiches: {total_revenue[0]}\nSalads: {total_revenue[1]}\nCakes: {total_revenue[2]}\n")
    print(f"Remaining Inventory:\nSandwiches: {inventories[0]}\nSalads: {inventories[1]}\nCakes: {inventories[2]}")

#generate_report()

# In reality, the cafeteria does not only care for the revenue but also for the left over items that can not be sold on the next day and have to be disposed of. 
# Assume, that the production costs for each item are half the sales price. Write a function that calculates the costs of the left over items. 
# Use the costs as well as the revenue to also calculate the profit for the day and include it in your daily report.

production_cost = [32.5, 22.5, 25]

def leftover_cost():
    leftoverCost = [production_cost[i] * inventories[i] for i in range(len(production_cost))]
    return leftoverCost

def sales_cost():
    SalesCost = [production_cost[i] * sales_list[i] for i in range(len(production_cost))]
    return SalesCost

leftoverCost = leftover_cost()
SalesCost = sales_cost()

total_cost = [SalesCost[i] + leftoverCost[i] for i in range(len(SalesCost))]

def profit():
    TotalProfit = [total_revenue[i] - total_cost[i] for i in range(len(total_revenue))]
    return TotalProfit

TotalProfit = profit()

print(TotalProfit)

