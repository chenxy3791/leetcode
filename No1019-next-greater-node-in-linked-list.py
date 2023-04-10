# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:29:55 2023

@author: chenxy

1019. Next Greater Node In Linked List
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Example 1:
Input: head = [2,1,5]
Output: [5,5,0]

Example 2:
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
 
Constraints:

The number of nodes in the list is n.
1 <= n <= 10**4
1 <= Node.val <= 10**9

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/next-greater-node-in-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it
import bisect

def lst2sll(data):
    head = ListNode(data[0])
    cur  = head
    for k in range(1,len(data)):
        lnode = ListNode(data[k])
        cur.next = lnode
        cur      = lnode            
    return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        '''
        执行用时：200 ms, 在所有 Python3 提交中击败了54.05%的用户
        内存消耗：20.6 MB, 在所有 Python3 提交中击败了5.40%的用户
        '''
        rslt = [0]
        s = deque()
        s.append((0,head.val))
        
        curnode = head
        while curnode.next != None:
            rslt.append(0) # Initialization for each new node
            curnode = curnode.next
            # print(s[-1])
            while len(s) > 0 and curnode.val > s[-1][1]:
                t = s.pop()
                rslt[t[0]] = curnode.val
            s.append((len(rslt)-1,curnode.val))
        return rslt        
        
if __name__ == '__main__':

    sln  = Solution()                
    
    head = lst2sll([2,1,5])
    print(sln.nextLargerNodes(head))
    
    head = lst2sll([2,7,4,3,5])
    print(sln.nextLargerNodes(head))
    
    head = lst2sll([0,1,5,2,4,6])
    print(sln.nextLargerNodes(head))