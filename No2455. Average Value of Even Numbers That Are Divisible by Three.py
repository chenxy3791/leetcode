# -*- coding: utf-8 -*-
"""
Created on Mon May 29 08:29:23 2023

@author: chenxy

2455. Average Value of Even Numbers That Are Divisible by Three
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

 

Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
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
import bisect
import sys
from utils.BinaryTree import TreeNode, binTree2Lst, lst2bintree
from functools import reduce

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        cnt = 0
        for num in nums:
            if num % 6 == 0:
                total += num
                cnt   += 1
        
        return 0 if cnt == 0 else total // cnt

    def averageValue2(self, nums: List[int]) -> int:
        new_list = [num for num in nums if num % 6 == 0]
        return 0 if len(new_list) == 0 else int(sum(new_list)/len(new_list))
        
if __name__ == '__main__':

    sln  = Solution()            
    
    nums = [1,3,6,10,12,15]
    print(sln.averageValue(nums))           
    
    nums = [1,2,4,7,10]
    print(sln.averageValue(nums))           