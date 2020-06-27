# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:41:26 2020

@author: nitin
"""

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        cnt = 0
        idx = 0
        
        while idx<=len(nums)-1:
            if idx == 0: 
                if nums[idx]>nums[idx+1]: # If First Element is not in order
                    cnt+=1
                    nums[idx]=nums[idx+1] # Modify and update cnt
            elif idx == len(nums)-1:
                    if nums[idx]<nums[idx-1]: # If last element is not in order
                        cnt+=1 # update cnt; no need to modify since there are no more elements to check
            
            else: # for internal elements
                if nums[idx-1]>nums[idx]>nums[idx+1]: # 3 elements in Decreasing order
                    return False # return false; cant do it by modifying at most 1 element
                
                elif nums[idx-1]>nums[idx]: # previous element not in order
                    if nums[idx+1] >= nums[idx-1]: # if the adjacent elements are in order
                        nums[idx] = nums[idx-1] # Modify the current element
                    else:
                        nums[idx-1]=nums[idx] # else modify the previous element
                    cnt+=1 #update cnt and modify
                    
                elif nums[idx+1]<nums[idx]: #next element not in order
                    if nums[idx+1] >= nums[idx-1]: # if the adjacent elements are in order
                        nums[idx] = nums[idx-1] # modify current element
                    else:
                        nums[idx+1] = nums[idx] # else modify the next element
                    cnt+=1                   # update cnt and modify
                #else the 3 elements are in order
            if cnt==2:
                return False
            
            idx+=1
            
        return True