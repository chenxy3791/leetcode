# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:55:11 2022

@author: Dell
"""
import time
from typing import List
import heapq
class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        def findMax(m):    
            curMax = max(nums[m:m+k])
            return curMax, nums[m:m+k].index(curMax)+m
            
        maxList = []
        # Find the maximum for the first window
        curMax,curMaxIdx = findMax(0)
        maxList.append(curMax)
        for m in range(1,len(nums)-k+1):
            # print(m,curMax,curMaxIdx)
            if nums[m+k-1] > curMax:
                curMax = nums[m+k-1]
                curMaxIdx = m+k-1
            else:
                if curMaxIdx == (m-1):
                    # The largest of the previous window is the first one,
                    # hence, not in the current window
                    # search for the maximum of the current window from the scratch
                    curMax,curMaxIdx = findMax(m)
                else:
                    # The largest of the previous window is not the first one
                    # Noting to do
                    None
            maxList.append(curMax)
        return maxList

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        maxlist = []
        h = []
        # Initialize the heaq with the first window
        for m in range(k):
            heapq.heappush(h,(-nums[m],m))
        maxlist.append(-(h[0][0]))
    
        for m in range(1,len(nums)-k+1):
            # print(m,h)
            heapq.heappush(h,(-nums[m+k-1],m+k-1))
            while True:                
                if h[0][1] < m:
                    heapq.heappop(h)
                else:
                    break
            maxlist.append(-h[0][0])
        return maxlist
    
if __name__ == '__main__':
    
    sln = Solution()
    
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sln.maxSlidingWindow1(nums, k))
    print(sln.maxSlidingWindow2(nums, k))

    nums = [7,2,4]
    k = 2
    print(sln.maxSlidingWindow1(nums, k))
    print(sln.maxSlidingWindow2(nums, k))
    
    nums = [1]
    k = 1
    print(sln.maxSlidingWindow1(nums, k))
    print(sln.maxSlidingWindow2(nums, k))

    nums = [9,10,9,-7,-4,-8,2,-6]  
    k = 5
    print(sln.maxSlidingWindow1(nums, k))
    print(sln.maxSlidingWindow2(nums, k))
    
    m = 10**5
    k = 5000
    nums = [m-k for k in range(m)]
    # tstart=time.time()  
    # print(sln.maxSlidingWindow1(nums, k))
    # tstop=time.time()
    # print('tcost = {0:5.3f}(sec)'.format(tstop-tstart))      
    
    # tstart=time.time()  
    # print(sln.maxSlidingWindow2(nums, k))
    # tstop=time.time()
    # print('tcost = {0:5.3f}(sec)'.format(tstop-tstart))   
    
    m = 10**5
    k = 50000
    nums = [m-k for k in range(m)]
    tstart=time.time()  
    print(sln.maxSlidingWindow2(nums, k))
    tstop=time.time()
    print('tcost = {0:5.3f}(sec)'.format(tstop-tstart))       