# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 07:21:42 2021

@author: chenxy

42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

"""

class Solution:
    #def trap(self, height: List[int]) -> int:
# =============================================================================
#         2021-04-02
#         执行用时：44 ms, 在所有 Python3 提交中击败了79.95%的用户
#         内存消耗：15.2 MB, 在所有 Python3 提交中击败了18.73%的用户        
# =============================================================================
    def trap(self, height) -> int:
        def getWater(m,n):
            water= 0
            hMin = min(height[m], height[n])
            for l in range(m+1,n): # No need of counting the start and the end
                water = water + max(0,hMin - height[l])
            # print('getWater(): ', m, n, ' -> ', water)
            return water

        if len(height) <= 2:
            return 0

        # Traverse height to find all the local maxima
        localMax = []
        for k in range(len(height)):
            if k==0:
                if height[k] > height[k+1]:
                    localMax.append(k)
            elif k==(len(height)-1):
                if height[k] >= height[k-1]:
                    localMax.append(k)
            else:
                if height[k] >= height[k-1] and height[k] > height[k+1]:
                    localMax.append(k)            
            
        # Remove the invalid local maximas
        # left--> right traverse
        maxH = height[localMax[0]]
        leftFlag = len(localMax) * [0]
        for k in range(1,len(localMax)):
            if height[localMax[k]] <= maxH:
                leftFlag[k] = 1
            else:
                maxH = height[localMax[k]]

        maxH = height[localMax[-1]]
        rightFlag = len(localMax) * [0]
        for k in range(len(localMax)-2,0,-1):
            if height[localMax[k]] <= maxH:
                rightFlag[k] = 1
            else:
                maxH = height[localMax[k]]
        # Remove localMax's with both leftFlag and rightFlag asserted
        localMax1 = []
        for k in range(len(localMax)):
            if leftFlag[k]==0 or rightFlag[k]==0:
                localMax1.append(localMax[k])                
                                
        # Calculate the volumn
        rslt = 0
        for k in range(len(localMax1)-1):
            rslt = rslt + getWater(localMax1[k], localMax1[k+1])
                        
        return rslt
                                            
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]    
    print(height, ' -> ', sln.trap(height))
    
    height = [2,0,2]
    print(height, ' -> ', sln.trap(height))
    
    height = [5,2,1,2,1,5]
    print(height, ' -> ', sln.trap(height))
    
    height = []
    print(height, ' -> ', sln.trap(height))
    
    height = [5,3,7,7]
    print(height, ' -> ', sln.trap(height))
    
    height = [4,2,0,3,2,5]
    print(height, ' -> ', sln.trap(height))