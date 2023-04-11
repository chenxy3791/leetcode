# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:27:20 2022

@author: Dell
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        state, bought, profit  = 0,0,0

        prices.append(0) # Appending one zero for the convenience of last day handling
        for i in range(len(prices)-1):
            if state == 0:
                if prices[i+1]>prices[i]:
                    bought = prices[i]
                    state  = 1
                elif prices[i+1]<prices[i]:
                    state  = -1
            elif state == -1:
                if prices[i+1]>prices[i]:
                    bought = prices[i]
                    state  = 1
            else:
                if prices[i+1]<prices[i]:
                    state  = -1
                    profit += prices[i]-bought
            # print(i,state,bought, profit)

        return profit
    
if __name__ == "__main__":
    
    sln = Solution()  
    
    prices = [7,1,5,3,6,4]
    print(sln.maxProfit(prices))
    
    prices = [7,6,4,3,1]
    print(sln.maxProfit(prices))
    
    prices = [7,6,4,3,6]
    print(sln.maxProfit(prices))    
    
    prices = [1,2,3,4,5]
    print(sln.maxProfit(prices))  