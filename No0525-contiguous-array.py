# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:37:21 2023

@author: Dell
525. 连续数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

提示：

1 <= nums.length <= 10**5
nums[i] 不是 0 就是 1
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
    # def findMaxLength(self, nums: List[int]) -> int:
    #     cnt = 0
    #     hmap = defaultdict(list)
    #     hmap[0] = [-1]
    #     pre  = 0
    #     maxlen = 0
    #     for i in range(len(nums)):
    #         pre = pre + (1 if nums[i]==1 else -1)
    #         if pre in hmap:
    #             print(hmap)
    #             maxlen = max(maxlen, i - min(hmap[pre]))
    #         hmap[pre].append(i)            
    #     return maxlen        

    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0
        hmap = defaultdict(int)
        hmap[0] = -1
        pre  = 0
        maxlen = 0
        for i in range(len(nums)):
            pre = pre + (1 if nums[i]==1 else -1)
            if pre in hmap:
                #print(hmap)
                maxlen = max(maxlen, i - hmap[pre])
            else:
                hmap[pre] = i            
        return maxlen    
    
if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [0,1]
    print(sln.findMaxLength(nums))
    
    nums = [0,1,0]
    print(sln.findMaxLength(nums))