# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:49:39 2019

@author: chenxy

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative method
        prevNode = None                
        nextNode = head # Next node to be handled
        curNode  = head
        
        while (nextNode != None):
            curNode  = nextNode            
            nextNode = curNode.next # Memoization of nextNode for the next iteration
            
            # Update curNode's next
            curNode.next = prevNode
            
            # Update prevNode for the next iteration
            prevNode = curNode
            
        head = curNode
        
        return head

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        # Recursive method
        if head.next == None:
            return head

        subReverse = 
        
        prevNode = None                
        nextNode = head # Next node to be handled
        curNode  = head
        
        while (nextNode != None):
            curNode  = nextNode            
            nextNode = curNode.next # Memoization of nextNode for the next iteration
            
            # Update curNode's next
            curNode.next = prevNode
            
            # Update prevNode for the next iteration
            prevNode = curNode
            
        head = curNode
        
        return head

if __name__ == '__main__':    
    
    # Create a singly-linked list
    node1 = ListNode(1)
    
    node2 = ListNode(2)
    node1.next = node2

    node3 = ListNode(3)
    node2.next = node3    

    node4 = ListNode(4)
    node3.next = node4
    
    sln = Solution()            
    head = sln.reverseList(node1)
    
    print(head.val)
    print(head.next.val)            
    print(head.next.next.val)            
    print(head.next.next.next.val)            