# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 06:39:11 2022

@author: Dell
"""

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        
        # Calculate F(0) and sum of nums
        nums_sum = 0
        F  = 0
        N  = len(nums)
        for k in range(N):
            nums_sum += nums[k]
            F  += k*nums[k]
            
        maxvalue = F
        for k in range(1,N):
            print(k,F)
            F = nums_sum + F - N * nums[(N-k)%N]
            maxvalue = F if F> maxvalue else maxvalue
        
        return maxvalue
    
if __name__ == "__main__":
    
    sln = Solution()    
    nums = [4,3,2,6]
    print(sln.maxRotateFunction(nums))
        
            
        