# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:45:08 2020

@author: nitin
"""

class Solution(object):
    def traverse(self, root, current):
        if current:
            if current.left:
                #print("left", current.left)
                current.left.bigger_ancestor = list(current.bigger_ancestor)
                current.left.smaller_ancestor = list(current.smaller_ancestor)
                current.left.smaller_ancestor.append(current.val)
                #print("left bigger:", current.left.bigger_ancestor)
                #print("left smaller:", current.left.smaller_ancestor)
                cond1 = all(current.left.val < ancestorVal for ancestorVal in current.left.smaller_ancestor)
                cond2 = all(current.left.val > ancestorVal for ancestorVal in current.left.bigger_ancestor)
                #print(cond1)
                #print(cond2)
                #print "\n"
                if cond1 and cond2:
                     self.traverse(root, current.left)
                else:
                    root.valid = False
                    return
            if current.right:
                #print("right", current.right)
                current.right.bigger_ancestor = list(current.bigger_ancestor)
                current.right.smaller_ancestor = list(current.smaller_ancestor)
                current.right.bigger_ancestor.append(current.val)
                #print("right bigger:", current.right.bigger_ancestor)
                #print("right smaller:", current.right.smaller_ancestor)
                cond1 = all(current.right.val < ancestorVal for ancestorVal in current.right.smaller_ancestor)
                cond2 = all(current.right.val > ancestorVal for ancestorVal in current.right.bigger_ancestor)
                #print(cond1)
                #print(cond2)
                #print "\n"
                if cond1 and cond2:
                     self.traverse(root, current.right)
                else:
                    root.valid = False
                    return
                
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        root.bigger_ancestor = []
        root.smaller_ancestor = []
        root.valid = True
        self.traverse(root, root)
        return root.valid