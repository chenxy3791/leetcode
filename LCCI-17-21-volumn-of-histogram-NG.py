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
以下解答建立一个错误的认识理解上，对于[5,2,1,2,1,5]这样的输入无法得出正确的结果。
总的储水量并不是各个局部洼地的储水量之和。
在[5,2,1,2,1,5]例子，a[3]=2是一个局部高点，但是它的两侧都有更高的高点，所以这个局部高点其实是可以忽略，
因为最终的水位是可以高于它。
只有对水位构成限制的局部高点才是有效的高点

"""

class Solution:
    #def trap(self, height: List[int]) -> int:
    def trap(self, height) -> int:
        def getWater(m,n):
            water= 0
            hMin = min(height[m], height[n])
            for l in range(m+1,n): # No need of counting the start and the end
                water = water + max(0,hMin - height[l])
            # print('getWater(): ', m, n, ' -> ', water)
            return water
            
        rslt  = 0
        start = 0
        state = 0
        for k in range(len(height)-1):            
            if state == 0:
                # Search for the start of the lower-lying land
                if height[k] > height[k+1]:
                    state = 1
                    start = k
                else:
                    state = 0
            elif state == 1:
                # Search for the end of the lower-lying land
                if height[k] < height[k+1]:
                    state = 2
            else:
                if height[k] > height[k+1]:
                    state = 1                    
                    # water = getWater(start,k)                    
                    rslt = rslt + getWater(start,k)                    
                    start = k
        # Handling the final block
        if state == 2:
            rslt = rslt + getWater(start,len(height)-1)                    
            
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