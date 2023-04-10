# -*- coding: utf-8 -*-
"""
Created on Thu May 26 05:39:27 2022

@author: Dell
"""
from typing import List
# class Solution:
#     def fallingSquares(self, positions: List[List[int]]) -> List[int]:
#         h = max(map(lambda x: x[0]+x[1], positions)) * [0]
#         ans = len(positions) * [0]
#         for i,pos in enumerate(positions):
#             maxtmp = max(h[pos[0]:pos[0]+pos[1]])
#             for k in range(pos[0],pos[0]+pos[1]):
#                 h[k] = maxtmp + pos[1]
#             if i == 0:    
#                 ans[0] = h[pos[0]]
#             else:
#                 ans[i] = max(ans[i-1],h[pos[0]])

#         return ans      

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def isOverlap(i,j):
            i_x,i_y = positions[i][0], positions[i][0]+positions[i][1]
            j_x,j_y = positions[j][0], positions[j][0]+positions[j][1]
            return (i_x-j_y) * (i_y-j_x) < 0
                
        ans = len(positions) * [0]
        for i in range(len(positions)):
            for j in range(i):
                if isOverlap(i, j):
                    # print(i,j)
                    ans[i] = max(ans[i],ans[j])
            ans[i] += positions[i][1]
                
        for i in range(1,len(ans)):
            ans[i] = max(ans[i-1],ans[i])

        return ans    
    
if __name__ == "__main__":
    
    sln = Solution()    
    
    positions = [[1, 2], [2, 3], [6, 1]]
    print(sln.fallingSquares(positions))
    
    
    positions = [[100, 100], [200, 100]]
    print(sln.fallingSquares(positions))
    
    positions = [[1,2],[1,3]]
    print(sln.fallingSquares(positions))