# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:24:35 2020

@author: nitin
"""

class Queue(object):
    def __init__(self, head = None):
        self.storage = [head]
        
    def enqueue(self, new_value):
        self.storage.append(new_value)
        
    def dequeue(self):
        return self.storage.pop(0)
    
    def peek(self):
        return self.storage[0]
      
    def print(self):
        return self.storage

# Initialization  
q1 = Queue(10)

print(q1.peek()) # Should be 10

# Enqueue

q1.enqueue(20)

# Dequeue

print(q1.dequeue()) # Should be 10

print(q1.peek()) # Should now be 20

# Print
print(q1.print())