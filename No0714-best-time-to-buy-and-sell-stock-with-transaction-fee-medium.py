# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:14:08 2022

@author: Dell
"""
from typing import List
import time
class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:
        
    #     n    = len(prices)
    #     memo = dict()
    #     def dp(k):
    #         # print(k,memo)
    #         if k in memo:
    #             return memo[k]
    #         if k >= n-1:
    #             return 0
            
    #         maxprofit = dp(k+1) # not buy at day#k
            
    #         # Assuming buy at day#k
    #         for j in range(k+1,len(prices)):
    #             if prices[j]>prices[k]+fee:
    #                 profit    = prices[j] - (prices[k]+fee) + dp(j+1)
    #                 maxprofit = max(maxprofit, profit)
    #         memo[k] = maxprofit
    #         return maxprofit
    
    #     return dp(0)

    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp   = [[0,0] for k in range(len(prices))]
        dp[0][1] = -prices[0]
        for k in range(1,len(prices)):
            dp[k][0] = max(dp[k-1][0],dp[k-1][1]+prices[k]-fee)
            dp[k][1] = max(dp[k-1][1],dp[k-1][0]-prices[k])
    
        return dp[len(prices)-1][0]
    
if __name__ == "__main__":
    
    sln = Solution()  
    
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(sln.maxProfit(prices,fee))
                        
    prices = [1,3,7,5,10,3]
    fee = 3
    print(sln.maxProfit(prices,fee))
            
    with open('No0714-testcase.py','r') as f:
        exec(f.read())  
        tstart=time.time()    
        print(sln.maxProfit(prices,fee))
        tstop=time.time()
        print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))   