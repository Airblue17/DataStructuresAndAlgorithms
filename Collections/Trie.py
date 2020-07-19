# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:17:39 2020

@author: nitin
"""

class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    
    def getCharIndex(self, char):
        return ord(char) - ord('a')
    
    def insert(self, key):
        
        curr = self.root
        
        for char in key:
            index = self.getCharIndex(char)
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        
        curr.isEndOfWord = True
        
        
    def search(self, key):
        # Complexity: Time - O(M) ; M = length of key
        curr = self.root
        
        for char in key:
            index = self.getCharIndex(char)
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        
        return curr and curr.isEndOfWord
        
    
keys = ["the","a","there","anaswe","any", "by","their"] 

output = ["Not present in trie", "Present in trie"] 
trie = Trie()
for key in keys: 
   trie.insert(key) 
   

print("{} ---- {}".format("the",output[trie.search("the")])) 
print("{} ---- {}".format("these",output[trie.search("these")])) 
print("{} ---- {}".format("their",output[trie.search("their")])) 
print("{} ---- {}".format("thaw",output[trie.search("thaw")])) 
  
                