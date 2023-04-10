# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:11:55 2022

@author: Dell
"""
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        dp = (amount+1) * [0]
        dp[0] = 1
        
        for k in range(1, amount+1):
            for coin in coins:
                if coin > k:
                    break
                else:
                    dp[k] += dp[k-coin]
        
        print(dp)
        return dp[-1]
    
if __name__ == "__main__":
    
    sln = Solution()    
    
    amount = 5
    coins = [1, 2, 5]
    print(sln.change(amount, coins))
    
    amount = 3
    coins = [2]
    print(sln.change(amount, coins))
    
    amount = 10
    coins = [10]
    print(sln.change(amount, coins))