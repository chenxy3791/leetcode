# -*- coding: utf-8 -*-
"""
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：

1 <= n <= 10^4

"""

import sys
import time
import datetime
import math
import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
from   math import sqrt, floor, ceil
import numpy 

class Solution:

    def numSquares_bfs_list(self, n: int) -> int:
        queue = deque()
        queue.append((n,0))
        visited = [n]
        
        while queue:
            vertex = queue.popleft()
            residuals = [vertex[0] - k*k for k in range(1,int(vertex[0]**.5)+1)]
            for i in residuals:
                # new_vertex = node(i, vertex[1]+1)
                if i==0:                   
                    return vertex[1]+1
                    
                elif i not in visited:
                    queue.append((i,vertex[1]+1))
                    visited.append(i)
                                        
        return -1

    def numSquares_bfs_set(self, n: int) -> int:
        queue = deque()
        queue.append((n,0))
        visited = set([n])
        
        while queue:
            vertex = queue.popleft()
            residuals = [vertex[0] - k*k for k in range(1,int(vertex[0]**.5)+1)]
            for i in residuals:
                # new_vertex = node(i, vertex[1]+1)
                if i==0:                   
                    return vertex[1]+1
                    
                elif i not in visited:
                    queue.append((i,vertex[1]+1))
                    visited.add(i)
                                        
        return -1

    def numSquares_bfs_set2(self, n: int) -> int:
        queue = deque()
        queue.append((n,0))
        visited = set([n])
        
        while queue:
            vertex = queue.popleft()
            for k in range(1,floor(sqrt(vertex[0])+1)):
                nxtNum = vertex[0] - k*k           
                if nxtNum==0:                   
                    return vertex[1]+1
                    
                elif nxtNum not in visited:
                    queue.append((nxtNum,vertex[1]+1))
                    visited.add(nxtNum)
                                        
        return -1

    def numSquares_bfs_dict(self, n: int) -> int:
        queue = deque()
        queue.append((n,0))
        visited = dict()
        visited[n] = ''
        
        while queue:
            vertex = queue.popleft()
            residuals = [vertex[0] - k*k for k in range(1,int(vertex[0]**.5)+1)]
            for i in residuals:
                # new_vertex = node(i, vertex[1]+1)
                if i==0:                   
                    return vertex[1]+1
                    
                elif i not in visited:
                    queue.append((i,vertex[1]+1))
                    visited[i] = ''
                                        
        return -1
        
    def numSquares_dp(self, n: int) -> int:
                       
        nSqr  = floor(sqrt(n))
        
        # Create a 2-D table to store the value and do the initialization
        table = numpy.zeros((n+1,nSqr+1),dtype='int')
        for k in range(1,nSqr+1):
            table[1,k] = 1        
        for k in range(1,n+1):
            table[k,1] = k

        for k in range(2,n+1):
            # print('k={}'.format(k))
            kSqr = floor(sqrt(k))
            # Fill-in table[k,i]            
            for i in range(2,kSqr+1):
                minValue  = table[k][i-1] # Corresponding to not Using i
                maxUseNum = k//(i**2)                
                for j in range(1,maxUseNum+1):
                    minValue  = min(minValue,j+table[k-j*(i**2)][i-1])
                table[k][i] = minValue                                                   
                # print('table[{0}][{1}] = {2}'.format(k,i,minValue))
                # print(table)

            for i in range(kSqr+1,nSqr+1):
                table[k][i] = table[k][kSqr]

        return table[n][nSqr]

    def numSquares_recursion(self, n: int) -> int:
                        
        memo  = dict()
        m0    = floor(sqrt(n))            
        # dp_cnt= 0 # Only for debug, count the number of dp() calls
        
        def dp(k,m):
            # print('(k,m) = ({0},{1})'.format(k,m))
            # dp_cnt = dp_cnt + 1 # why not work?

            if m == 1:
                return k
            
            if (k,m) in memo:
                return memo[(k,m)]
            
            m2 = m**2
            if m2 == k:
                memo[(k,m)] = 1
                return 1

            tmp = floor(sqrt(k-m2))
            ans = min(dp(k,m-1),1+dp(k-m2,min(m,tmp)))
            memo[(k,m)] = ans
            return ans
                        
        return dp(n,m0)

    def numSquares_recursion2(self, n: int) -> int:
                        
        memo  = dict()
        m0    = floor(sqrt(n))            
        # dp_cnt= 0 # Only for debug, count the number of dp() calls
        
        def dp(k):
            # print('k = {0}'.format(k))
            # dp_cnt = dp_cnt + 1 # why not work?

            if k == 0:
                return 0

            kSqrt    = floor(sqrt(k))            
            
            if k in memo:
                return memo[k]
            
            # m2 = m**2
            # if m2 == k:
            #     memo[(k,m)] = 1
            #     return 1

            minnum = k
            for m in range(1,kSqrt+1):
                tmp    = dp(k - m**2)
                minnum = min(tmp,minnum)
            memo[k] = minnum + 1                       
            return minnum + 1 
                        
        return dp(n)
                    
if __name__ == '__main__':        
    
    sln = Solution()
    
    # for n in range(10,4999,117):
    # for n in range(1000,1001):

    # n = 4696
    n = 9999
    # tStart = time.time()
    # nums = sln.numSquares_recursion(n)
    # tCost = time.time() - tStart
    # print('numSquares_recursion({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))

    # tStart = time.time()
    # nums = sln.numSquares_bfs_list(n)
    # tCost = time.time() - tStart
    # print('numSquares_bfs_list({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))

    tStart = time.time()
    nums = sln.numSquares_bfs_set(n)
    tCost = time.time() - tStart
    print('numSquares_bfs_set({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))

    tStart = time.time()
    nums = sln.numSquares_bfs_set2(n)
    tCost = time.time() - tStart
    print('numSquares_bfs_set2({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))

    tStart = time.time()
    nums = sln.numSquares_bfs_dict(n)
    tCost = time.time() - tStart
    print('numSquares_bfs_dict({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))

    # tStart = time.time()
    # nums = sln.numSquares_recursion2(n)
    # tCost = time.time() - tStart
    # print('numSquares_recursion2({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))
        
        # tStart = time.time()
        # nums = sln.numSquares_dp(n)
        # tCost = time.time() - tStart
        # print('numSquares_dp({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))