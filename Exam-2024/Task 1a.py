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

    data = {'salesTarget': salesT, 'customerSatisfaction': customorS, 'attendance': attendance, 'peerFeedback': peerF}
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
        Performance = "Needs improvement"
    elif Good == 3:
        Performance = "Strong Performer"
    else:
        Performance = "Satisfactory"

    return Performance

data = get_info()
Performance = evaluate_performance(data)
print(f"The employees performance evaluation is: {Performance}")
