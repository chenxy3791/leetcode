# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:56:20 2023

@author: chenxy

1043. Partition Array for Maximum Sum
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10**9
1 <= k <= arr.length
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

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        '''
        执行用时：160 ms, 在所有 Python3 提交中击败了98.70%的用户
        内存消耗：15.1 MB, 在所有 Python3 提交中击败了34.41%的用户
        '''
        dp = len(arr)*[0]
        tmp_max = 0
        for i in range(k):
            tmp_max = max(tmp_max, arr[i])
            dp[i]   = (i+1) * tmp_max
            
        for i in range(k,len(arr)):
            tmp_max = 0
            dp_max  = 0
            for l in range(k):
                tmp_max = max(tmp_max,arr[i-l])
                dp_max  = max(dp_max, tmp_max * (l+1) + dp[i-l-1])
                # print(tmp_max,dp[i-l-1],dp_max)
            dp[i] = dp_max
        # print(dp)
        return max(dp)

if __name__ == '__main__':

    sln  = Solution()                
    
    arr = [1,15,7,9,2,5,10]
    k = 3
    print(sln.maxSumAfterPartitioning(arr,k))
    
    arr = [1,4,1,5,7,3,6,1,9,9,3]; k = 4
    print(sln.maxSumAfterPartitioning(arr,k))
    
    arr = [1]; k = 1
    print(sln.maxSumAfterPartitioning(arr,k))