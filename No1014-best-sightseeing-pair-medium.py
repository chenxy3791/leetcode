# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:29:10 2022

@author: Dell
"""
from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # Initialization for (0,1)
        max_vi_plus_i = values[0] + 0
        # vj_minus_j    = nums[1] - 1
        max_score     = max_vi_plus_i + values[1] - 1
        
        for j in range(2,len(values)):
            max_vi_plus_i = max(max_vi_plus_i,values[j-1]+j-1)
            max_score = max(max_score,max_vi_plus_i + values[j] - j)

        return max_score
            
if __name__ == "__main__":
    
    sln = Solution()  
            
    values = [8,1,5,2,6]
    print(sln.maxScoreSightseeingPair(values))
    
    values = [1,2]
    print(sln.maxScoreSightseeingPair(values))