# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:14:33 2020

@author: nitin
"""

import heapq 

def WithSorting(arr, k):
    if k-1 > (len(arr)-1) or k-1 < 0 or not arr:
        return ValueError
    arr.sort()
    return arr[k-1]

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

def QuickSelect(arr, begin, end, k):
    if k - 1 > len(arr) - 1 or k -1 < 0 or not arr:
        return ValueError
    if begin <= end:
        pivotIdx = partition(arr, begin, end)
        if pivotIdx == k-1:
            return arr[pivotIdx]
        elif pivotIdx > k-1:
            return  QuickSelect(arr, begin, pivotIdx-1, k)
        else:
            return QuickSelect(arr, pivotIdx+1, end, k)
        
def WithMinHeap(arr, k):
    if k - 1 > len(arr) - 1 or k -1 < 0 or not arr:
        return ValueError
    return heapq.nsmallest(k, arr)[k-1]
    
arr = [21,4,1,3,9,20,25,6,21,14]
arr_sort = arr.copy()
arr_sort.sort()
k = 3

print("Sorted Array:", arr_sort)
print("\nWith Sorting")
print(WithSorting(arr.copy(), k))

print("\nWith QuickSelect")
print(QuickSelect(arr.copy(), 0, len(arr)-1, k))

print("\nWith Min Heap")
print(WithMinHeap(arr.copy(), k))
