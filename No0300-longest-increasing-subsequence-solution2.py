# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 08:39:28 2023

@author: chenxy

300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-10**4 <= nums[i] <= 10**4
 

进阶：你能将算法的时间复杂度降低到 O(n log(n)) 吗?

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
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     S = [[]]
    #     max_len = 0
    #     for k in range(1,len(nums)+1):
    #         maxlen_inner = 0
    #         j_max        = 0
    #         for j in range(k-1,0,-1):
    #             # print(k,j)
    #             if (nums[k-1] > S[j][-1]) and (len(S[j]) > maxlen_inner):
    #                 maxlen_inner = len(S[j])
    #                 j_max = j

    #         S.append(S[j_max]+[nums[k-1]])                    
    #         max_len = max(max_len, maxlen_inner+1)
        
    #     # print(S)
        
    #     return max_len

    def lengthOfLIS(self, nums: List[int]) -> int:
        S = [[0,0]] # [length, the last number]
        max_len = 0
        for k in range(1,len(nums)+1):
            maxlen_inner = 0
            # j_max        = 0
            for j in range(k-1,0,-1):
                # print(k,j)
                if (nums[k-1] > S[j][1]) and (S[j][0] > maxlen_inner):
                    maxlen_inner = S[j][0]
                    # j_max = j

            S.append([maxlen_inner+1,nums[k-1]])
            max_len = max(max_len, maxlen_inner+1)
                
        return max_len
                
if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [10,9,2,5,3,7,101,18]
    print(sln.lengthOfLIS(nums))
    
    nums = [0,1,0,3,2,3]
    print(sln.lengthOfLIS(nums))
    
    nums = [7,7,7,7,7,7,7]
    print(sln.lengthOfLIS(nums))