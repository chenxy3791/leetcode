# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:29:22 2019

@author: chenxy

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
输入: 3
输出: [1,3,3,1]

你可以优化你的算法到 O(k) 空间复杂度吗？--Sure.
"""

class Solution:
    def getRowRecursion(self, rowIndex: int): # -> List[int]:
        
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        yh_row  = self.getRowRecursion(rowIndex-1)        
        
        # Based on row#(rowIndex-1), firstly append 1 to the end.
        yh_row.append(1)
        
        # Then update in the reverse order.
        for k in range(rowIndex-1,0,-1):
            yh_row[k] = yh_row[k] + yh_row[k-1]                                
        
        return yh_row

    def getRowDirect(self, rowIndex: int): # -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1,1]
        
        yh_row = [1,1]
        for jj in range(2,rowIndex+1):        
            # Based on row#(rowIndex-1), firstly append 1 to the end.
            yh_row.append(1)
            
            # Then update in the reverse order.
            for k in range(jj-1,0,-1):
                yh_row[k] = yh_row[k] + yh_row[k-1]                                
            
            #print(jj, yh_row)
        
        return yh_row

    def printYanghRowRecursion(self, rowIndex: int):
        yh_row = self.getRowRecursion(rowIndex)                
        print(yh_row)            
        return

    def printYanghRowDirect(self, rowIndex: int):
        yh_row = self.getRowDirect(rowIndex)                
        print(yh_row)            
        return

if __name__ == '__main__':    
    # [1,2,3,4]            
    sln = Solution()
    sln.printYanghRowRecursion(0)
    sln.printYanghRowRecursion(1)
    sln.printYanghRowRecursion(2)
    sln.printYanghRowRecursion(3)    
    sln.printYanghRowRecursion(10)    
    sln.printYanghRowRecursion(33)

    sln.printYanghRowDirect(33)    
    