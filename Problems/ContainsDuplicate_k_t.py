# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:29:40 2020

@author: nitin
"""

'''
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference
between i and j is at most k.
'''

def containsNearbyAlmostDuplicate(nums, k, t):
    buckets = {}

    for idx, digit in enumerate(nums):
        # either the digit to satisfy the conditon is in the same bucket or the immediate adjacent bucket(either left/right)
        bucketNum, offset = (digit/t, 1) if t else (digit, 0) # t == 0 is a special case

        for bucketIdx in range(bucketNum - offset, bucketNum + offset + 1):
            if bucketIdx in buckets and abs(buckets[bucketIdx] - digit) <= t:
                return True
        
        # If not match found, store the value
        buckets[bucketNum] = nums[idx]

        if len(buckets) > k: # To satisfy conditon on k, keep at most k buckets
            del buckets[nums[idx-k]/t if t else nums[idx-k]] # remove farthest bucket

    return False

nums = [1,2,3,1]
k = 3
t = 0

print(containsNearbyAlmostDuplicate(nums, k, t))