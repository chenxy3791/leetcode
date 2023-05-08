# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:39:22 2023

@author: Dell

15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:
3 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        brute-force, time-out
        '''
        rslt = set()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        rslt.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [list(r) for r in rslt]

if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [-1,0,1,2,-1,-4]
    print(sln.threeSum(nums))
    
    nums = [0,1,1]
    print(sln.threeSum(nums))
    
    nums = [0,0,0]
    print(sln.threeSum(nums))