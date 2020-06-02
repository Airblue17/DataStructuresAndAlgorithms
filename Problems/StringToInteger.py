# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 03:42:01 2020

@author: nitin
"""

def Atoi(str):
    str = str.strip()
    if len(str) == 0:
        return 0
    
    index = 0
    res = []
    neg = False
    
    if str[index] == '+':
        index += 1
    elif str[index] == '-':
        neg = True
        index+=1
        
    while index < len(str) and str[index].isdigit():
        res.append(str[index])
        index +=1
        
    if not res:
        return 0
    
    res = int(''.join(res))
    
    int_min = -2**31
    int_max = -1*int_min - 1
    
    if neg:
        res *= -1
        if res < int_min:
            return int_min
        
    if res > int_max:
        return int_max
    
    return res

print(Atoi("   -3.4"))