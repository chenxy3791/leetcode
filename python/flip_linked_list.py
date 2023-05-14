# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:57:36 2023

@author: Dell

<<一本书读懂ChatGPT>>, P062
用Python 写代码:有一个无环单链表，里面存的都是数值，请将连续3个及以上的偶数进行翻盘，
比如单链表 1-2-4-3-5-7-6-7-8-2-0-3，这里的字表示单链表的值，标点符号-表示下一个元素，
这里仅需要将 8-2-0翻盘为0-2-8，即输出1-2-4-3-5-7-6-7-0-2-8-3。

"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
from bisect import bisect, bisect_left, bisect_right
from functools import reduce

class ListNode:
    def __init__ (self,val=0,next=None):
        self.val = val
        self.next = next
    
def flip_even_nodes (head):
    dummy = ListNode(0,head)
    prev  = dummy
    curr  = head
    count = 0

    while curr:
        if curr.val%2== 0:
            count += 1
        else:
            if count >= 3:
                '''
                找到一个奇数，而此前的连续偶数计数大于等于3，执行反转处理
                '''
                prev.next = flip(prev.next,count)
                # _ = flip(prev.next,count)
                count =0
        curr = curr.next
        prev = prev.next
    
    # Processing the final segments, because the final part maybe continuous evens
    if count >= 3:
        prev.next = flip(prev.next, count)
    return dummy.next
    
def flip(head,count):
    print('head.val = ', head.val)
    curr = head
    prev = None

    for i in range(count):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        head.next = curr
    return prev

# 测试 -- 运行结果不正确, need further debug
head = ListNode(1,
        ListNode(2, 
        ListNode(4,
        ListNode(3,
        ListNode(5,
            ListNode(7,
                ListNode(6,
                    ListNode(7,
                        ListNode(8,
                            ListNode(2,
                                ListNode(0,
                                    ListNode(3))))))))))))

print('before flipping: ', end='')
result = head
while result:
    print(result.val,end="")
    result = result.next
print()

result = flip_even_nodes(head)
print('after flipping: ', end='')
while result:
    print(result.val,end="")
    result = result.next