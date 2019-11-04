# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:16:21 2019

@author: Yutong
"""
# Bisection Search
# find square root 
# appicable only to numbers >=1
target = float(input("Enter a number: "))
epsilon = 0.02

start = 1
end = target
counter = (start + end)/2

while abs (counter**2 - target) > epsilon and  counter <= target + epsilon:
    if counter**2 >= target+epsilon:
        start = start
        end = (start + end)/2
    else:
        start = (start + end)/2
        end = end
    counter = (start + end)/2

if counter**2 - target > epsilon:
    print('mission failed')
else:
    print(counter)


