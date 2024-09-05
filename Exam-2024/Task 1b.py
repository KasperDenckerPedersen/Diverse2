import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_info():
    data = {}
    salesT = int(input("What is the eployeess sales target achievement?\n>"))
    customorS = int(input("What is the employees customer satisfaction?\n>"))
    attendance = int(input("What was the amployess attendancy days?\n>"))
    peerF = int(input("What was the employees peer feedback?\n>"))
    yearS = int(input("How many years of service does the employee have?\n>"))

    data = {'salesTarget': salesT, 'customerSatisfaction': customorS, 'attendance': attendance, 'peerFeedback': peerF, 'yearsOfService': yearS}
    return data

def evaluate_performance(data):
    Poor = 0
    Average = 0
    Good = 0
    Excellent = 0
    Performance = ""
    if data['salesTarget'] < 80:
        Poor += 1
    elif data['salesTarget'] <= 100:
        Average += 1
    elif data['salesTarget'] <= 120:
        Good += 1
    else:
        Excellent += 1
    
    if data['customerSatisfaction'] < 6:
        Poor += 1
    elif data['customerSatisfaction'] <= 7:
        Average += 1
    elif data['customerSatisfaction'] <= 9:
        Good += 1
    else:
        Excellent += 1
    
    if data['attendance'] < 20:
        Poor += 1
    elif data['attendance'] <= 24:
        Average += 1
    elif data['attendance'] <= 27:
        Good += 1
    else:
        Excellent += 1

    if data['peerFeedback'] < 4:
        Poor += 1
    elif data['peerFeedback'] <= 6:
        Average += 1
    elif data['peerFeedback'] <= 8:
        Good += 1
    else:
        Excellent += 1

    if Excellent == 4:
        Performance = "Outstanding"
    elif Poor == 2:
        Performance = "Needs Improvement"
    elif Good == 3:
        Performance = "Strong Performer"
    else:
        Performance = "Satisfactory"
    data2 = {'PerformanceRating': Performance, 'yearsOfService': data['yearsOfService']}
    return data2

def calculate_bonus(data):
    Bonus = 0
    if data['PerformanceRating'] == "Outstanding":
        Bonus = 1000
    elif data['PerformanceRating'] == "Needs Improvement":
        Bonus = 800
    elif data['PerformanceRating'] == "Strong Performer":
        Bonus = 500
    elif data['PerformanceRating'] == "Satisfactory":
        Bonus = 200
    
    if data['yearsOfService'] < 2:
        Bonus *= 1
    elif data['yearsOfService'] <= 5:
        Bonus *= 1.5
    else:
        Bonus *= 2
    return Bonus

data = get_info()
data2 = evaluate_performance(data)
Bonus = calculate_bonus(data2)
print(f"The annual bonus for the performance rating of: {data2['PerformanceRating']} and years of service of {data2['yearsOfService']} is:\n{Bonus}")


