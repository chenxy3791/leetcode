# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:40:55 2023

@author: chenxy
974. 和可被 K 整除的子数组
给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。

子数组 是数组的 连续 部分。


示例 1：

输入：nums = [4,5,0,-2,-3,1], k = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 k = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
示例 2:

输入: nums = [5], k = 9
输出: 0
 

提示:

1 <= nums.length <= 3 * 10**4
-10**4 <= nums[i] <= 10**4
2 <= k <= 10**4

执行用时：92 ms, 在所有 Python3 提交中击败了31.44%的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了12.75%的用户

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
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        hmap = defaultdict(int)
        hmap[0] = 1
        presum  = 0
        for i in range(len(nums)):
            presum = presum + nums[i]
            if presum % k in hmap:
                cnt = cnt + hmap[presum % k]
            hmap[presum % k] = hmap[presum % k] + 1
            
        return cnt        

if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [4,5,0,-2,-3,1]
    k    = 5
    print(sln.subarraysDivByK(nums,k))
    
    nums = [5]
    k    = 9
    print(sln.subarraysDivByK(nums,k))