# # Assignment 3: Monte Carlo Simulation for Inventory Management
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ## Scenario
# In this assignment, you will use Monte Carlo simulation to help a retail company manage its inventory. 
# The company sells a single product, and the daily demand for this product is uncertain. 
# You will simulate the daily demand over a month (30 days) to help the company determine optimal inventory levels.

# ## Tasks

# ### 1. Simulate Daily Demand and Analyze Results
# Write a function that simulates the daily demand for the product over the next n days using a Poisson distribution.

# **Steps:**
# - Assume the average daily demand (`λ`) is 20 units.
# - Use `numpy` to generate Poisson-distributed daily demand for n days.

# **Analyze the Results:**
# - Plot a histogram of the simulated daily demand values.
# - Calculate and print the following statistics from the simulation results:
#   - Mean (average) daily demand
#   - Standard deviation
#   - 5th percentile (to understand the lower bound in a worst-case scenario)
#   - 95th percentile (to understand the upper bound in a best-case scenario)
# - Interpret the results in the context of inventory management.

demandList = []
n = 30

def simulate_n_days_demand(n):
    for i in range(n):
        demand = np.random.poisson(20)
        demandList.append(demand)
    return demandList

demandList = simulate_n_days_demand(n)

def get_summary(demand_list):
    Mean = np.mean(demand_list)
    Std = np.std(demand_list)
    LowerBound = np.quantile(demand_list, 0.05)
    UpperBound = np.quantile(demand_list, 0.95)
    print(f"Mean: {Mean:.2f}")
    print(f"Std: {Std:.2f}")
    print(f"Lower Bound: {LowerBound:.2f}")
    print(f"Upper Bound: {UpperBound:.2f}")

plt.hist(demandList)

get_summary(demandList)

plt.show()