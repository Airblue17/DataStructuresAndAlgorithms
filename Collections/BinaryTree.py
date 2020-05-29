# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:17:10 2020

@author: nitin
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, rootValue):
        self.root = Node(rootValue)
        
    def search(self, findVal):
        # Pre-Order Search
        # Worst Case: O(n)
        current = self.root
        nodes_list = []
        
        current.visited = True
        nodes_list.append(current)
        
        self._clearChildVisit(current) # Set Left and right child visit status to False
            
        while nodes_list:
            current.visited = True
            
            if current.value == findVal:
                return True
            
            if current.left and not current.left.visited: # If Left Child exists and not visited
                current = current.left
                nodes_list.append(current)
                
                self._clearChildVisit(current)
            elif current.right and not current.right.visited: # If right child exists and not visited
                current = current.right
                nodes_list.append(current)
                
                self._clearChildVisit(current)
            else: # Either leaf node or all childs visited
                nodes_list.pop() 
                if len(nodes_list) != 0:
                    current = nodes_list[-1]
                
        return False
    
    def _clearChildVisit(self, node):
        if node.left:
            node.left.visited = False
        if node.right:
            node.right.visited = False
            
    def print_tree(self):
        # Pre-Order Search
        # Worst Case: O(n)
        current = self.root
        nodes_list = []
        
        current.visited = True
        nodes_list.append(current)
        
        self._clearChildVisit(current) # Set Left and right child visit status to False
          
        traversal = []
        traversal.append(str(current.value))
        while nodes_list:
            
            if current.left and not current.left.visited: # If Left Child exists and not visited
                current = current.left
                nodes_list.append(current)
                current.visited = True
                traversal.append(str(current.value))
                self._clearChildVisit(current)
                
            elif current.right and not current.right.visited: # If right child exists and not visited
                current = current.right
                nodes_list.append(current)
                current.visited = True
                traversal.append(str(current.value))
                self._clearChildVisit(current)
            else: # Either leaf node or all childs visited
                nodes_list.pop() 
                if len(nodes_list) != 0:
                    current = nodes_list[-1]
        
        return '-'.join(traversal)
    
    def preorder_search(self, start, findVal):
        if start:
            if start.value == findVal:
                return True
            
            return self.preorder_search(start.left,findVal) or self.preorder_search(start.right,findVal)
            
        return False
    
    def preorder_print(self, start, traversal):
        if start:
            traversal.append(str(start.value))
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            
        if start != self.root:
            return traversal
        else:
            return '-'.join(traversal)
                
            
            
        
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(2))
# Should be False
print(tree.search(10))


# Test print_tree
# Should be 1-2-4-5-3
print("Pre-order:",tree.print_tree())

# Recursive Search
print("With Recursion:")
print(tree.preorder_search(tree.root,2)) # Should be True
print(tree.preorder_search(tree.root,10)) # Should be False

# Recurvsive Print
traversal = []
print(tree.preorder_print(tree.root, traversal))
