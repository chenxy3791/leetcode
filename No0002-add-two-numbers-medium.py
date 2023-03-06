# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:16:51 2021

@author: chenxy

2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 
提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from utils.SinglyLinkedList import ListNode 
from utils.SinglyLinkedList import create_SinglyLinkedList
from utils.SinglyLinkedList import print_linkedlist
 
class Solution:
    def append_ListNode(self, val, head):        
        if head != None:
            curNode = head
            while curNode.next is not None:
                curNode = curNode.next    
            curNode.next = ListNode(val, None)                                                     
        else:
            head = ListNode(val, None)
        return head
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        c,p1,p2  = 0,l1,l2
        
        while p1 != None or p2 != None:
            op1 = 0 if p1==None else p1.val                
            op2 = 0 if p2==None else p2.val            
            s = op1 + op2 + c
            val,c = s%10, s//10
            head = self.append_ListNode(val, head)                

            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
                
        if c > 0:
            head = self.append_ListNode(c, head)
            
        return head
        
if __name__ == '__main__':        
    
    sln = Solution()
    
    l1 = create_SinglyLinkedList([2,4,3])
    l2 = create_SinglyLinkedList([5,6,4])
    rslt = sln.addTwoNumbers(l1, l2)
    print_linkedlist(rslt)

    l1 = create_SinglyLinkedList([0])
    l2 = create_SinglyLinkedList([0])
    rslt = sln.addTwoNumbers(l1, l2)
    print_linkedlist(rslt)    
    
    l1 = create_SinglyLinkedList([0])
    l2 = create_SinglyLinkedList([2])
    rslt = sln.addTwoNumbers(l1, l2)
    print_linkedlist(rslt)    

    l1 = create_SinglyLinkedList([9,9,9,9,9,9,9])
    l2 = create_SinglyLinkedList([9,9,9,9])
    rslt = sln.addTwoNumbers(l1, l2)
    print_linkedlist(rslt)        
    
    l1 = create_SinglyLinkedList([1,0,1,9,8,9,9,9])
    l2 = create_SinglyLinkedList([9,9,8,2,4,5])
    rslt = sln.addTwoNumbers(l1, l2)
    print_linkedlist(rslt)        