# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:33:45 2020

@author: nitin
"""


# Time Complexity:
# Worst Case: O(n^2)
def bubbleSort(arr):
    n = len(arr)
    itr = 1
    
    while itr <= n-1:
        compr = 1
        i = 0
        while compr <= n-1:
            j = i+1
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i+=1
            compr+=1
        itr+=1
    return arr

arr = [21,4,1,3,9,20,25,6,21,14]


    
print(bubbleSort(arr))