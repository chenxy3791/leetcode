# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:54:12 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        R,C        = len(heights),len(heights[0])

        q          = deque([(0,k) for k in range(C)] + [(k,0) for k in range(1,R)])
        connected1 = set([(0,k) for k in range(C)] + [(k,0) for k in range(1,R)])
        
        while len(q) > 0:
            r,c = q.popleft()
            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=x<R and 0<=y<C and (x,y) not in connected1:
                    if heights[x][y] >= heights[r][c]:
                        connected1.add((x,y))
                        q.append((x,y))
        print(connected1)

        q          = deque([(R-1,k) for k in range(C)] + [(k,C-1) for k in range(R-1)])
        connected2 = set([(R-1,k) for k in range(C)] + [(k,C-1) for k in range(R-1)])
        
        while len(q) > 0:
            r,c = q.popleft()
            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=x<R and 0<=y<C and (x,y) not in connected2:
                    if heights[x][y] >= heights[r][c]:
                        connected2.add((x,y))
                        q.append((x,y))
        print(connected2)
            
        return list(connected2.intersection(connected1))
                        
if __name__ == '__main__':
    sln = Solution()

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sln.pacificAtlantic(heights))  

    heights = [[2,1],[1,2]]
    print(sln.pacificAtlantic(heights))  
