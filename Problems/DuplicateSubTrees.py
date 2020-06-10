# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:49:32 2020

@author: nitin
"""

def findDuplicateSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    if not root:
        return
    
    ret_list = []
    subtree = collections.Counter()
    
    def DFS_helper(current):
        if current:
            subtree_key = (current.val, DFS_helper(current.left), DFS_helper(current.right))
            subtree[subtree_key] += 1
            
            if subtree[subtree_key] == 2:
                ret_list.append(current)
            return subtree_key
        else:
            return '#'
        
    
    DFS_helper(root)
    return ret_list