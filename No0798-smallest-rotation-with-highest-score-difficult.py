# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 07:29:13 2022

@author: chenxy

798. 得分最高的最小轮调
给定一个数组 A，我们可以将它按一个非负整数 K 进行轮调，这样可以使数组变为 A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。
例如，如果数组为 [2, 4, 1, 3, 0]，我们按 K = 2 进行轮调后，它将变成 [1, 3, 0, 2, 4]。这将记作 3 分，因为 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point]。
在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。

示例 1：
输入：[2, 3, 1, 4, 0]
输出：3
解释：
下面列出了每个 K 的得分：
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
所以我们应当选择 K = 3，得分最高。

示例 2：
输入：[1, 3, 0, 2, 4]
输出：0
解释：
A 无论怎么变化总是有 3 分。
所以我们将选择最小的 K，即 0。

提示：
A 的长度最大为 20000。
A[i] 的取值范围是 [0, A.length]。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
# import random
from typing import List	
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
# import itertools as it
import numpy as np
class Solution:
    def bestRotation1(self, nums: List[int]) -> int:
        N = len(nums)
        margin = np.zeros((N,)) # idx - value
        r_max = 0
        point_max = -float('inf')
        for r in range(N):
            for i in range(N):
                margin[i] = ((i-r)%N) - nums[i]
            # print(margin >= 0)
            point  = sum((margin >= 0).astype('int'))
            if point_max < point:
                point_max = point
                r_max = r
        return r_max               

    def bestRotation(self, nums: List[int]) -> int:
# =============================================================================
# 执行用时：7656 ms, 在所有 Python3 提交中击败了6.82%的用户
# 内存消耗：42.1 MB, 在所有 Python3 提交中击败了6.82%的用户        
# =============================================================================
        N = len(nums)

        points = np.zeros((N,))

        for i in range(N):
            x = nums[i]
            if i < x:
                points[i+1:i-x+N+1] += 1
            else:
                points[0:i-x+1] += 1
                points[(i+1):] += 1
            # print(i, points)

        k_max = 0
        point_max = points[0]
        
        for k in range(1,N):
            if point_max < points[k]:
                point_max = points[k]
                k_max = k
        return k_max                               
        
if __name__ == '__main__':            
    sln = Solution()
    
    nums = [2, 3, 1, 4, 0]
    print('ans = {0}'.format(sln.bestRotation1(nums)))            
    print('ans = {0}'.format(sln.bestRotation(nums)))            
        
    nums = [1, 3, 0, 2, 4]
    print('ans = {0}'.format(sln.bestRotation1(nums)))            
    print('ans = {0}'.format(sln.bestRotation(nums)))            
    
    N = 2000
    nums = list(np.random.randint(0,N,N))

    tStart = time.time()     
    ans = sln.bestRotation1(nums)
    tElapsed = time.time() - tStart        
    print('ans = {0}, tElapsed = {1} (sec)'.format(ans,tElapsed))            
    
    tStart = time.time()     
    ans = sln.bestRotation(nums)
    tElapsed = time.time() - tStart        
    print('ans = {0}, tElapsed = {1} (sec)'.format(ans,tElapsed))            
        