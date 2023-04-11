# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 18:09:35 2022

@author: Dell
"""
from typing import List
# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         # Find the maximum subarray sum
#         maxsum = nums[0]
#         prev   = nums[0]
        
#         for i in range(1,len(nums)):
#             cur = max(prev+nums[i], nums[i])
#             maxsum = max(cur,maxsum)
#             prev   = cur
            
#         # Find the minimum subarray sum
#         minsum = nums[0]
#         prev   = nums[0]
        
#         for i in range(1,len(nums)):
#             cur = min(prev+nums[i], nums[i])
#             minsum = min(cur,minsum)
#             prev   = cur
        
#         print(maxsum, minsum)
#         if minsum == sum(nums):
#             return maxsum
#         else:
#             return max(maxsum, sum(nums)-minsum)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Find the maximum subarray sum
        maxsum = nums[0]
        prevMax   = nums[0]
        minsum = nums[0]
        prevMin   = nums[0]
        
        for i in range(1,len(nums)):
            curMax = max(prevMax+nums[i], nums[i])
            maxsum = max(curMax,maxsum)
            prevMax   = curMax
            curMin = min(prevMin+nums[i], nums[i])
            minsum = min(curMin,minsum)
            prevMin   = curMin
        
        maxsum2 = sum(nums)-minsum
        if maxsum2 == 0:
            return maxsum
        else:
            return max(maxsum, maxsum2)

if __name__ == "__main__":
    
    sln = Solution()    
    
    nums = [1,-2,3,-2]
    print(sln.maxSubarraySumCircular(nums))
    
    nums = [5,-3,5]
    print(sln.maxSubarraySumCircular(nums))
    
    nums = [3,-2,2,-3]
    print(sln.maxSubarraySumCircular(nums))
    
    nums = [1,-2,1-2]
    print(sln.maxSubarraySumCircular(nums))
    
    nums = [-3,-2,-3]
    print(sln.maxSubarraySumCircular(nums))