# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:55:02 2020

@author: nitin
"""

def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums: return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])

    return root