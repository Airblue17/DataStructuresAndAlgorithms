# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:04:51 2020

@author: nitin
"""

class HashTable(object):
    def __init__(self, buckets):
        self.table = [None]*buckets
        
    def calculateHashValue(self, string):
        # Assume string will have atleast 2 letters
        hashVal = ord(string[0]) * 100 + ord(string[1])
        return hashVal
    
    def store(self,string):
        # Store the string in the hash table
        idx = self.calculateHashValue(string)
        
        if self.table[idx]:
            self.table[idx].append(string)
        else:
            self.table[idx] = [string]
            
    def lookup(self, string):
        # return hash value if string is present in hash table. Return -1 if not
        key = self.calculateHashValue(string)
        
        if self.table[key]:
            if string in self.table[key]:
                return key
        return -1
    
hashTable = HashTable(10000)

hashTable.store('Football')

print(hashTable.lookup('Football')) # Should be 7111

print(hashTable.lookup('Food')) #Should be -1

hashTable.store('Food')

print(hashTable.lookup('Food')) # Should be 7111