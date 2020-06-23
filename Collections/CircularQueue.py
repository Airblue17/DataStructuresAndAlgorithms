# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 23:16:44 2020

@author: nitin
"""

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = 0
        self.cap = k
        self.storage = [0]*k
        self.head = self.rear = -1
        
    def next_element_idx(self, idx):
        return 0 if idx == self.cap -1 else idx+1
    
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.storage[0] = value
            self.size +=1
            self.head = 0
            self.rear = 0
            return True
        
        if self.size == self.cap:
            return False
        
        newIdx = self.next_element_idx(self.rear)
        
        self.storage[newIdx]  = value
        self.size += 1
        self.rear = newIdx
        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.storage[self.head] = 0
        self.size -= 1
        self.head = self.next_element_idx(self.head)
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.storage[self.head]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.storage[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()