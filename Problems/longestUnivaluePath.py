# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 02:58:05 2020

@author: nitin
"""

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.longest = 0
        def dfs(current):
            if not current: return  0
            left_length = dfs(current.left)
            right_length = dfs(current.right)
            left_arrow = right_arrow = 0
            
            if current.left and current.left.val == current.val:
                left_arrow = left_length + 1
            if current.right and current.right.val == current.val:
                right_arrow = right_length + 1
            
            self.longest = max(self.longest, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

                    
        dfs(root)
        
        return self.longest