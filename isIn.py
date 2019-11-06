# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:23:34 2019

@author: Seb
"""

def isIn(char, inputStr):
    
    if len(inputStr) == 0:
        return False
    elif len(inputStr) ==1:
        return char == inputStr
    else:
        if inputStr[0] == char or inputStr[-1]==char:
            return True
        else:
            return isIn(char, inputStr[1:-1])
        
print(isIn('a', 'abc'))
        



    