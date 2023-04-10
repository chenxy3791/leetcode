# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:06:18 2022

@author: Dell
"""
from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R,C = len(image),len(image[0])
        q = deque()
        visited = set()        
        q.append((sr,sc))
        visited.add((sr,sc))
        
        while len(q) > 0:
            pr,pc = q.popleft()
            
            if pr-1>=0 and image[pr-1][pc]==image[pr][pc] and (pr-1,pc) not in visited:
                q.append((pr-1,pc))
                visited.add((pr-1,pc))

            if pr+1<R and image[pr+1][pc]==image[pr][pc] and (pr+1,pc) not in visited:
                q.append((pr+1,pc))
                visited.add((pr+1,pc))

            if pc-1>=0 and image[pr][pc-1]==image[pr][pc] and (pr,pc-1) not in visited:
                q.append((pr,pc-1))
                visited.add((pr,pc-1))
            
            if pc+1<C and image[pr][pc+1]==image[pr][pc] and (pr,pc+1) not in visited:
                q.append((pr,pc+1))
                visited.add((pr,pc+1))
            
            image[pr][pc] = newColor
        return image
            
        
if __name__ == '__main__':
    sln = Solution()
    
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(sln.floodFill(image, sr, sc, newColor))
    
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2
    print(sln.floodFill(image, sr, sc, newColor))