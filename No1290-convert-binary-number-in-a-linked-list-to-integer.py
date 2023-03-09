# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:50:10 2023

@author: chenxy
1290. 二进制链表转整数
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

 

示例 1：
输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
示例 2：
输入：head = [0]
输出：0
示例 3：
输入：head = [1]
输出：1
示例 4：
输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
输出：18880
示例 5：
输入：head = [0,0]
输出：0

提示：
链表不为空。
链表的结点总数不超过 30。
每个结点的值不是 0 就是 1。

"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # def getDecimalValue(self, head: ListNode) -> int:
    #     """
    #     执行用时：44 ms, 在所有 Python3 提交中击败了19.17%的用户
    #     内存消耗：14.7 MB, 在所有 Python3 提交中击败了93.80%的用户
    #     居然这么慢!
    #     """
    #     num = 0
    #     while True:
    #         num = 2*num + head.val            
    #         if head.next == None:
    #             break
    #         head = head.next

    #     return num

    def getDecimalValue(self, head: ListNode) -> int:
        """
        执行用时：44 ms, 在所有 Python3 提交中击败了19.17%的用户
        内存消耗：14.7 MB, 在所有 Python3 提交中击败了93.80%的用户
        居然这么慢!
        """
        num = 0
        while True:
            num = (num << 1) | head.val            
            if head.next == None:
                break
            head = head.next

        return num
    
if __name__ == '__main__':

    sln  = Solution()                
    
    a = [1]
    head = ListNode(a[0])
    curNode = head
    for num in a[1:]:
        nextNode = ListNode(num)
        curNode.next = nextNode
        curNode      = nextNode
    print(sln.getDecimalValue(head))           

    a = [0]
    head = ListNode(a[0])
    curNode = head
    for num in a[1:]:
        nextNode = ListNode(num)
        curNode.next = nextNode
        curNode      = nextNode
    print(sln.getDecimalValue(head))           

    a = [1,0,1]
    head = ListNode(a[0])
    curNode = head
    for num in a[1:]:
        nextNode = ListNode(num)
        curNode.next = nextNode
        curNode      = nextNode
    print(sln.getDecimalValue(head))           
    
    a = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
    head = ListNode(a[0])
    curNode = head
    for num in a[1:]:
        nextNode = ListNode(num)
        curNode.next = nextNode
        curNode      = nextNode
        
    print(sln.getDecimalValue(head))           