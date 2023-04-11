# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 09:43:56 2022

@author: Dell
"""

import time
from typing import List

class Solution:
    # def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
    #     childs = dict()
    #     for k in range(n):
    #         childs[k] = []
        
    #     for k in range(n):
    #         parent = manager[k]
    #         if parent in childs:
    #             childs[parent].append(k)
        
    #     def dfs(root) -> int:
    #         # The longest time cost from the specified root, to the leaf of its subtree
    #         longestTime = 0
    #         for child in childs[root]:
    #             t = dfs(child)
    #             longestTime = t if t > longestTime else longestTime
    #         return longestTime + informTime[root]
        
    #     return dfs(headID)
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        memo = dict()
        memo[headID] = 0
        
        def dp(staff:int) -> int:
            if staff in memo:
                return memo[staff]
            t = dp(manager[staff]) + informTime[manager[staff]]
            memo[staff] = t
            return t
        
        maxT = 0
        for k in range(n):
            t = dp(k)
            maxT = t if t > maxT else maxT
        
        return maxT
    
if __name__ == "__main__":
    
    sln = Solution()
    
    n = 1
    headID = 0
    manager = [-1]
    informTime = [0]
    print(sln.numOfMinutes(n, headID, manager, informTime))
    
    n = 6 
    headID = 2
    manager = [2,2,-1,2,2,2] 
    informTime = [0,0,1,0,0,0]
    print(sln.numOfMinutes(n, headID, manager, informTime))