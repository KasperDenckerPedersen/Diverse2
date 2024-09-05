import random
import numpy as np

prodCost = 5
Price = 20
holdingCost = 2
lostSalePrice = Price - prodCost
maxCapacity = 1500

def Simulate_1_Month():
    demand = np.random.normal(1000, 200)
    return demand

def Simulate_1_Year(Production):
    SoldUnits = 0
    Inventory = 0
    Revenue = 0
    RevenueList = []
    Profit = 0
    ProfitList = []
    Cost = 0
    CostList = []
    InventoryList = []
    for i in range(12):
        Inventory += Production
        demand = Simulate_1_Month()
        if demand > 1500:
            demand = 1500
        SoldUnits = np.minimum(demand, Inventory)
        lostSale = np.maximum(0, demand-Inventory)
        Revenue = SoldUnits * Price
        RevenueList.append(Revenue)
        Inventory -= SoldUnits
        InventoryList.append(Inventory)
        Cost = (SoldUnits * prodCost) + (Inventory * holdingCost) + (lostSalePrice * lostSale)
        CostList.append(Cost)
        Profit = Revenue - Cost
        ProfitList.append(Profit)
    MinInventory = np.min(InventoryList)
    return ProfitList, MinInventory

def Simulate_n_years(n, Production):
    AllProfitList = []
    AllInventoryList = []
    for i in range(n):
        ProfitList, MinInventory = Simulate_1_Year(Production)
        MeanProfit = np.mean(ProfitList)
        AllProfitList.append(MeanProfit)
        AllInventoryList.append(MinInventory)
    AllMeanProfit = np.mean(AllProfitList)
    AllMinInventory = np.min(AllInventoryList)
    return AllMeanProfit, AllMinInventory

for i in range(975, 1075, 5):
    Production = i
    AllMeanProfit, AllMinInventory = Simulate_n_years(1000, i)

    print(f" The average profit a year, when producing {Production} is: {AllMeanProfit}")
    #print(f"The lowest inventory level this year was: {AllMinInventory}\n")

# Task 1:
#The optimal number of umbrellas to produce is mostly: 1050

#Task 2:
#If i increase the holding cost to 3$, the optimal number to produce is now mostly: 1020