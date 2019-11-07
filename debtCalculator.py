# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:49:40 2019

@author: Seb
"""
balance= 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12

for month in range(1,13):
    balance = balance*(1-monthlyPaymentRate)
    balance = balance*(1+monthlyInterestRate)

balance = round(balance, 2)
str_balance = str(balance)
if str_balance[-1] == '0'and str_balance[-2] == '0':
    str_balance = str_balance[0:-1]
print("Remaining balance: "+str(balance))
