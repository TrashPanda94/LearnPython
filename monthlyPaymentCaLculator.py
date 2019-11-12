# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:42:03 2019

@author: Seb
"""

balance = 3926
annualInterestRate = 0.2
mRate = annualInterestRate/12
ret = 10
def enough(balance, mRate):
        for i in range (1,13):
            balance = balance - ret
            balance = balance*(1+mRate)
        return (balance > 0)
while(enough(balance, mRate)):
    ret +=10
print (ret)

