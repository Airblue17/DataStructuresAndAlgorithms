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
                # Assign the 2nd node as head
                head = current.next
                # Current = Old Head 
                # So update its next to point to the 2nd Node Next 
                current.next = head.next
                # update New Head (2nd Node) next to point to the old head(current)
                head.next = current
                prev = current
                # Go to the 3rd node
                current = current.next
            else:
                Next = current.next 
                currentNode = current
                swap(currentNode, Next)
                # Update the pointer of the node thats just before the node that was swapped
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