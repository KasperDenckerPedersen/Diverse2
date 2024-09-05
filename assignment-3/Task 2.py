import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### 2. Inventory Level Simulation
# Determine the optimal inventory level for one month that minimizes the risk of stockouts (running out of stock). Assume that there is no reordering during a month.

# **Steps:**
# - Assume the company wants to maintain a service level of 95%, meaning they want to meet the demand 95% of the time.
# - Simulate the total demand for 30 days multiple times (e.g., 1,000 simulations) to understand the distribution of monthly demand.
# - Determine the inventory level that would be sufficient to meet the demand 95% of the time.
# - Plot a histogram of the total monthly demand and mark the optimal inventory level on the plot.
# - Calculate and print the optimal inventory level.

# # Assignment 3: Monte Carlo Simulation for Inventory Management

def get_info():
    n = int(input("How many times should the simulation run?\n>"))
    service_level = float(input("What service level is required? (Between 0-1)\n>"))
    dailyDemand = int(input("What is the daily demand?\n>"))
    return n, service_level, dailyDemand

def simulate_30_days_n_simulations_demand(n, dailyDemand):
    for i in range(n):
        monthlyDemand = 0
        for i in range(30):
            demand = np.random.poisson(dailyDemand)
            demandList.append(demand)
            monthlyDemand += demand
        totalDemandList.append(monthlyDemand)
    return totalDemandList

def get_summary():
    print(f"\nInventory level that secures {service_level*100}% service level each month:\n{Quantile:.2f}\n")

def get_histogram():
    plt.hist(totalDemandList, bins=30, edgecolor="white")
    plt.axvline(Quantile, color='k', linestyle='dashed', linewidth=1)
    plt.show()

demandList = []
totalDemandList = []

n, service_level, dailyDemand = get_info()

totalDemandList = simulate_30_days_n_simulations_demand(n, dailyDemand)
Quantile = np.quantile(totalDemandList, service_level)

get_summary()

choice = input("Should the simulation be visualised? (Y or N)\n>")
if choice == "Y":
    get_histogram()
