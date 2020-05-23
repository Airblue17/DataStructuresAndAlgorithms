# -*- coding: utf-8 -*-
"""
Created on Sat May 23 04:46:51 2020

@author: nitin
"""

arr = [21,4,1,3,9,20,25,6,21,14]


def partition(arr, begin, end):
    pivot=arr[end]
    pivotIdx = end
    
    i=0
    
    while i<pivotIdx:
        while arr[i]>pivot:
            arr[i], arr[pivotIdx-1] = arr[pivotIdx-1], arr[i]
            arr[pivotIdx], arr[pivotIdx-1] = arr[pivotIdx-1], arr[pivotIdx]
            pivotIdx -= 1
            pivot = arr[pivotIdx]
        i+=1
        
    return pivotIdx

def quickSort(arr, begin, end):
    if begin>=end:
        return
    else:
        pivotIdx = partition(arr, begin, end)
        quickSort(arr, begin, pivotIdx-1)
        quickSort(arr, pivotIdx+1, end)
        return arr
    
    
print(quickSort(arr,0, len(arr)-1))