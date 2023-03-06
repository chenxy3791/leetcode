# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:48:30 2021

@author: chenxy

57. 插入区间
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]
示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]
 
提示：

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals 根据 intervals[i][0] 按 升序 排列
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
"""

class Solution:
    def isOverlap(self, intv1, intv2):
        if intv1[1] < intv2[0] or intv1[0] > intv2[1]:
            return False
        else:
            return True
        
    def joinTwoIntv(self, intv1, intv2):
        newIntv = []
        newIntv.append(min(intv1[0], intv2[0]))
        newIntv.append(max(intv1[1], intv2[1]))
        return newIntv
        
    #def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    def insert(self, intervals, newInterval):        
        # print(intervals)
        overlapFound = False
        newIntv = newInterval
        for k in range(len(intervals)):
            if self.isOverlap(intervals[k], newIntv):
                newIntv = self.joinTwoIntv(intervals[k], newIntv)
                if overlapFound == False:
                    overlapFound = True
                    i = k # Record the first overlapped interval
            else:                
                if overlapFound == True:
                    # remove s[i:k]
                    # insert newIntv
                    # print(i,k)
                    for _ in range(i,k):
                        del intervals[i]
                    intervals.insert(i,newIntv)
                    return intervals
                else:
                    # if overlapFound == True:
                    #     for _ in range(i,len(intervals)):
                    #         del intervals[i]
                    #     intervals.insert(i,newIntv)
                    #     return intervals
                    # else:    
                    if newIntv[0] < intervals[k][0]:
                        # No need to continue, insert the newIntv here
                        intervals.insert(k,newIntv)
                        return intervals
                        
        # Coming here means one of the two possibilities
        # 1. no overlap found, and newIntv should be inserted into the end of intervals
        # 2. the last one or more intervals overlaps with newIntv
        if overlapFound == False:
            intervals.append(newIntv)
        else:
            for _ in range(i,len(intervals)):
                del intervals[i]
            intervals.append(newIntv)
        return intervals                    
    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()
    
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(sln.insert(intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(sln.insert(intervals, newInterval))    
                    
    intervals = []
    newInterval = [5,7]
    print(sln.insert(intervals, newInterval))    
                
    intervals = [[1,5]]
    newInterval = [2,3]
    print(sln.insert(intervals, newInterval))    
            
    intervals = [[1,5]]
    newInterval = [2,7]
    print(sln.insert(intervals, newInterval))    
    
    intervals = [[1,5]]
    newInterval = [0,0]
    print(sln.insert(intervals, newInterval))        

    intervals = [[3,5],[12,15]]
    newInterval = [6,6]
    print(sln.insert(intervals, newInterval))        
