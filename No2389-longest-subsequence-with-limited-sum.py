# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 07:59:02 2023

@author: chenxy
2389. 和有限的最长子序列
给你一个长度为 n 的整数数组 nums ，和一个长度为 m 的整数数组 queries 。

返回一个长度为 m 的数组 answer ，其中 answer[i] 是 nums 中 元素之和小于等于 queries[i] 的 子序列 的 最大 长度  。

子序列 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。

示例 1：

输入：nums = [4,5,2,1], queries = [3,10,21]
输出：[2,3,4]
解释：queries 对应的 answer 如下：
- 子序列 [2,1] 的和小于或等于 3 。可以证明满足题目要求的子序列的最大长度是 2 ，所以 answer[0] = 2 。
- 子序列 [4,5,1] 的和小于或等于 10 。可以证明满足题目要求的子序列的最大长度是 3 ，所以 answer[1] = 3 。
- 子序列 [4,5,2,1] 的和小于或等于 21 。可以证明满足题目要求的子序列的最大长度是 4 ，所以 answer[2] = 4 。
示例 2：

输入：nums = [2,3,4,5], queries = [1]
输出：[0]
解释：空子序列是唯一一个满足元素和小于或等于 1 的子序列，所以 answer[0] = 0 。
 

提示：

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 10**6

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/longest-subsequence-with-limited-sum/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
import bisect

class Solution:
    # def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    #     nums.sort()
    #     presum = len(nums) * [0]
    #     presum[0] = nums[0]
    #     for k in range(1,len(nums)):
    #         presum[k] = presum[k-1] + nums[k]
        
    #     ret = []
    #     for q in queries:
    #         ret.append(bisect.bisect_right(presum, q))
        
    #     return ret

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = list(it.accumulate(sorted(nums)))
        return [bisect.bisect_right(f, q) for q in queries]        
            
if __name__ == '__main__':

    sln  = Solution()                
    
    nums = [4,5,2,1]
    queries = [3,10,21]
    print(sln.answerQueries(nums,queries))        
    
    nums = [2,3,4,5]
    queries = [1]
    print(sln.answerQueries(nums,queries))        