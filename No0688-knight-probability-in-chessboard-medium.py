# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:51:12 2022
@author: chenxy

688. 骑士在棋盘上的概率
在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。
行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
(注，类似于中国象棋中的‘马走日’，只不过中国象棋的棋子在格点上，国际象棋的棋子是在格子内)

每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

示例 1：
输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。

示例 2：
输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
 
提示:
1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/knight-probability-in-chessboard
"""

from collections import defaultdict
import time
import numpy as np

class Solution:
    def knightProbability_matpower(self, n: int, k: int, row: int, col: int) -> float:
        delta = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        # 1. Create row vector to represent prob state 
        p0            = np.zeros((1,n*n))
        p0[0][row*n+col] = 1 
        # 2. Create prob transition matrix
        T = np.zeros((n*n, n*n))
        for l in range(n*n): # for each row of T. Transition from cell#l
            # Fill T according to the reachability from cell#r
            l_row = l // n
            l_col = l % n
            for m in range(8):
                r_new,c_new = l_row + delta[m][0], l_col + delta[m][1]
                if r_new>=0 and r_new<n and c_new>=0 and c_new<n:
                    T[l][r_new * n + c_new] = 1        
        T  /= 8
        # print(T,p0)

        # 3. Calculate the final prob state after k steps
        Tk = np.eye(n*n)
        for j in range(0,k):
            Tk = Tk @ T
        pk = p0 @ Tk
            
        # 4. Calculate the probability inside the board after k steps
        return np.sum(pk,1)[0]
        
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        # Add memoization technique.
        nextcell = defaultdict(list)
        for r in range(n):
            for c in range(n):                
                r_tmp,c_tmp = r+1,c+2
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))
                r_tmp,c_tmp = r+2,c+1
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                    
                r_tmp,c_tmp = r+2,c-1
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                                    
                r_tmp,c_tmp = r+1,c-2
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                    
                r_tmp,c_tmp = r-1,c-2
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                    
                r_tmp,c_tmp = r-2,c-1
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                    
                r_tmp,c_tmp = r-2,c+1
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                    
                r_tmp,c_tmp = r-1,c+2
                nextcell[(r,c)].append(((r_tmp if r_tmp>=0 and r_tmp<n else -1), (c_tmp if c_tmp>=0 and c_tmp<n else -1)))                                    

        memo = dict()
                
        def dp(row,col,k):        
            if (row,col,k) in memo:
                return memo[(row,col,k)]
            if k == 0:
                return 1 if row >= 0 and row < n and col >= 0 and col < n else 0
            if row < 0 or col < 0 or row >= n or col >= n:
                return 0

            nxt = nextcell[(row,col)]
            p   = 0
            # print(nxt)
            for m in range(8):
                # print(m)
                if m >= len(nxt):
                    print(row,col,k,m,nxt)
                cellnext = nxt[m]
                p = p + dp(cellnext[0],cellnext[1],k-1)/8
            # print('dp({0},{1},{2} = {3})'.format(row,col,k,p))
            memo[(row,col,k)] = p
            return p

        return dp(row,col,k)

if __name__ == '__main__':        
    
    sln = Solution()

    n,k,row,col = 3, 2, 0, 0
    print(sln.knightProbability(n, k, row, col))
    print(sln.knightProbability_matpower(n, k, row, col))

    n,k,row,col = 1, 0, 0, 0
    print(sln.knightProbability(n, k, row, col))         
    print(sln.knightProbability_matpower(n, k, row, col))       
    
    n,k,row,col = 6, 12, 5, 4
    tStart = time.time()
    p = sln.knightProbability(n, k, row, col)
    tCost = time.time() - tStart
    print('knightProbability({0},{1},{2},{3}) = {4}, tCost = {5}(sec)'.format(n,k,row,col,p,tCost))    

    tStart = time.time()
    p = sln.knightProbability_matpower(n, k, row, col)
    tCost = time.time() - tStart
    print('knightProbability({0},{1},{2},{3}) = {4}, tCost = {5}(sec)'.format(n,k,row,col,p,tCost))    
    
    n,k,row,col = 8, 30, 6, 4
    tStart = time.time()
    p = sln.knightProbability(n, k, row, col)
    tCost = time.time() - tStart
    print('knightProbability({0},{1},{2},{3}) = {4}, tCost = {5}(sec)'.format(n,k,row,col,p,tCost))    
    tStart = time.time()
    p = sln.knightProbability_matpower(n, k, row, col)
    tCost = time.time() - tStart
    print('knightProbability({0},{1},{2},{3}) = {4}, tCost = {5}(sec)'.format(n,k,row,col,p,tCost))    
    
    n,k,row,col = 10, 13, 5, 3
    tStart = time.time()
    p = sln.knightProbability(n, k, row, col)
    tCost = time.time() - tStart
    print('knightProbability({0},{1},{2},{3}) = {4}, tCost = {5}(sec)'.format(n,k,row,col,p,tCost))
    tStart = time.time()
    p = sln.knightProbability_matpower(n, k, row, col)
    tCost = time.time() - tStart
    print('knightProbability({0},{1},{2},{3}) = {4}, tCost = {5}(sec)'.format(n,k,row,col,p,tCost))        
                