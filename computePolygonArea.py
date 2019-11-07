# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:17:40 2019

@author: Seb
"""

import math
def polysum(n,s):
    ret = 0.25*n*s*s/math.tan(math.pi/n)
    ret = ret + (n*s)**2
    ret = round(ret, 4)
    return ret

    
    