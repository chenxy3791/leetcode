# -*- coding: utf-8 -*-
"""
Created on Fri May  6 06:52:28 2022

@author: Dell
"""
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                elif (i==0 or j==0):
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1]) + 1
               
                ans = max(ans,matrix[i][j])
        return ans*ans
                    
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     m,n = len(matrix),len(matrix[0])
    #     def get(i,j):
    #         if i>=m or j>=n:
    #             return 0
    #         else:
    #             return int(matrix[i][j])
            
    #     maxarea = 0
    #     for i in range(m):
    #         for j in range(n):
    #             # print('.....',i,j)
    #             if get(i,j) == 0:
    #                 continue
    #             else:
    #                 # Find the max square with (i,j) as the top-left corner
    #                 area  = 1
    #                 layer = 1
    #                 flag  = True
    #                 while True:
    #                     for j1 in range(j,j+layer+1):
    #                         if get(i+layer,j1) ==0:
    #                             flag = False
    #                             break
    #                     if flag is False:
    #                         break
                        
    #                     for i1 in range(i,i+layer+1):
    #                         if get(i1,j+layer)==0:
    #                             flag = False
    #                             break
    #                     if not flag:
    #                         break
    #                     # print(i,j,layer,flag)
    #                     area  += 2*layer + 1
    #                     layer += 1
    #                 # print(i,j,layer,area)
    #                 maxarea = max(maxarea,area)
    #     return maxarea

if __name__ == "__main__":
    
    sln = Solution()    
    
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sln.maximalSquare(matrix))
                
    matrix = [["0","1"],["1","0"]]
    print(sln.maximalSquare(matrix))    
    
    matrix = [["0"]]
    print(sln.maximalSquare(matrix))