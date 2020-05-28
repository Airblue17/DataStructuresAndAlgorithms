# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:57:58 2020

@author: nitin
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoubleLinkedList(object):
    def __init__(self, head = None):
        self.head = head
        
    def append(self, new_element):
        
        
        if not self.head:
            self.head = new_element
            return
        
        current = self.head
        
        while current.next:
            current = current.next
             
        current.next = new_element
        new_element.prev = current
        
    def get_positon(self, position):
        if position<1:
            return ValueError
        else:
            current = self.head
            counter = 1
            while counter < position and current.next:
                current = current.next
                counter +=1 
                
            if counter == position:
                return current.prev, current
            else:
                return ValueError
            
    def insert_at(self, position, new_element):
        prev, current = self.get_positon(position)
        
        if not prev:
            new_element.next = self.head
            self.head.prev = new_element
            self.head = new_element
            return
        else:
            prev.next = new_element
            new_element.prev = prev
            new_element.next = current
            current.prev = new_element
            
    def _clearNodeRef(self, element):
        element.next = None
        element.prev = None
        
    def delete_at(self, position):
        prev, current = self.get_positon(position)
        
        if not prev:
            deleted = self.head
            self.head = self.head.next
            self.head.prev = None
            self._clearNodeRef(deleted)
        else:
            deleted = current
            prev.next = current.next
            if current.next:
                current.next.prev = prev
            self._clearNodeRef(deleted)
        return deleted
     
    def reverse(self):
        current = self.head
        
        while current.next:
            current = current.next
            
        newHead = current
        
        prev = current.prev
        
        while prev:
            prev = current.prev
            current.next, current.prev = current.prev, current.next
            current = prev
            
        newHead.prev = None
        self.head = newHead
            
    def print_ll(self):
        current = self.head
        print("\nLinked List")
        while current:
            print(current.value)
            current = current.next
            
            
        
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
DLL = DoubleLinkedList()

DLL.append(e2)
DLL.append(e3)
e5 = Element(5)
DLL.append(e5)
DLL.print_ll()
DLL.insert_at(1, e1)
print("\nInserted element with value 1 into position 1")
DLL.print_ll()
print("\nInserted element with value 4 into position 4")
DLL.insert_at(4, e4)
DLL.print_ll()

print("\nDeleted", DLL.delete_at(1).value)
DLL.print_ll()

print("\nDeleted", DLL.delete_at(4).value)
DLL.print_ll()

print("\nDeleted", DLL.delete_at(2).value)
DLL.print_ll()

print("\nReversing the Linked List")
DLL.reverse()
print("\n Reversed:")
DLL.print_ll()

DLL.insert_at(2, e1)
print("\nInserted element with value 1 into position 1")


print("\nBack to Original Sequence:")
DLL.reverse()
DLL.print_ll()