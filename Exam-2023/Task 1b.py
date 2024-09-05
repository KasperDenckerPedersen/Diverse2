import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_info():
    citizenID = input("Citizen ID: ")
    firstName = input("First name: ")
    lastName = input("Last name: ")
    WaterUsage = int(input("Water usage (in liters): "))
    ElecUsage = int(input("Electricity usage (in kWh): "))
    Year = int(input("Year: "))
    Information = {
        'citizenID': citizenID,
        'first name': firstName,
        'last name': lastName,
        'water usage': WaterUsage,
        'electricity usage': ElecUsage,
        'year': Year
    }
    return Information

def water_price(WaterUsage):
    if WaterUsage <= 50000:
        WaterCost = WaterUsage * 0.05
    elif WaterUsage <= 100000:
        WaterCost = WaterUsage * 0.03
    elif WaterUsage <= 150000:
        WaterCost = WaterUsage * 0.02
    else:
        WaterCost = WaterUsage * 0.015
    return WaterCost

def electricity_price(ElecUsage):
    if ElecUsage <= 1000:
        ElecCost = ElecUsage * 0.3
    elif ElecUsage <= 2000:
        ElecCost = ElecUsage * 0.35
    elif ElecUsage <= 4000:
        ElecCost = ElecUsage * 0.45
    else:
        ElecCost = ElecUsage * 0.55
    return ElecCost

def calculate_charge(Information):
    WaterCost = water_price(Information["water usage"])
    ElecCost = electricity_price(Information['electricity usage'])
    utilityCharges = WaterCost + ElecCost
    return utilityCharges

def calculate_charge_all(citizen_list):
    charges = {}
    for citizen in citizen_list:
        charge = calculate_charge(citizen)
        charges[citizen['citizenID']] = charge
    return charges

citizen_list = []
n = 2

for i in range(n):
    citizen_info = get_info()
    citizen_list.append(citizen_info)

charges = calculate_charge_all(citizen_list)


for citizen in citizen_list:
    citizenID = citizen['citizenID']
    utility_charge = charges[citizenID]
    print(f"Citizen ID: {citizenID} must pay {utility_charge:.2f} euphoriums for utility charges for the year {citizen['year']}.")