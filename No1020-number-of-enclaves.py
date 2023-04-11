# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        
        R,C       = len(grid),len(grid[0])
        totalGridCnt = 0
        for r in range(1,len(grid)-1):
            for c in range(1,len(grid[0])-1):
                if grid[r][c] == 1:
                    isClosedIsland = True
                    gridCnt = 1
                    q = deque([(r,c)])
                    grid[r][c] = 0
                    while len(q)>0:
                        # (r0,c0) = q.popleft()
                        (r0,c0) = q.pop()
                        for x,y in [(r0-1,c0),(r0+1,c0),(r0,c0-1),(r0,c0+1)]:
                            if 0<=x<R and 0<=y<C and grid[x][y]==1:
                                if x==0 or x==R-1 or y==0 or y==C-1: # Not closed island
                                    isClosedIsland = False
                                # Even not closed island, the search has to continue to flag the island.
                                q.append((x,y))
                                grid[x][y] = 0
                                gridCnt += 1
                    totalGridCnt = totalGridCnt + (gridCnt if isClosedIsland else 0)
        return totalGridCnt
                        
if __name__ == '__main__':
    sln = Solution()

    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    print(sln.numEnclaves(grid))
    
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    print(sln.numEnclaves(grid))