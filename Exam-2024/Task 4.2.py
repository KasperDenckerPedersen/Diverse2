import random
import numpy as np
import matplotlib.pyplot as plt

prodCost = 5
Price = 15
lostSalePentalty = Price - prodCost
maxProduction = 1200

def Simulate_1_day():
    DailyDemand = np.random.poisson(800)
    return DailyDemand

def optimal_production(Production):
    SoldUnits = 0
    Revenue = 0
    Profit = 0
    ProfitList = []
    Cost = 0
    for i in range(10000):
        DailyDemand = Simulate_1_day()
        if DailyDemand > 1200:
            DailyDemand = 1200
        
        SoldUnits = np.minimum(DailyDemand, Production)
        lostSale = np.maximum(0, DailyDemand-Production)
        Revenue = SoldUnits * Price
        Cost = (Production * prodCost) + (lostSale * lostSalePentalty)
        Profit = Revenue - Cost
        ProfitList.append(Profit)
    TotalProfit = np.sum(ProfitList)
    return TotalProfit

productionQuantities = []
totalProfits = []
BestProfit = 0
BestQuantity = 0

for i in range(800, 850, 1):
    TotalProfit = optimal_production(i)
    productionQuantities.append(i)
    totalProfits.append(TotalProfit)
    if TotalProfit > BestProfit:
        BestProfit = TotalProfit
        BestQuantity = i

print(f"\nThe best quantity to produce is: {BestQuantity}\nThis gives a total profit of: {BestProfit}$")
plt.plot(productionQuantities, totalProfits)
plt.xlabel('Production quantity')
plt.ylabel('Profit')
plt.title('Profit based apond the production quantity')
plt.show()

#When increasing the production cost to 5$, the optimal quantity decreases a little (around 5 units)
#The total profit will also decrease (around 10%).