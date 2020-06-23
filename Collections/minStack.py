# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:03:27 2020

@author: nitin
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage = []
        self.min_elements = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.storage.append(x)
        #print "Push \n storage", self.storage
        if not self.min_elements:
            self.min_elements.append(x)
        elif self.min_elements[-1] >= x:
            self.min_elements.append(x)
            
        #print "min:", self.min_elements
        #print "\n"
        

    def pop(self):
        """
        :rtype: None
        """
        del_top = self.storage.pop()
        if  del_top == self.min_elements[-1]:
            self.min_elements.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.storage[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_elements[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()