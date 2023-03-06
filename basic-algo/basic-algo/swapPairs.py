# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 15:57:16 2019

@author: chenxy
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if head == None:
            print('base case 0')            
            return head        
        if head.next == None:
            print('base case 1')
            return head
        if head.next.next == None:
            newHead = head.next
            newHead.next = head
            newHead.next.next = None
            print('base case 2')
            return newHead
        
        # recursive call
        newSubHead = self.swapPairs(head.next.next)
        
        newHead = head.next
        newHead.next = head
        newHead.next.next = newSubHead
        
        return newHead
    
if __name__ == '__main__':    
    # [1,2,3,4]    
    a0 = ListNode(1);
    a1 = ListNode(2);
    a2 = ListNode(3);
    a3 = ListNode(4);
    
    a0.next = a1;
    a1.next = a2;
    a2.next = a3;
    
    sln = Solution();
    a0_swap = sln.swapPairs(a0)
    
    print(a0_swap.val)
    print(a0_swap.next.val)
    print(a0_swap.next.next.val)
    print(a0_swap.next.next.next.val)
    
    
    