# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:23:35 2020

@author: nitin
"""

from collections import Counter
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        
        s_to_t = s
        letter_mappings = {}
        
        s_to_t = list(s_to_t)
        for idx, letter in enumerate(s):
            if letter not in letter_mappings:
                letter_mappings[letter] = t[idx]
                s_to_t[idx] = letter_mappings[letter]
            else:
                s_to_t[idx] = letter_mappings[letter]
        
        if len(set(letter_mappings.values())) != len(letter_mappings.values()):
            return False
        s_to_t = "".join(s_to_t)
        
        if s_to_t == t:
            return True
        return False