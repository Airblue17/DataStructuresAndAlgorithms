# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 01:05:06 2020

@author: nitin
"""

def decodeAtIndex(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
   

    decoded_size = 0
    
    for c in S:
        if c.isdigit():
            decoded_size *= int(c)
        else:
            decoded_size += 1
            
    for c in reversed(S):
        K = K % decoded_size
        if K == 0 and c.isalpha():
            return c
        if c.isdigit():
            decoded_size /= int(c)
        else:
            decoded_size -= 1