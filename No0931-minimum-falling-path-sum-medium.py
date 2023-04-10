# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:20:43 2022

@author: Dell
"""
from typing import List
import time
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
#         memo = dict()
        
#         def dp(i,j):
#             if (i,j) in memo:
#                 return memo[(i,j)]
            
#             if j<0 or j>=len(matrix[0]):
#                 return 20000 # Just because -100 <= matrix[i][j] <= 100 and 1 <= n <= 100
#             if i==len(matrix)-1:
#                 return matrix[i][j]
            
#             ans = min(dp(i+1,j-1),dp(i+1,j),dp(i+1,j+1)) + matrix[i][j]
#             memo[(i,j)] = ans
#             return ans
        
#         return min([dp(0,j) for j in range(len(matrix[0]))])

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m > 1:
            for i in range(m - 2, -1, -1):
                for j in range(n):
                    if j==0:
                        matrix[i][j] = min(matrix[i][j] + matrix[i + 1][j],  matrix[i][j] + matrix[i + 1][j + 1])
                    elif j == n - 1:
                        matrix[i][j] = min(matrix[i][j] + matrix[i + 1][j - 1], matrix[i][j] + matrix[i + 1][j])
                    else:    
                        matrix[i][j] = min(min(matrix[i][j] + matrix[i + 1][j - 1],  matrix[i][j] + matrix[i + 1][j]), matrix[i][j] + matrix[i + 1][j + 1])
                    
        return min(matrix[0]);

if __name__ == "__main__":
    
    sln = Solution()
    
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(sln.minFallingPathSum(matrix))
    
    matrix = [[-19,57],[-40,-5]]
    print(sln.minFallingPathSum(matrix))