# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 08:59:16 2022

@author: chenxy

1380. 矩阵中的幸运数
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
幸运数是指矩阵中满足同时下列两个条件的元素：
在同一行的所有元素中最小
在同一列的所有元素中最大

示例 1：
输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

示例 2：
输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

示例 3：
输入：matrix = [[7,8],[1,2]]
输出：[7]

提示：
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5
矩阵中的所有元素都是不同的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# import numpy as np
# class Solution:
#     def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
#         m = len(matrix)    # number of row
#         n = len(matrix[0]) # number of col
#         A = np.array(matrix)
#         rslt = []
#         for k in range(m):
#             min_idx = np.argmin(A[k,:])
#             col_max = np.max(A[:,min_idx])
#             if col_max == A[k,min_idx]:
#                 rslt.append(col_max)
#         return rslt

class Solution:    
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
# =============================================================================
# 执行用时：96 ms, 在所有 Python3 提交中击败了5.16%的用户
# 内存消耗：32.4 MB, 在所有 Python3 提交中击败了5.16%的用户        
# =============================================================================
        m = len(matrix)    # number of row
        n = len(matrix[0]) # number of col
        rslt = []
        for k in range(m): # Iteration over each row           
            # Find row min and also the min index
            # rowmin,minidx = self.findMin(matrix[k])
            rowmin = matrix[k][0]
            rowminidx = 0
            for col in range(1,n):
                if matrix[k][col] < rowmin:
                    rowmin = matrix[k][col]
                    rowminidx = col

            # Find the max of column[minidx]
            colmax = matrix[0][rowminidx]
            for k in range(1,m):
                if matrix[k][rowminidx] > colmax:
                    colmax = matrix[k][rowminidx]
            # Whether the row-min coincidence with col-max
            if colmax == rowmin:            
                rslt.append(colmax)
        return rslt        

if __name__ == '__main__':        
    
    sln = Solution()

    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(sln.luckyNumbers(matrix))          

    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(sln.luckyNumbers(matrix))                      
    
    matrix = [[7,8],[1,2]]
    print(sln.luckyNumbers(matrix))                          

    matrix = [[7]] # corner case
    print(sln.luckyNumbers(matrix))                          

    matrix = [[8,7],[1,9]]
    print(sln.luckyNumbers(matrix))                              