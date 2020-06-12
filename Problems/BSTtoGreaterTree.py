# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 19:32:37 2020

@author: nitin
"""


        
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        def DFS_helper(current, currentSum):
            if not current:
                return currentSum
            current.val += DFS_helper(current.right, currentSum)
            return DFS_helper(current.left, current.val)
                
        DFS_helper(root, 0)
        return root