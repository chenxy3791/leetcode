# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 08:45:15 2023

@author: chenxy

剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200

2023-03-08
执行用时：48 ms, 在所有 Python3 提交中击败了74.83%的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了5.26%的用户
通过测试用例：61 / 61

执行用时：40 ms, 在所有 Python3 提交中击败了96.77%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了92.73%的用户
通过测试用例：61 / 61

"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

class Solution:
    # def maxValue(self, grid: List[List[int]]) -> int:
    #     n,m = len(grid),len(grid[0])
    #     s = [ [0 for j in range(m) ] for i in range(n)]
    #     # print(s)
    #     s[n-1][m-1] = grid[n-1][m-1]
    #     for i in range(n-2,-1,-1):        
    #         s[i][m-1] = grid[i][m-1] + s[i+1][m-1]
    #     for j in range(m-2,-1,-1):        
    #         s[n-1][j] = grid[n-1][j] + s[n-1][j+1]
        
    #     for i in range(n-2,-1,-1):
    #         for j in range(m-2,-1,-1):
    #             s[i][j] = grid[i][j] + max(s[i+1][j],s[i][j+1])

    #     # print(s)
    #     return s[0][0]

    def maxValue(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        s = [ 0 for j in range(m) ]
        # print(s)
        s[m-1] = grid[n-1][m-1]
        for j in range(m-2,-1,-1):        
            s[j] = grid[n-1][j] + s[j+1]
        
        for i in range(n-2,-1,-1):
            s[m-1] = grid[i][m-1] + s[m-1]
            for j in range(m-2,-1,-1):
                s[j] = grid[i][j] + max(s[j],s[j+1])
        return s[0]

if __name__ == '__main__':

    sln  = Solution()                
    
    grid = [ [1,3,1],  [1,5,1],  [4,2,1]]
    print(sln.maxValue(grid))
            
    grid = [[1,2,5],[3,2,1]]
    print(sln.maxValue(grid))

