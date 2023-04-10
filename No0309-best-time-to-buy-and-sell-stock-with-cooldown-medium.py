# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:14:08 2022

@author: Dell
"""
from typing import List
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n    = len(prices)
        memo = dict()
        def dp(k):
            # print(k,memo)
            if k in memo:
                return memo[k]
            if k >= n-1:
                return 0
            maxprofit = dp(k+1) # not buy at day#k
            
            # Assuming buy at day#k
            for j in range(k+1,len(prices)):
                if prices[j]>prices[k]:
                    profit    = prices[j] - prices[k] + dp(j+2)
                    maxprofit = max(maxprofit, profit)
            memo[k] = maxprofit
            return maxprofit
    
        return dp(0)
    
if __name__ == "__main__":
    
    sln = Solution()  
    
    prices = [1,2,3,0,2]
    print(sln.maxProfit(prices))
                        
    prices = [1]
    print(sln.maxProfit(prices))
            