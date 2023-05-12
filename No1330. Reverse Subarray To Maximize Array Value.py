# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:45:52 2023

@author: chenxy

1330. Reverse Subarray To Maximize Array Value
You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.
 
Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.

Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 
Constraints:

1 <= nums.length <= 3 * 10**4
-10**5 <= nums[i] <= 10**5
"""

import os
import time
import random
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right
from   functools import reduce

class Solution:
    def maxValueAfterReverse_bruteforce(self, nums: List[int]) -> int:
        orig_sum = 0
        for k in range(len(nums)-1):
            orig_sum += abs(nums[k+1]-nums[k])

        max_delta = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                delta = 0
                if i > 0:
                    delta = delta + abs(nums[j]-nums[i-1]) - abs(nums[i]-nums[i-1])
                if j < len(nums) - 1:
                    delta = delta + abs(nums[j+1]-nums[i]) - abs(nums[j+1]-nums[j])
                max_delta = max(max_delta,delta)
        return max_delta + orig_sum

    def maxValueAfterReverse(self, nums: List[int]) -> int:
        '''
        Official reference solution.
        Refer to https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/solution/fan-zhuan-zi-shu-zu-de-dao-zui-da-de-shu-t9jv/ 
        for detail explanation
        '''
        value, n = 0, len(nums)
        for i in range(n - 1):
            value += abs(nums[i] - nums[i + 1])
        mx1 = 0
        for i in range(1, n - 1):
            mx1 = max(mx1, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]))
            mx1 = max(mx1, abs(nums[-1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))
        mx2, mn2 = -inf, inf
        for i in range(n - 1):
            x, y = nums[i], nums[i + 1]
            mx2 = max(mx2, min(x, y))
            mn2 = min(mn2, max(x, y))
        return value + max(mx1, 2 * (mx2 - mn2))

    
if __name__ == '__main__':
        
    sln  = Solution()                

    nums = [2,3,1,5,4]
    print(sln.maxValueAfterReverse(nums))        

    nums = [2,4,9,24,2,1,10]
    print(sln.maxValueAfterReverse(nums))       
    
    with open('No1330-testdata.py','r') as f:
        exec(f.read())    
    tstart=time.time()    
    print(sln.maxValueAfterReverse(nums))       
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))    