# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 23:05:46 2020

@author: nitin
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    current = head
    
    prev = None
    
    def swap(current, Next):
        current.next = Next.next
        Next.next = current
        
    while current:
        if current.next:
            if current is head:
                head = current.next
                current.next = head.next
                head.next = current
                prev = current
                current = current.next
            else:
                Next = current.next 
                currentNode = current
                swap(currentNode, Next)
                prev.next = Next
                prev = currentNode
                current = currentNode.next
        else:
            current = current.next
            
    return head

LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)

swapLL = swapPairs(LL)

current = swapLL

while current:
    print(current.val)
    current = current.next