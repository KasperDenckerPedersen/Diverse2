import random

# Task 1 - Three separate lists:
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]
sales_list = [0, 0, 0]

# Task 2 - Simulate Customer Arrivals
# - Create a function `simulate_customers`:
#   - Simulate a given number of students arriving in the university.
#   - For each student, the chance of buying an item at the cafeteria is 50%.
#   - For the students that buy an item, randomly select which item it is.
#   - Check if there is still inventory for the item available and process the transaction (reduce the inventory, store the sale)
#   - The function should return a list `sales` storing all item ids of the performed transactions

def simulate_customers():
    min_students = 50
    max_students = 200
    arriving_students = random.randint(min_students, max_students)

    for _ in range(arriving_students):
        if random.randint(0, 1) == 1:  # 50% chance to buy
            product_decider = random.randint(0, 2)
            if inventories[product_decider] > 0:
                sales_list[product_decider] += 1
                inventories[product_decider] -= 1

# Task 3 - Process sales
# - Create a function `process_sales`:
#   - Calculate the total revenue from the list of customer transactions (`sales`).

def process_sales():
    total_revenue = [prices[i] * sales_list[i] for i in range(len(prices))]
    return total_revenue

# Task 4 - Generate Sales Report
# - Create a function `generate_report`:
#   - Print a summary of the day's sales, including total revenue and remaining inventory.

def generate_report():
    simulate_customers()
    total_revenue = process_sales()
    print("Sales Report:")
    print("-------------")
    for i in range(len(items)):
        print(f"{items[i]}: Sold {sales_list[i]}, Remaining {inventories[i]}, Revenue: {total_revenue[i]}")
    return total_revenue

# Task 5 - Optional 1 (If you want to practice some more)
# In reality, the cafeteria does not only care for the revenue but also for the left over items that can not be sold on the next day and have to be disposed of. 
# Assume, that the production costs for each item are half the sales price. Write a function that calculates the costs of the left over items. 
# Use the costs as well as the revenue to also calculate the profit for the day and include it in your daily report.

def production_cost():
    total_revenue = generate_report()
    cost = 0.5
    cost_list = [prices[i] * cost for i in range(len(prices))]
    
    leftover_cost = sum(inventories[i] * cost_list[i] for i in range(len(inventories)))
    total_profit = sum(total_revenue[i] - (sales_list[i] * cost_list[i]) for i in range(len(prices)))
    
    print("\nCost and Profit Report:")
    print("-----------------------")
    print(f"Total Leftover Cost: {leftover_cost}")
    print(f"Total Profit: {total_profit}")

# Run the report and profit calculation
production_cost()