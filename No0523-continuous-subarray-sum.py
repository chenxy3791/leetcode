# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:00:32 2023

@author: chenxy
523. 连续的子数组和
给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。

示例 1：

输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
示例 2：

输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
示例 3：

输入：nums = [23,2,6,4,7], k = 13
输出：false

提示：

1 <= nums.length <= 10**5
0 <= nums[i] <= 10**9
0 <= sum(nums[i]) <= 2**31 - 1
1 <= k <= 2**31 - 1

2023-03-11
执行用时：136 ms, 在所有 Python3 提交中击败了29.55%的用户
内存消耗：43.6 MB, 在所有 Python3 提交中击败了5.20%的用户
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
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # cnt = 0
        hmap = defaultdict(list)
        hmap[0] = [-1]
        presum  = 0
        for i in range(len(nums)):
            presum = presum + nums[i]
            if presum % k in hmap:
                print(hmap)
                # cnt = cnt + sum([(i-j)>=2 for j in hmap[presum % k]])
                for j in hmap[presum % k]:
                    if (i-j)>=2:
                        return True    
            # hmap[presum % k] = hmap[presum % k].append(i) # Incorrect!
            hmap[presum % k].append(i)            
            
        # return cnt          
        return False

if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [23,2,4,6,7]
    k    = 6
    print(sln.checkSubarraySum(nums,k))
    
    nums = [23,2,6,4,7]
    k    = 6
    print(sln.checkSubarraySum(nums,k))
    
    nums = [23,2,6,4,7]
    k    = 13
    print(sln.checkSubarraySum(nums,k))    
    
    nums = [5,0,0,0]
    k    = 3
    print(sln.checkSubarraySum(nums,k))    