# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 01:49:03 2020

@author: nitin
"""

def leafNode(node): # Return True if leaf node
    return not node.left and not node.right

def matches_target(node, target): # Return True if leaf value matches target
    return node.val == target

class Solution(object):
    
    def DFS_helper(self, current, target): # DFS
        if current:
            if current.left:
                current.left.parent = current
                if not leafNode(current.left): 
                    self.DFS_helper(current.left,target)
                else: # If leaf node and matches target, remove the reference
                    if matches_target(current.left, target):
                        current.left = None
                        
            if current.right:
                current.right.parent = current
                if not leafNode(current.right):
                    self.DFS_helper(current.right,target)
                else: # If leaf node and matches target, remove the reference
                    if matches_target(current.right, target):
                        current.right = None
            
            # If current becomes leaf node and matches target, remove reference to current
            if leafNode(current) and matches_target(current, target):
                if current.parent:
                    if current.parent.left is current:
                        current.parent.left = None
                    else:
                        current.parent.right = None
                
                
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        
        root.parent = None
        
        self.DFS_helper(root, target)
        
        # Check if root is now a leaf node and matches target
        if leafNode(root) and matches_target(root, target):
            root = None
            
        return root
        