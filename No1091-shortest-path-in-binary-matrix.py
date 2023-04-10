# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        R,C    = len(grid),len(grid[0])
        if grid[0][0] !=0 or grid[R-1][C-1] != 0:
            return -1
        
        offset = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        q      = deque([(0,0,1)])
        
        if len(q) == 0: return -1
        
        while len(q) > 0:
            r,c,layer = q.popleft()
            if (r,c) == (R-1,C-1):
                return layer
            for x,y in [(r+offset[k][0],c+offset[k][1]) for k in range(8)]:
                if 0<=x<R and 0<=y<C and grid[x][y]==0:
                    q.append((x,y,layer+1))
                    grid[x][y] = 1
                    
        return -1
                        
if __name__ == '__main__':
    sln = Solution()

    grid = [[1]]
    print(sln.shortestPathBinaryMatrix(grid))  

    grid = [[0]]
    print(sln.shortestPathBinaryMatrix(grid))  
    
    grid = grid = [[0,1],[1,0]]
    print(sln.shortestPathBinaryMatrix(grid))  
    
    grid = grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(sln.shortestPathBinaryMatrix(grid))  

    grid = [[1,0,0],[1,1,0],[1,1,0]]
    print(sln.shortestPathBinaryMatrix(grid))  
