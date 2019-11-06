# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:01:36 2019

@author: Seb
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    counter = min(a,b)
    while (a%counter != 0) or (b%counter != 0):
        counter = counter-1
    return counter


test = gcdIter(17,12)

print(test)