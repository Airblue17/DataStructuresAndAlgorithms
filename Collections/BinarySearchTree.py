# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:08:50 2020

@author: nitin
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree(object):
    def __init__(self, rootValue):
        self.root = Node(rootValue)
        
    def insert(self, newNodeVal):
        current = self.root
        
        if not current:
            current.value = newNodeVal
            return
        
        while current:
            if newNodeVal <= current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(newNodeVal)
                    return
                    
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(newNodeVal)
                    return
                
    def search(self, findVal):
        current = self.root
        
        while current:
            if current.value == findVal:
                return True
            if findVal < current.value:
                if current.left:
                    current = current.left
                else:
                    return False
            else:
                if current.right:
                    current = current.right
                else:
                    return False
        return False
    
    def recursiveSearch(self, start, findVal):
        if start:
            if start.value == findVal:
                return True
            elif findVal < start.value:
                return self.recursiveSearch(start.left, findVal)
            else:
                return self.recursiveSearch(start.right, findVal)
        return False
    
    def print_tree(self, start, traversal):
        # Preorder Traversal
        if start:
            traversal.append(str(start.value))
            traversal = self.print_tree(start.left, traversal)
            traversal = self.print_tree(start.right, traversal)
            
        if start != self.root:
            return traversal
        else:
            return '-'.join(traversal)
# Set up tree
tree = BinarySearchTree(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
                    
# search
# Should be True
print(tree.search(1))
# Should be False
print(tree.search(6))  

# Recursive
print("With Recursion:")
print(tree.recursiveSearch(tree.root, 12)) # Should be False
print(tree.recursiveSearch(tree.root, 3)) # Should be True

# Preorder traversal
traversal = []
print(tree.print_tree(tree.root, traversal))
            