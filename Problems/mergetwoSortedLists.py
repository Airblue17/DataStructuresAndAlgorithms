# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:32:55 2020

@author: nitin
"""

class Solution:        
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a           
            a.next = self.mergeTwoLists(a.next, b)
        return a or b