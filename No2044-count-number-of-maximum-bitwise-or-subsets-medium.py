# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 08:10:28 2022

@author: chenxy

2044. 统计按位或能得到最大值的子集数目
给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。
对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。

示例 1：
输入：nums = [3,1]
输出：2
解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ：
- [3]
- [3,1]

示例 2：
输入：nums = [2,2,2]
输出：7
解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 2^3 - 1 = 7 个子集。

示例 3：
输入：nums = [3,2,1,5]
输出：6
解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ：
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
 
提示：
1 <= nums.length <= 16
1 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List	
# import random
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
from functools import reduce
import itertools as it
from itertools import chain, combinations
# import numpy as np
# class Solution:
#     def powerset(self,iterable):
#         "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#         s = list(iterable)
#         return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#     def countMaxOrSubsets(self, nums: List[int]) -> int:        
#         # Hash table construction
#         d = dict()
#         for k, num in enumerate(nums):
#             print(k,num)
#             bitpos = 0
#             while num > 0:
#                 if num & 1 == 1:
#                     if bitpos not in d:
#                         d[bitpos] = set([k])
#                     else:
#                         d[bitpos].add(k)
#                 num = num // 2
#                 bitpos += 1
#         print(d)                            
        
#         # Find the valid subset
#         setOfsubset = set()
#         for key in d:            
#             curPowSet = set(self.powerset(d[key]))
#             print(key, d[key],curPowSet)
#             if len(setOfsubset) == 0:
#                 setOfsubset = curPowSet
#             else:
#                 setOfsubset = it.product(setOfsubset,curPowSet)
            
#         print(list(setOfsubset))        

# class Solution:
#     def countMaxOrSubsets(self, nums: List[int]) -> int:
#         def powerset(iterable):
#             "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#             s = list(iterable)
#             return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))        

#         maxbitor = -1
#         maxcnt   = 0
#         for s in powerset([k for k in range(len(nums))]):
#             bitor = 0
#             for k in range(len(s)):
#                 bitor = bitor | nums[s[k]]
#             print(s, bitor)
#             if maxbitor < bitor:
#                 maxbitor = bitor
#                 maxcnt   = 1
#             elif maxbitor == bitor:
#                 maxcnt   = maxcnt + 1
#         return maxcnt                
                

# class Solution:
#     # Official Solution, but run with error. What the fuck is 'or_'?
#     def countMaxOrSubsets(self, nums: List[int]) -> int:
#         maxOr, cnt = 0, 0
#         for i in range(1, 1 << len(nums)):
#             orVal = reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
#             if orVal > maxOr:
#                 maxOr, cnt = orVal, 1
#             elif orVal == maxOr:
#                 cnt += 1
#         return cnt

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:     
        maxVal, maxCnt = 0, 0
        def dfs(idx, bitorval):
            if idx == len(nums):
                nonlocal maxVal, maxCnt
                if bitorval > maxVal:
                    maxVal = bitorval
                    maxCnt = 1 # New max found, so the counter should be reset to 1
                elif bitorval == maxVal:
                    maxCnt += 1
                return
            dfs(idx + 1, bitorval | nums[idx])
            dfs(idx + 1, bitorval)
        dfs(0, 0)
        return maxCnt
            
if __name__ == '__main__':            
    
    sln = Solution()

    # print(list(sln.powerset([1,2,3])))

    nums = [3,1]
    tStart = time.time()        
    ans = sln.countMaxOrSubsets(nums)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))                  
    
    nums = [2,2,2]
    tStart = time.time()        
    ans = sln.countMaxOrSubsets(nums)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))                      
    
    nums = [3,2,1,5]
    tStart = time.time()        
    ans = sln.countMaxOrSubsets(nums)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))                          