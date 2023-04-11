# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:07:12 2022

@author: Dell
"""
from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        maxscore = 2*10**4
        for j in range(n+1):
            if j == 0 or j == n:
                score = nums[n-1] - nums[0]
            else:
                score = max(nums[n-1]-k,nums[j-1]+k) - min(nums[0]+k,nums[j]-k)
            maxscore = min(maxscore,score)     
        return maxscore
            
if __name__ == "__main__":
    
    sln = Solution()  
            
    nums = [1]
    k = 0
    print(sln.smallestRangeII(nums, k))
    
    nums = [0,10]
    k = 2
    print(sln.smallestRangeII(nums, k))
    
    nums = [1,3,6]
    k = 3
    print(sln.smallestRangeII(nums, k))