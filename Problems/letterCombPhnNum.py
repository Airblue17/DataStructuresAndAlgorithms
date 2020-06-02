# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 01:55:31 2020

@author: nitin
"""

letterDict={}
letterDict[2] = ['a','b','c']
letterDict[3] = ['d','e','f']
letterDict[4] = ['g','h','i']
letterDict[5] = ['j','k','l']
letterDict[6] = ['m','n','o']
letterDict[7] = ['p','q','r','s']
letterDict[8] = ['t','u','v']
letterDict[9] = ['w','x','y','z']

digits = "9762"


index = 0

res = []

while index < len(digits):
    currentNum = int(digits[index])
    currentLetterList = letterDict[currentNum]
    if not res:
        res = currentLetterList
    else:
        res = [i+j for i in res for j in currentLetterList]
    index +=1
    
print(res)
    