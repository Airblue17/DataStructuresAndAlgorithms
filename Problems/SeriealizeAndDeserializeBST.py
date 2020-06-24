# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:03:34 2020

@author: nitin
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(current):
            if not current:return []
            return [current.val]+dfs(current.left)+dfs(current.right)
        
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def insert(root, newNode):
            if newNode.val < root.val:
                if root.left:
                    insert(root.left, newNode)
                else:
                    root.left = newNode
            else:
                if root.right:
                    insert(root.right, newNode)
                else:
                    root.right = newNode
                
        def reconstruct(tree, data):
            while data:
                if not tree:
                    tree = TreeNode(data.pop(0))
                else:
                    newNode = TreeNode(data.pop(0))
                    insert(tree, newNode)
        
            return tree
        
        return reconstruct(None, data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))