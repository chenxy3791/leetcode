# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if len(grid2)==0 or len(grid2[0])==0:
            return 0
        
        R,C          = len(grid2),len(grid2[0])
        subIslandCnt = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):                
                if grid2[r][c] == 1:
                    island = [(r,c)]
                    q = deque([(r,c)])
                    grid2[r][c] = 0
                    while len(q)>0:
                        # (r0,c0) = q.popleft() # Used as queue, to implement BFS
                        (r0,c0) = q.pop() # Used as stack, to implement DFS
                        for x,y in [(r0-1,c0),(r0+1,c0),(r0,c0-1),(r0,c0+1)]:
                            if 0<=x<R and 0<=y<C and grid2[x][y]==1:
                                island.append((x,y))
                                q.append((x,y))
                                grid2[x][y] = 0
                    # check whether this island is a sub-island of grid1
                    print(island)
                    isSubIsland = True
                    for xy in island:
                        if grid1[xy[0]][xy[1]] == 0:
                            isSubIsland = False
                            break
                    if isSubIsland:
                        subIslandCnt += 1
                        
        return subIslandCnt
                        
if __name__ == '__main__':
    sln = Solution()

    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    print(sln.countSubIslands(grid1,grid2))  
    
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(sln.countSubIslands(grid1,grid2))
