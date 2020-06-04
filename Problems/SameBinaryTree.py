# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 00:40:56 2020

@author: nitin
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    def preorder(p, q):
        if p and q:
            if p.val == q.val:
                if not preorder(p.left, q.left) or not preorder(p.right, q.right):
                    return False
                return True
            else:
                return False
            
        if (p and not q) or (not p and q):
            return False
        
        if not p and not q:
            return True
        

    return preorder(p, q)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)


tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

print(isSameTree(tree1, tree2))
