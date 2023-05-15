# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:44:26 2023

@author: chenxy

2441. Largest Positive Integer That Exists With Its Negative
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
 

Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0

"""
import time
import random
import time
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right

class Solution:
    def findMaxK1(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # print(nums)
        for k,num in enumerate(nums):
            # print(k,num)
            if num < 0:
                return -1
            for j in range(len(nums)-1,k,-1):
                if nums[j] > 0:
                    break
                if nums[j] + num == 0:
                    return num
        return -1

    def findMaxK2(self, nums: List[int]) -> int:
        '''
        Counter return a dict holding the number of occurence of each number
        '''
        cnt = Counter(nums)
        print(cnt)
        ans = -1
        for k in cnt:
            if k > 0 and cnt[-k] > 0:
                ans = max(ans, k)
        return ans

    def findMaxK3(self, nums: List[int]) -> int:
        '''
        sorting, then dual pointer method
        '''
        nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            if nums[j]<0 or nums[i]>0:
                return -1
            if nums[i]+nums[j]==0:
                return nums[j]
            elif nums[i]+nums[j]<0:
                i+=1
            else:
                j-=1
        return -1

    def findMaxK(self, nums: List[int]) -> int:
        '''
        Similar to findMaxK2
        '''
        k = -1
        s = set(nums)
        for x in nums:
            if -x in s:
                k = max(k, x)
        return k    
                
if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [-1,2,-3,3]
    print(sln.findMaxK(nums))   
    
    nums = [-1,10,6,7,-7,1]
    print(sln.findMaxK(nums))   
    
    nums = [-10,8,6,7,-2,-3]
    print(sln.findMaxK(nums))   
    
    nums = [648,674,610]
    print(sln.findMaxK(nums))       