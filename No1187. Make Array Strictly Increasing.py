# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 07:49:33 2023

@author: chenxy

1187. Make Array Strictly Increasing
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.


Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
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
from bisect import bisect, bisect_left, bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 预处理：排序，去重，加哨兵
        maxv = 1000000000
        arr1 = [-1] + arr1 + [maxv + 5]
        arr2 = sorted(list(set(arr2)))
        n = len(arr1)

        dp = [0] + [maxv]*(n-1)
        for i in range(1,n):
            j = bisect_left(arr2, arr1[i])
            for k in range(1, min(i-1, j) + 1):  # 1. 枚举替换的个数 k = 1 to min(i-1,j)
                if arr1[i-k-1] < arr2[j-k]:
                    dp[i] = min(dp[i], dp[i-k-1] + k)
            if arr1[i-1] < arr1[i]:          # 2. 不替换 arr1[i-1]
                dp[i] = min(dp[i], dp[i-1])

        return dp[-1] if dp[-1] < maxv else -1

    
    # def makeArrayIncreasing1(self, arr1: List[int], arr2: List[int]) -> int:
    #     arr2.sort()

    #     @cache
    #     def dfs(i: int, pre: int) -> int:
    #         if i == len(arr1): return 0
    #         res = inf
    #         # 换
    #         pos = bisect_right(arr2, pre)
    #         if pos < len(arr2):
    #             res = dfs(i + 1, arr2[pos]) + 1

    #         # 不换
    #         if arr1[i] > pre:
    #             res = min(res, dfs(i + 1, arr1[i]))
    #         return res
        
    #     ans = dfs(0, -1)
    #     return ans if ans != inf else -1

    # def makeArrayIncreasing2(self, arr1: List[int], arr2: List[int]) -> int:
    #     store = sorted(set(arr2))

    #     @lru_cache(None)
    #     def dfs(i: int, pre: int) -> int:
    #         if i >= len(arr1):
    #             return 0

    #         j = bisect_right(store, pre)
    #         swap = 1 + dfs(i + 1, store[j]) if j < len(store) else INF
    #         noswap = dfs(i + 1, arr1[i]) if arr1[i] > pre else INF
    #         return min(swap, noswap)

    #     res = dfs(0, -INF)
    #     return res if res != INF else -1

if __name__ == '__main__':

    sln  = Solution()                
    
    arr1 = [1,5,3,6,7]; arr2 = [1,3,2,4]
    print(sln.makeArrayIncreasing(arr1,arr2))        
    
    arr1 = [1,5,3,6,7]; arr2 = [4,3,1]
    print(sln.makeArrayIncreasing(arr1,arr2))        
    
    arr1 = [1,5,3,6,7]; arr2 = [1,6,3,3]
    print(sln.makeArrayIncreasing(arr1,arr2))        