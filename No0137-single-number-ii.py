# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 07:42:21 2021

@author: chenxy

137. 只出现一次的数字 II
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

示例 1：
输入：nums = [2,2,3,2]
输出：3

示例 2：
输入：nums = [0,1,0,1,0,1,99]
输出：99
 
提示：
1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
 
进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import sys
import time
import random
import collections
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        k = 1
        while k < len(nums)-1:
            if nums[k] == nums[k-1]:
                k += 1
                continue
            elif nums[k] == nums[k+1]:
                k += 2
                continue
            else:
                return nums[k]

    def singleNumber2(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans
        

if __name__ == '__main__':        
            
    sln = Solution()

    nums = [2]    
    print(nums, ' -> ', sln.singleNumber(nums))            
    print(nums, ' -> ', sln.singleNumber2(nums))            

    nums = [2,2,3,2]    
    print(nums, ' -> ', sln.singleNumber(nums))            
    print(nums, ' -> ', sln.singleNumber2(nums))            
                
    nums = [0,1,0,1,0,1,99]
    print(nums, ' -> ', sln.singleNumber(nums))            
    print(nums, ' -> ', sln.singleNumber2(nums))            

    nums = [0,1,99,1,99,1,99]
    print(nums, ' -> ', sln.singleNumber(nums))             
    print(nums, ' -> ', sln.singleNumber2(nums))            