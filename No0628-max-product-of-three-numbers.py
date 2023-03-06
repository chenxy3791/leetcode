# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:08:23 2021

@author: chenxy

628. 三个数的最大乘积
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1：

输入：nums = [1,2,3]
输出：6
示例 2：

输入：nums = [1,2,3,4]
输出：24
示例 3：

输入：nums = [-1,-2,-3]
输出：-6
 

提示：

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000

"""

class Solution:
    #def maximumProduct(self, nums: List[int]) -> int:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        
        n = len(nums)
        
        numOfPositive = 0
        for k in range(len(nums)):
            if nums[k] > 0:
                numOfPositive = numOfPositive +1
        
        if numOfPositive >= 3:
            return max(nums[n-1]*nums[n-2]*nums[n-3], nums[0]*nums[1]*nums[n-1])
        elif numOfPositive == 2 or numOfPositive == 1:
            return nums[0]*nums[1]*nums[n-1]
        else:
            return nums[n-1]*nums[n-2]*nums[n-3]
                
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()
    
    nums = [1,2,3]    
    print(sln.maximumProduct(nums))        
    
    nums = [-1,-2,-3,-4]    
    print(sln.maximumProduct(nums))            
    
    nums = [-1,-2,-3,-4, 5, 6]    
    print(sln.maximumProduct(nums))                
    
    nums = [-2,-3,-4, -5, 5]    
    print(sln.maximumProduct(nums))                    
    
    nums = [-3,-2,-1,0,0,0,0]
    print(sln.maximumProduct(nums))                    