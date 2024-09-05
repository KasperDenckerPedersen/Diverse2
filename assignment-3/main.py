import random 
import numpy as np
import matplotlib.pyplot as plt

print('Task 1')
def run_simulation(n, demand_list):
    for i in range(n):
        avgDemand = 20
        demand = np.random.poisson(avgDemand)
        demand_list.append(demand)
    return demand_list

print('Interpret the results:\n') 
def print_statistics():
    print(f"The average daily demand of the {n} days is {np.mean(demand_list):.2f}.")
    print(f"The daily demand varies {np.std(demand_list):.2f}, from the average demand.")
    print(f"5th percentile (lower bound): The daily demand has a 5 % chance of being {np.quantile(demand_list, 0.05)} or lower.")
    print(f"95th percentile (upper bound): The daily demand has a 95% chance og being {np.quantile(demand_list, 0.95):.2f} or lower.\n")

n = 30
demand_list = []
run_simulation(n, demand_list)
print_statistics()
plt.hist(demand_list, bins = 10,  edgecolor = 'black')
plt.title(f'Simulated daily demand of {n} days')
plt.xlabel('Avg Daily Demand')
plt.ylabel('Frequency (days)')
plt.savefig("A1.png")
#plt.show()

print('Task 2\n')

def run_simulation2(n):
    totalDemand = 0
    for i in range(n):
        avgDemand = 20
        demand_list = []
        demand = np.random.poisson(avgDemand)
        totalDemand += demand
    return totalDemand

demand_list2 = []
for i in range(1000):
    totalDemand = run_simulation2(30)
    demand_list2.append(totalDemand)

serviceLevel = np.quantile(demand_list2, 0.95)
print(f"The monthly demand average is {np.mean(demand_list2)}")
print(f"To make sure 95% of the demand is met, the monthly inventory level should be {serviceLevel}")

plt.figure()
plt.hist(demand_list2, bins = 10,  edgecolor = 'black')
plt.title(f'Simulated total demand of 1000 runs')
plt.axvline(serviceLevel, color = 'red', linestyle = 'dashed')
plt.xlabel('Avg monthly Demand')
plt.ylabel('Frequency (moths)')
plt.savefig("A2.png")




