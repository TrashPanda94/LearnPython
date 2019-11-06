# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:57:30 2019

@author: Seb
"""
# check if an input str is of the palindrome pattern

def palindromeSolver(inputStr):
    if len(inputStr) == 0 or len(inputStr) ==1 :
        return True
    else: 
        if inputStr[0] == inputStr[-1]:
            return palindromeSolver(inputStr[1:-1])
        else:
            return False;


print(palindromeSolver('aba'))