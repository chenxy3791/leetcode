# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 08:15:02 2022

@author: Dell
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        prev   = nums[0]
        
        for i in range(1,len(nums)):
            cur = max(prev+nums[i], nums[i])
            maxsum = max(cur,maxsum)
            prev   = cur
        return maxsum
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if len(nums)==1:
    #         return nums[0]
    #     if max(nums)<=0:
    #         return max(nums)
    #     # nums.insert(0, -1)
    #     # nums.append(-1)
            
    #     left_sum = nums[0]
    #     max_leftsum = nums[0]
    #     right_boundary = 0
    #     for k in range(1,len(nums)):
    #         num = nums[k]
    #         if num <= 0:
    #             if max_leftsum < left_sum:
    #                 max_leftsum = left_sum
    #                 right_boundary = k
    #         left_sum += num
    #     if nums[-1]>0:
    #         if max_leftsum < left_sum:
    #             max_leftsum = left_sum
    #             right_boundary = len(nums)            
    #     print(right_boundary)
        
    #     right_sum = nums[-1]
    #     max_rightsum = nums[-1]
    #     left_boundary = len(nums)-1
    #     for k in range(len(nums)-2,-1,-1):
    #         num = nums[k]
    #         if num <= 0:
    #             if max_rightsum < right_sum:
    #                 max_rightsum = right_sum
    #                 left_boundary = k
    #         right_sum += num
    #     if nums[0]>0:
    #         if max_rightsum < right_sum:
    #             max_rightsum = right_sum
    #             left_boundary = -1
    #     print(left_boundary)
        
    #     return sum(nums[left_boundary+1:right_boundary])
    
if __name__ == "__main__":
    
    sln = Solution()    
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sln.maxSubArray(nums))
    
    nums = [1]
    print(sln.maxSubArray(nums))
    
    nums = [5,4,-1,7,8]
    print(sln.maxSubArray(nums))
    
    nums = [-1]
    print(sln.maxSubArray(nums))
    
    nums = [-1,-2]
    print(sln.maxSubArray(nums))
    
    nums = [-1,-2,0]
    print(sln.maxSubArray(nums))
    
    nums = [-2,1]
    print(sln.maxSubArray(nums))
    
    nums = [1,-2]
    print(sln.maxSubArray(nums))