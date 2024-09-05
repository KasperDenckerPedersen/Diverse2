# Assignment 3: Monte Carlo Simulation for Inventory Management

## Scenario
In this assignment, you will use Monte Carlo simulation to help a retail company manage its inventory. The company sells a single product, and the daily demand for this product is uncertain. You will simulate the daily demand over a month (30 days) to help the company determine optimal inventory levels.

## Tasks

### 1. Simulate Daily Demand and Analyze Results
Write a function that simulates the daily demand for the product over the next n days using a Poisson distribution.

**Steps:**
- Assume the average daily demand (`λ`) is 20 units.
- Use `numpy` to generate Poisson-distributed daily demand for n days.

**Analyze the Results:**
- Plot a histogram of the simulated daily demand values.
- Calculate and print the following statistics from the simulation results:
  - Mean (average) daily demand
  - Standard deviation
  - 5th percentile (to understand the lower bound in a worst-case scenario)
  - 95th percentile (to understand the upper bound in a best-case scenario)
- Interpret the results in the context of inventory management.

### 2. Inventory Level Simulation
Determine the optimal inventory level for one month that minimizes the risk of stockouts (running out of stock). Assume that there is no reordering during a month.

**Steps:**
- Assume the company wants to maintain a service level of 95%, meaning they want to meet the demand 95% of the time.
- Simulate the total demand for 30 days multiple times (e.g., 1,000 simulations) to understand the distribution of monthly demand.
- Determine the inventory level that would be sufficient to meet the demand 95% of the time.
- Plot a histogram of the total monthly demand and mark the optimal inventory level on the plot.
- Calculate and print the optimal inventory level.

### 3. Optional
To further enhance your simulation, consider the following improvement:
- Create a user interface to input different assumptions (e.g., average daily demand, service level).