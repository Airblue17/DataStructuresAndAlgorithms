# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:51:13 2020

@author: nitin
"""

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.lastNodeChecked = -float('inf')
        self.ans = float('inf')
        
        def dfs(current):
            if current.left:
                dfs(current.left)
            self.ans = min(self.ans, current.val - self.lastNodeChecked)
            self.lastNodeChecked = current.val
            if current.right:
                dfs(current.right)
                
        
        dfs(root)
        
        return self.ans