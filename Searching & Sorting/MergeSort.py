# -*- coding: utf-8 -*-
"""
Created on Sat May 23 04:14:32 2020

@author: nitin
"""

arr = [21,4,1,3,9,20,25,6,21,14]


def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left) # Returns Left Subarray
        mergeSort(right) # Returns Right Subarray
        
        i=0
        j=0
        
        k=0
        
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
            
        while i<len(left):
            arr[k]=left[i]
            k+=1
            i+=1
            
        while j<len(right):
            arr[k] = right[j]
            k+=1 
            j+=1
        
        return arr
    
    
print(mergeSort(arr))