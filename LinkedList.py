# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:23:38 2020

@author: nitin
"""

class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self,new_element):
        current = self.head
        
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def insert(self, new_element, position):
        current = self.head
        if position < 1:
            return ValueError
        else:
            counter = 1
            previous = None
            while(counter < position and current.next):
                previous = current
                current = current.next
                counter += 1
                
            if counter < position:
                return ValueError
            else:
                if previous :
                    previous.next = new_element
                    new_element.next = current
                else:
                    new_head = new_element
                    new_head.next = self.head
                    self.head = new_head
    
    def delete(self, position):
        current = self.head
        if position < 1 :
            return ValueError
        else:
            previous = None
            counter = 1
            while(counter < position and current.next):
                previous = current
                current = current.next
                counter += 1
            
            if counter < position:
                return ValueError
            else:
                if previous:
                    deleted = current
                    previous.next = current.next
                    deleted.next = None
                else:
                    deleted = self.head
                    self.head = self.head.next
                    deleted.next = None
                    
                return deleted
            
    def print(self):
        if self.head:
            print("LinkedList:")
            current = self.head
            while(current):
                print(current.value)
                current = current.next
        else:
            return ValueError
        
    def get_position(self, position):
        current = self.head
        
        if position < 1:
            return ValueError
        else:
            counter = 1
            while(counter < position and current):
                current = current.next
                counter += 1
            if(counter == position):
                return current
            else:
                return ValueError

e1 = Element(10)
e2 = Element(20)
e3 = Element(30)
            
LL = LinkedList(e1) # Intitialize new LinkedList object with e1 as head
print(LL.head.value) # Should be 10

# Append
LL.append(e2)  # Append e2 to the LinkedList
print(LL.head.next.value) # Should be 20

# Insert
LL.insert(e3, 2) # Insert e2 in the second position
print(LL.head.next.value) # Should now be 30             
print(LL.head.next.next.value) # e2 should have shifted right by one position; Should be 20

# Delete
print(LL.delete(1).value) # Should be 10
print(LL.head.value) # Should be 30
e4 = Element(40)
LL.append(e4)
print(LL.delete(2).value) # Should be 20
print(LL.head.next.value) # Should be 40

# Print
print()
LL.print()
print()

# Getting the 2nd Node value
print(LL.get_position(2).value) # Should be 40
LL.insert(e1, 2)
print(LL.get_position(2).value) # Should be now 10
  
            