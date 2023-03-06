# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 07:59:55 2021

@author: chenxy

1198. 找出所有行中最小公共元素
给你一个矩阵 mat，其中每一行的元素都已经按 严格递增 顺序排好了。请你帮忙找出在所有这些行中 最小的公共元素。

如果矩阵中没有这样的公共元素，就请返回 -1。

 

示例：

输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
输出：5
 

提示：

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] 已按严格递增顺序排列。

"""

class Solution:
    # def smallestCommonElement(self, mat: List[List[int]]) -> int:
    def smallestCommonElement(self, mat) -> int:            
        m = len(mat)    # number of rows
        n = len(mat[0]) # number of cols
        if m == 0 or n == 0: 
            return -1
        
        max0 = mat[0][0]
        row0 = 0
        
        while 1:
            print('max0 = {0}, row0 = {1}'.format(max0,row0))
            gotonext = 0
            for k in range(0,m):
                equal = 0
                row = (row0+1) % m 
                for j in range(n):
                    if mat[k][j] == max0:
                        equal = 1
                        break
                    elif mat[k][j] > max0:
                        max0 = mat[k][j]
                        row0 = k
                        gotonext = 1
                        break
                if gotonext == 1:
                    break
                if equal == 0:
                    return -1
            if gotonext == 0:
                return max0

if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()

    mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]    
    print(sln.smallestCommonElement(mat))            
                    
    mat = [[1,2,3,4,5],[2,4,5,8,10],[3,6,7,9,11],[1,3,5,7,9]]    
    print(sln.smallestCommonElement(mat))                
                
                
        