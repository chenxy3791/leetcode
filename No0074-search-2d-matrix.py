# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 07:57:30 2021

@author: chenxy

74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

"""

class Solution:
    #def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target) -> bool:
        
        def addr(x,n):
            x1 = x // n
            x2 = x % n            
            return x1,x2

        m = len(matrix)
        n = len(matrix[0])

        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
                            
        left = 0
        right = m*n-1
        
        while left <= right:            
            mid = left + (right - left)//2
            print(left, right, mid)            
            x1,x2 = addr(mid,n)
            if target < matrix[x1][x2]:
                right = mid - 1
            elif target > matrix[x1][x2]:
                left  = mid + 1
            else:
                return True            
        return False

if __name__ == '__main__':        
    #import time
    sln = Solution()

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 61
    print(matrix, ' --> ', sln.searchMatrix(matrix, target))      

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(matrix, ' --> ', sln.searchMatrix(matrix, target))      
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(matrix, ' --> ', sln.searchMatrix(matrix, target))      