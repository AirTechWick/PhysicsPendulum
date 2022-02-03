# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:58:32 2022

@author: erikr
"""

import numpy as np
import matplotlib.pyplot as plt

data_1 = np.loadtxt("pendulum_1.txt")
data_2 = np.loadtxt("pendulum_2.txt")
data_3 = np.loadtxt("pendulum_3.txt")

length_1 = data_1[:,0]
length_2 = data_2[:,0]
length_3 = data_3[:,0]
length_4 = []

period_1 = data_1[:,1]
period_2 = data_2[:,1]
period_3 = data_3[:,1]
period_4 = []


def ln(L):
    m = 1/2
    x = np.log(L)
    b = np.log(2)
    return m * x + b

def T(L):
    k = 2
    return k * (L**(1/2))
       
    
for i in range(0, len(data_1)):   
    avg_len = np.average(length_1[i]) / 3 + np.average(length_2[i]) / 3 + np.average(length_3[i]) / 3
    avg_per = np.average(period_1[i]) / 3 + np.average(period_2[i]) / 3 + np.average(period_3[i]) / 3
    length_4.append(avg_len)
    period_4.append(avg_per)

x_value = np.linspace(0.100, 0.300,25)

plt.scatter(np.log(length_4),period_4) 
plt.plot(np.log(x_value),ln(x_value))
plt.scatter(np.log(length_4), np.log(T(x_value)))