# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:10:08 2020

@author: nitin
"""

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        def dfs(current, level, position, start, end):
            if not current: return 0
            if len(start) == level:
                start.append(position)
                end.append(position)
            else:
                end[level] = position

            cur = end[level] - start[level] + 1
            left = dfs(current.left, level + 1, 2*position, start, end)
            right = dfs(current.right, level + 1, 2*position + 1, start, end)

            return max(cur, max(left, right))

        
        return dfs(root, 0, 1, [], [])
            