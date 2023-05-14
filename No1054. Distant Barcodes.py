# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:41:35 2023

@author: Dell

1054. Distant Barcodes
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque,Counter
import heapq
import itertools as it
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
class Solution:
    def rearrangeBarcodes_NG(self, barcodes: List[int]) -> List[int]:
        '''
        贪婪: 每找到一个跟前一个相同的数值，就向后搜索找一个不同的，找到后交换位置。
        in-place operation.
        如何证明贪婪必定可行? -- 不一定可行。比如说[2,1,1]
        '''
        p = 1
        while p < len(barcodes):
            if barcodes[p] == barcodes[p-1]:
                q = p + 1
                while barcodes[p] == barcodes[q]:
                    q = q + 1
                barcodes[p], barcodes[q] = barcodes[q], barcodes[p]
            p = p + 1
        return barcodes

    def rearrangeBarcodes1(self, barcodes: List[int]) -> List[int]:
        data = []
        for i, j in Counter(barcodes).most_common():
            data += [i] * j
        l = len(data)
        ans = [0] * l
        ans[::2] = data[:(l+1)//2]
        ans[1::2] = data[(l+1)//2:]
        return ans

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        q = []
        for x, cx in count.items():
            heapq.heappush(q, (-cx, x))
        res = []
        while len(q) > 0:
            cx, x = heapq.heappop(q)
            if len(res) == 0 or res[-1] != x:
                res.append(x)
                if cx < -1:
                    heapq.heappush(q, (cx + 1, x))
            else:
                cy, y = heapq.heappop(q)
                res.append(y)
                if cy < -1:
                    heapq.heappush(q, (cy + 1, y))
                heapq.heappush(q, (cx, x))
        return res
    
if __name__ == '__main__':

    sln  = Solution()                
    
    barcodes = [1,1,1,2,2,2]
    print(sln.rearrangeBarcodes(barcodes))  
    
    barcodes = [1,1,1,1,2,2,3,3]
    print(sln.rearrangeBarcodes(barcodes)) 
    
    barcodes = [2,1,1]
    print(sln.rearrangeBarcodes(barcodes))     