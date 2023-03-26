# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 08:12:32 2023

@author: chenxy
436. 寻找右区间
给你一个区间数组 intervals ，其中 intervals[i] = [starti, endi] ，且每个 starti 都 不同 。

区间 i 的 右侧区间 可以记作区间 j ，并满足 startj >= endi ，且 startj 最小化 。

返回一个由每个区间 i 的 右侧区间 在 intervals 中对应下标组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则下标 i 处的值设为 -1 。

 
示例 1：

输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。
示例 2：

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
 
提示：

1 <= intervals.length <= 2 * 10**4
intervals[i].length == 2
-10**6 <= starti <= endi <= 10**6
每个间隔的起点都 不相同
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
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        '''
        执行用时：60 ms, 在所有 Python3 提交中击败了99.27%的用户
        内存消耗：19.4 MB, 在所有 Python3 提交中击败了28.21%的用户
        '''
        starts = []
        start2idx = defaultdict(int)
        for k,itvl in enumerate(intervals):
            print(itvl, k)
            starts.append(itvl[0])
            start2idx[itvl[0]] = k
        starts.sort()
        print(starts, start2idx)
        
        rslt = []
        for itvl in intervals:
            pos = bisect.bisect_left(starts,itvl[1])
            print(starts,itvl[1],pos)
            if pos >= len(intervals): 
                pos = -1
            else:
                pos = start2idx[starts[pos]]
            rslt.append(pos)
        
        return rslt
        
if __name__ == '__main__':

    sln  = Solution()                
    
    intervals = [[1,2]]
    print(sln.findRightInterval(intervals))            
    
    intervals = [[3,4],[2,3],[1,2]]
    print(sln.findRightInterval(intervals))            
    
    intervals = [[1,4],[2,3],[3,4]]
    print(sln.findRightInterval(intervals))            