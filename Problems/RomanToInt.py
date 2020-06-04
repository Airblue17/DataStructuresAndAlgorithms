# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:51:45 2020

@author: nitin
"""

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    
    roman = list(s)

    valDict ={'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}

    def subtract(current, Next):
        if current == 'I' and (Next == 'V' or Next == 'X'):
            return True
        elif current == 'X' and (Next == 'L' or Next == 'C'):
            return True
        elif current == 'C' and (Next == 'D' or Next == 'M'):
            return True
        else:
            return False

    digit = 0
    idx = 0
    while idx < len(roman):
        current = roman[idx]
        Next = None
        
        if idx + 1 < len(roman):
            Next = roman[idx+1]
            
        if Next:
            if subtract(current, Next):
                digit += valDict[Next] - valDict[current]
                idx += 2
            else:
                digit += valDict[current]
                idx += 1
        else:
            digit += valDict[current]
            idx += 1
            
    return digit

roman = "MCMXCIV"

print(romanToInt(roman))