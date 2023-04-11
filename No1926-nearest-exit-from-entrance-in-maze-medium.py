# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        R,C    = len(maze),len(maze[0])
        offset = [(1,0),(0,1),(-1,0),(0,-1)]
        
        if maze[0][0] ==0 or maze[R-1][C-1] == 0:
            return -1
        
        q  = deque([(entrance[0],entrance[1],0)])
        maze[entrance[0]][entrance[1]] = '+'
        
        while len(q) > 0:
            r,c,layer = q.popleft()
            # print(r,c,layer)
            # Judge whether it is exit
            if (r==0 or r==R-1 or c==0 or c==C-1) and [r,c]!=entrance:
                return layer
            # Find neighbour empty grids
            for x,y in [(r+offset[k][0],c+offset[k][1]) for k in range(len(offset))]:
                if 0<=x<R and 0<=y<C and maze[x][y]=='.':
                    q.append((x,y,layer+1))
                    maze[x][y] = '+'
        return -1
                        
if __name__ == '__main__':
    sln = Solution()

    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    print(sln.nearestExit(maze,entrance))  

    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    print(sln.nearestExit(maze,entrance))  
    
    maze = [[".","+"]]
    entrance = [0,0]
    print(sln.nearestExit(maze,entrance))  
    
    maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+","+","."]]
    entrance = [0,1]
    tstart = time.time()
    ans = sln.nearestExit(maze,entrance)
    tstop  = time.time()
    print('ans = {0}, tcost = {1:}'.format(ans, tstop-tstart))