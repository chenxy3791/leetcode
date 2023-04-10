# -*- coding: utf-8 -*-
"""
Created on Sun May 22 10:36:49 2022

@author: Dell
"""
import time
# class Solution:
#     def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
#         @cache
#         def dfs(usedNumbers: int, currentTotal: int) -> bool:
#             for i in range(maxChoosableInteger):
#                 if (usedNumbers >> i) & 1 == 0:
#                     if currentTotal + i + 1 >= desiredTotal or not dfs(usedNumbers | (1 << i), currentTotal + i + 1):
#                         return True
#             return False

#         return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        memo = dict()
        def dp(usedNumbers: int, currentTotal: int) -> bool:
            if (usedNumbers,currentTotal) in memo:
                return memo[(usedNumbers,currentTotal)]
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i) & 1 == 0:
                    if currentTotal + i + 1 >= desiredTotal or not dp(usedNumbers | (1 << i), currentTotal + i + 1):
                        memo[(usedNumbers,currentTotal)] = True
                        return True
            memo[(usedNumbers,currentTotal)] = False
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dp(0, 0)

if __name__ == "__main__":
    
    sln = Solution() 
    
    maxChoosableInteger = 10
    desiredTotal = 11
    print(sln.canIWin(maxChoosableInteger, desiredTotal))
    
    maxChoosableInteger = 10
    desiredTotal = 0
    print(sln.canIWin(maxChoosableInteger, desiredTotal))
    
    maxChoosableInteger = 10
    desiredTotal = 1
    print('maxChoosable={0}, desired={1}, ans={2}' \
          .format(maxChoosableInteger,desiredTotal,sln.canIWin(maxChoosableInteger, desiredTotal)))
    
        
    maxChoosableInteger = 20
    desiredTotal = 140
    tic = time.time()
    ans = sln.canIWin(maxChoosableInteger, desiredTotal)
    toc = time.time()
    print('maxChoosable={0}, desired={1}, ans={2}, tcose={3:4.2f}(sec)'.format(maxChoosableInteger,desiredTotal,ans,toc-tic))