# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 07:21:42 2021

@author: chenxy

面试题 17.21. 直方图的水量
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

同Leetcode-No42

2021-04-02 
LCCI-17-21-volumn-of-histogram-NG.py的解答建立一个错误的认识理解上，
即：总的储水量等于各个局部洼地的储水量之和。
对于[5,2,1,2,1,5]这样的输入无法得出正确的结果。
在[5,2,1,2,1,5]例子，a[3]=2是一个局部高点，但是它的两侧都有更高的高点，所以这个局部高点其实是可以忽略，
因为最终的水位是可以高于它。
只有对水位构成限制的局部高点才是有效的高点

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