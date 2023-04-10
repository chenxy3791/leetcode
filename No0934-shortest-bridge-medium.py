# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # print(grid)
        R,C    = len(grid),len(grid[0])
        offset = [(1,0),(0,1),(-1,0),(0,-1)]
        # Search for the first land grid
        flag = False
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    flag = True
                    break
            if flag:
                break
        # print(r,c)
        # Start from (r,c) to tranverse island1 and put the outest land grid of it into queue
        q     = deque([(r,c)])
        q2    = deque([(r,c,0)]) # For the later Multi-Source BFS
        visited = set([(r,c)])
        while len(q) > 0:
            r,c = q.popleft()
            for ofst in offset:
                x,y = r+ofst[0], c+ofst[1]
                if 0<=x<R and 0<=y<C and grid[x][y]==1 and (x,y) not in visited:
                    visited.add((x,y))
                    q.append((x,y))
                    # Whether (x,y) is the outest land grid of the island1?
                    for ofst in offset:
                        x1,y1 = x+ofst[0], y+ofst[1]
                        if 0<=x1<R and 0<=y1<C and grid[x1][y1]==0:
                            q2.append((x,y,0))
                            break
        # print(q2,visited)
        # Multi-source BFS start from q2
        if len(q2) == 0: return 0
        while len(q2) > 0:
            r,c,layer = q2.popleft()
            # print(r,c,layer,visited)
            for ofst in offset:
                x,y = r+ofst[0], c+ofst[1]
                # print(r,c,x,y)
                if 0<=x<R and 0<=y<C and (x,y) not in visited:                    
                    if grid[x][y]==0:
                        q2.append((x,y,layer+1))
                        visited.add((x,y))
                    else:
                        return layer                 
        return -1
                
if __name__ == '__main__':
    sln = Solution()

    A = [[0,1],[1,0]]
    print(sln.shortestBridge(A))  

    A = [[0,1,0],[0,0,0],[0,0,1]]
    print(sln.shortestBridge(A))  
    
    A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(sln.shortestBridge(A))  
    