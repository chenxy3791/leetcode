# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:15:46 2023

@author: chenxy

1027. Longest Arithmetic Subsequence
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].
 

Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500
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
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        执行用时：3444 ms, 在所有 Python3 提交中击败了18.69%的用户
        内存消耗：40.5 MB, 在所有 Python3 提交中击败了34.11%的用户
        '''
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = max(2, dp[j][diff] + 1)
                res = max(res, dp[i][diff])
        return res        
    
if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [3,6,9,12]
    print(sln.longestArithSeqLength(nums))           
    
    nums = [9,4,7,2,10]
    print(sln.longestArithSeqLength(nums))           
    
    nums = [20,1,15,3,10,5,8]
    print(sln.longestArithSeqLength(nums))  
