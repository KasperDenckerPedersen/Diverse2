
# Reset the initial inventory, sales, and id_list to simulate new conditions
import random

items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]

sales_list = [0, 0, 0]
id_list = []
n = 400

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

def process_sales():
    total_revenue = [prices[i] * sales_list[i] for i in range(len(prices))]
    return total_revenue

total_revenue = process_sales()

def generate_report():
    print(f"{sales_list[0]} Sandwiches sold\n{sales_list[1]} Salads sold\n{sales_list[2]} Cakes sold\n")
    print(f"Revenue:\nSandwiches: {total_revenue[0]}\nSalads: {total_revenue[1]}\nCakes: {total_revenue[2]}\n")
    print(f"Remaining Inventory:\nSandwiches: {inventories[0]}\nSalads: {inventories[1]}\nCakes: {inventories[2]}")

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

def reset_inventory():
    global inventories, sales_list, id_list
    inventories = [100, 50, 100] 
    sales_list = [0, 0, 0]
    id_list = []

def calculate_profit(n):
    simulate_customers(n)
    total_revenue = process_sales()
    leftoverCost = leftover_cost()
    SalesCost = sales_cost()
    total_cost = [SalesCost[i] + leftoverCost[i] for i in range(len(SalesCost))]
    TotalProfit = sum([total_revenue[i] - total_cost[i] for i in range(len(total_revenue))])
    return TotalProfit

def find_optimal_inventory():
    max_profit = float('-inf')
    best_inventory = None
    inventory_ranges = range(50, 151, 10)

    for inv_sandwich in inventory_ranges:
        for inv_salad in inventory_ranges:
            for inv_cake in inventory_ranges:
                reset_inventory()
                inventories[0] = inv_sandwich
                inventories[1] = inv_salad
                inventories[2] = inv_cake
                
                profit = calculate_profit(n)
                
                if profit > max_profit:
                    max_profit = profit
                    best_inventory = (inv_sandwich, inv_salad, inv_cake)

    return best_inventory, max_profit

optimal_inventory, optimal_profit = find_optimal_inventory()
print(f"Optimal Inventory Levels:\nSandwiches: {optimal_inventory[0]}\nSalads: {optimal_inventory[1]}\nCakes: {optimal_inventory[2]}")
print(f"Maximum Profit: {optimal_profit}")