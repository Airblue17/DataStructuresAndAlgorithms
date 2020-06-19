# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:45:21 2020

@author: nitin
"""

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        
        height = -1
        
        nodes = 0
        tree = []
        lastNode = 0
        
        while label > nodes:
            height +=1
            nodes += 2**height  
            if (height+1)%2 !=0:
                tree.append([i for i in range(lastNode+1,nodes+1)])
                lastNode = tree[-1][-1]
            else:
                tree.append([i for i in range(nodes,lastNode,-1)])
                lastNode = tree[-1][0]
                
        currentNode = label
        traversal = []
        traversal.append(currentNode)
        idx = len(tree)-1
        
        while idx>=0:
            currentPos = tree[idx].index(currentNode) + 1
            childNodes = 2
            if idx-1 >=0:
                for parent in tree[idx-1]:
                    if currentPos <= childNodes:
                        traversal.append(parent)
                        currentNode = parent
                        break
                    childNodes += 2
            idx -= 1
                    
        traversal.reverse()    
        
        return traversal