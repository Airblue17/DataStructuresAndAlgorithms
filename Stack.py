# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:04:16 2020

@author: nitin
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, top = None):
        self.top = top
        
    def insert_top(self, new_element):

        if self.top:
            new_element.next = self.top
            self.top = new_element
        else:
            self.top = new_element
            
    def delete_top(self):
        
        if self.top:
            deleted = self.top
            self.top = self.top.next
            deleted.next= None
            return deleted
        else:
            return ValueError
            
    def print(self):
        if self.top:
            print("Stack:")
            current = self.top
            while(current):
                print(current.value)
                current = current.next
        else:
            print("stack empty")
        
class Stack(object):
    def __init__(self, LL = None):
        self.LL = LL
        
    def push(self, new_element):
        self.LL.insert_top(new_element)
        
    def pop(self):
        return self.LL.delete_top()
    
    def print_stack(self):
         self.LL.print()
        
e1 = Element(10)
e2 = Element(20)

# Initialization
stk = Stack(LinkedList(e1))

print(stk.LL.top.value) # Should be 10

# Push
stk.push(e2)

print(stk.LL.top.value) # Should be 20

print(stk.LL.top.next.value) # Should be 10

# Pop

print(stk.pop().value) # Should be 20

print(stk.LL.top.value) # Should be 10 

# Print
print()
stk.print_stack()