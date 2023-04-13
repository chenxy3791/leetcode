# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 08:15:28 2023

@author: chenxy
2404. Most Frequent Even Element
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:
Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.

Example 2:
Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.

Example 3:
Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 10**5
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
    def mostFrequentEven(self, nums: List[int]) -> int:
        h = defaultdict(int)        
        for n in nums:
            if n % 2 == 0:
                h[n] = h[n] + 1
        max_num = -1
        max_count = 0
        for num in h:
            if (h[num] > max_count) or (h[num] == max_count and num < max_num):
                max_count = h[num]
                max_num   = num
        return max_num
                    
if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [0,1,2,2,4,4,1]
    print(sln.mostFrequentEven(nums))           
    
    nums = [4,4,4,9,2,4]
    print(sln.mostFrequentEven(nums))           

    nums = [29,47,21,41,13,37,25,7]
    print(sln.mostFrequentEven(nums))               
    
    nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
    print(sln.mostFrequentEven(nums))               