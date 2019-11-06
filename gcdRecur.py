# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:57:30 2019

@author: Seb
"""
def gcdRecur(a,b):
    if b ==0:
        return a
    else:
        return gcdRecur(b, a%b)

test = gcdRecur(17,12)
print(test)