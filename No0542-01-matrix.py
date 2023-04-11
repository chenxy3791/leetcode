# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R,C   = len(mat),len(mat[0])
        q     = deque()
        visited = set()
        for r in range(R):
            for c in range(C):
                if mat[r][c]==0:
                    for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                        if 0<=x<R and 0<=y<C and mat[x][y]==1:
                            q.append((r,c,0))
                            break
        if len(q) == 0: return mat
        while len(q) > 0:
            r,c,layer = q.popleft()
            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=x<R and 0<=y<C and mat[x][y]==1 and (x,y) not in visited:
                    visited.add((x,y))
                    q.append((x,y,layer+1))
                    mat[x][y] = layer+1
        return mat
                        
if __name__ == '__main__':
    sln = Solution()

    mat = [[1]]
    print(sln.updateMatrix(mat))  

    mat = [[0]]
    print(sln.updateMatrix(mat))  
    
    mat = mat = [[0,1],[1,0]]
    print(sln.updateMatrix(mat))  
    
    mat = mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(sln.updateMatrix(mat))  

    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(sln.updateMatrix(mat))  
