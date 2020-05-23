# -*- coding: utf-8 -*-
"""
Created on Sat May 23 03:58:36 2020

@author: nitin
"""

def binarySearch(arr, value):
    begin=0
    end=len(arr)
    
    while True :        
        if  begin>=end:
            return -1 # If the value is not found
        else:
            mid = begin +(end-begin)//2
            mid_val = arr[mid]
            if  value>mid_val:
                begin=mid+1
            elif value<mid_val :
                end=mid
            else:
                return mid
            
def binarySearchRecursive(arr, begin,end,value):
    if begin>=end:
        return -1
    else:
        mid = begin +(end-begin)//2
        mid_val = arr[mid]
        if  value>mid_val:
            return binarySearchRecursive(arr,mid+1,end,value)
        elif value<mid_val :
            return binarySearchRecursive(arr,begin,mid,value)
        else:
            return mid
        
            
arr = [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]

print(binarySearch(arr,25)) # Should be 9
print(binarySearch(arr,55)) # Should be -1


# Recursive Binary Search
print()
print(binarySearchRecursive(arr,0,len(arr),0)) # Should be -1
print(binarySearchRecursive(arr,0,len(arr),4)) # Should be 2