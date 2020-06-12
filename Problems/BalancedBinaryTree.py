# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:46:29 2020

@author: nitin
"""

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        self.balanced = True
        
        def Balanced(left, right):
            return abs(left - right)<=1
        
        def get_subtree_key(current):
            if not current: return 0
            left_subtree_h = get_subtree_key(current.left)
            right_subtree_h = get_subtree_key(current.right)
            #print current.val, left_subtree_h, right_subtree_h
            if not Balanced(left_subtree_h, right_subtree_h):
                self.balanced = False
                
            return max(left_subtree_h + 1, right_subtree_h + 1)
        
        get_subtree_key(root)
        
        return self.balanced