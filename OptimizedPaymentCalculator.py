# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:47:54 2019

@author: Seb


"""

def yearEndBalance(balance, mRate,  mPayment):
    for i in range (1,13):
        balance -= mPayment
        balance = balance*(1+mRate)
    return balance



balance = 999999
annualInterestRate = 0.18
mRate = annualInterestRate/12

lowerBound = balance/12
upperBound = balance*((1+mRate)**12)/12
ret = (lowerBound + upperBound)/2
epsilon = 0.01

while True:
    temp = yearEndBalance(balance, mRate, ret)
    if (abs(temp) <= 0.01):
        break
    elif temp > 0:
        lowerBound = (lowerBound+upperBound)/2
        upperBound = upperBound
        ret = (lowerBound + upperBound)/2
    else:   #temp<0
        lowerBound = lowerBound
        upperBound = (lowerBound+upperBound)/2
        ret = (lowerBound + upperBound)/2
        
print(round(ret,2))
    





        
    