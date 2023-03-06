# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 07:28:51 2021

@author: chenxy

83. 删除排序链表中的重复元素
存在一个按升序排列的链表，给你这个链表的头节点head，请你删除所有重复的元素，使每个元素只出现一次。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：

链表中节点数目在范围 [0, 300] 内-100 <= Node.val <= 100题目数据保证链表已经按升序排列

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import myPackage.SinglyLinkedList as SLL
from myPackage.SinglyLinkedList import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curNode = head
        
        while curNode is not None and curNode.next is not None:
            #print(curNode.val, curNode.next)
            prevNode = curNode
            curNode  = curNode.next
            while curNode is not None and curNode.val == prevNode.val:                
                prevNode.next = curNode.next
                curNode       = curNode.next        
        return head

if __name__ == '__main__':        
    #import time
    sln = Solution()

    a = [2, 3, 1, 0, 2, 5, 3]
    a.sort()
    print(a)
    head = SLL.create_SinglyLinkedList(a)
    head = sln.deleteDuplicates(head)
    SLL.print_linkedlist(head)

    a = [1, 1, 1]    
    print(a)
    head = SLL.create_SinglyLinkedList(a)
    head = sln.deleteDuplicates(head)
    SLL.print_linkedlist(head)
    
    a = [1, 1, 2]
    print(a)
    head = SLL.create_SinglyLinkedList(a)
    head = sln.deleteDuplicates(head)
    SLL.print_linkedlist(head)

    a = [1,1,2,3,3]
    print(a)
    head = SLL.create_SinglyLinkedList(a)
    head = sln.deleteDuplicates(head)
    SLL.print_linkedlist(head)    