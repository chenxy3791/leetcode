# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 09:22:38 2023

@author: chenxy

给你一个整数数组 nums ，返回其中 按位与三元组 的数目。

按位与三元组 是由下标 (i, j, k) 组成的三元组，并满足下述全部条件：

0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。
 
示例 1：
输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

示例 2：
输入：nums = [0,0,0]
输出：27

提示：
1 <= nums.length <= 1000
0 <= nums[i] < 216

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    def countTriplets(self, nums: List[int]) -> int:
        counts = defaultdict()
        for k in range(len(nums)):
            for j in range(len(nums)):
                # counts[nums[k] & nums[j]] += 1
                and_rslt = nums[k] & nums[j]
                if and_rslt in counts:
                    counts[and_rslt] = counts[and_rslt] + 1
                else:
                    counts[and_rslt] = 1
        
        print(counts)
        triples_cnt = 0
        for k in counts:
            for j in range(len(nums)):
                triples_cnt += ( k & nums[j] == 0) * counts[k]
                    
        return triples_cnt
            
if __name__ == '__main__':

    sln  = Solution()        

    nums = [2,1,3]
    print(sln.countTriplets(nums))

    nums = [0,0,0]
    print(sln.countTriplets(nums))
    
    nums = [1,1,1]
    print(sln.countTriplets(nums))
           