# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:19:25 2023

@author: Chenxy

560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 10**4
-1000 <= nums[i] <= 1000
-10**7 <= k <= 10**7
"""

import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     presum = [0]*(len(nums)+1)
    #     for i in range(1,len(nums)+1):
    #         presum[i] = presum[i-1] + nums[i-1]

    #     # print(presum)
    #     cnt = 0
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)+1):
    #             if presum[j] - presum[i] == k:
    #                 cnt = cnt + 1
    #     return cnt            

    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for start in range(len(nums)):
            partsum = 0
            for end in range(start,len(nums)):
                partsum = partsum + nums[end]
                if partsum == k:
                    cnt = cnt + 1
                    # break
        return cnt
                

if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [1,1,1]
    k    = 2
    print(sln.subarraySum(nums,k))
    
    nums = [1,2,3]
    k    = 3
    print(sln.subarraySum(nums,k))
    
    nums = [1,-1,0]
    k    = 0
    print(sln.subarraySum(nums,k))