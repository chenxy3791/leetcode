# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:53:53 2021

@author: chenxy
220. 存在重复元素 III
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。

 

示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
 

提示：

0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1
"""
import time
import random
import sys
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
# =============================================================================
#         2021-04-17
#         Too slow!
# =============================================================================
        N = len(nums)
        if N < 2: 
            return False
                        
        for i in range(N-1):
            for j in range(i+1,min(i+k+1,N)):
                # print(i,j,nums[i],nums[j])                
                if abs(nums[i]-nums[j]) <= t:                    
                    return True
        return False

if __name__ == '__main__':        
    
    sln = Solution()        
    
    nums = [1,2,3,1]
    k = 3
    t = 0
    print(sln.containsNearbyAlmostDuplicate(nums,k,t))    
    
    nums = [1,0,1,1]
    k = 1
    t = 2
    print(sln.containsNearbyAlmostDuplicate(nums,k,t))        
    
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    print(sln.containsNearbyAlmostDuplicate(nums,k,t))         
    
    nums = [2147483646,2147483647]
    k = 3
    t = 3    
    print(sln.containsNearbyAlmostDuplicate(nums,k,t))             
    
    nums = [7,1,3]
    k = 2
    t = 3    
    print(sln.containsNearbyAlmostDuplicate(nums,k,t))             
    
    N = 10000
    nums = [random.randint(0, N) for _ in range(N)]
    k = N//2
    t = -1
    t1 = time.time()
    print(sln.containsNearbyAlmostDuplicate(nums,k,t))             
    t2 = time.time()
    print(t2-t1)