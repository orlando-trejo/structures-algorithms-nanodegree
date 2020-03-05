#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 19:57:23 2019

@author: otrejo
"""

daysofMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
    
def createN(N):
    lst = [1]
    for i in range(2,N+1):
        lst.append(i)
        
    return lst


def isN(lst):
    N = len(lst)
    ref = createN(N)
    #print(ref)
    lst = lst
    lst.sort()
    #print(lst)
    return lst == ref

print(isN([1,2,3]))