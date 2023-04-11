# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:27:20 2022

@author: Dell
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minprice = prices[0]
        maxprofit= -prices[0]
        for j in range(1,len(prices)):
            profit = prices[j] - minprice
            minprice = min(minprice,prices[j])
            maxprofit= max(maxprofit,profit)
            
        return max(maxprofit,0)
    
if __name__ == "__main__":
    
    sln = Solution()  
    
    prices = [7,1,5,3,6,4]
    print(sln.maxProfit(prices))
    
    prices = [7,6,4,3,1]
    print(sln.maxProfit(prices))
    
        