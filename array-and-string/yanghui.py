# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:29:22 2019

@author: chenxy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

"""

class Solution:
    def generateRecursion(self, numRows: int): # -> list[list[int]]:

        print('Call generateRecursion with numRows = {0}'.format(numRows))

        if numRows < 0:
            print('Warining: numRows should be nongative integers!')
            return []

        if numRows == 0:
            return []

        if numRows == 1:
            return [1]
        
        if numRows == 2:
            return [[1], [1,1]]
                
        yangh   = self.generateRecursion(numRows-1)  # Generate lower order by 1      
        lastRow = yangh[-1] # Take the last row for the calculation of new row
        
        newRow = [1] # The first element must be 1
        
        for k in range(1,len(lastRow)):
            newRow.append(lastRow[k-1] + lastRow[k])
            
        newRow.append(1)  # The last element must be 1 too
        yangh.append(newRow)
        
        return yangh
    
    def generateDirect(self, numRows: int):
        yangh = []
        
        if numRows >= 1:
            yangh.append([1])
            
        if numRows >= 2:   
            yangh.append([1,1])
            
        if numRows > 2:      
            for k in range(2,numRows): # Generate each row iteratively
                newRow = [1]  
                for j in range(1,k):
                    newRow.append(yangh[k-1][j-1] + yangh[k-1][j])
                newRow.append(1)    
                yangh.append(newRow)        
                
        if numRows < 0:
            print('generateDirect: numRows should be non-negative integer!')
                
        return yangh
    
    def printYangHuiDirect(self, numRows: int):
        print('Call printYangHuiDirect...')
        yangh = self.generateDirect(numRows)        
        for k in range(numRows):
            print(yangh[k])
            
        print('\n')
        return

    def printYangHuiRecursion(self, numRows: int):
        print('Call printYangHuiRecursion...')
        yangh = self.generateRecursion(numRows)
        for k in range(numRows):
            print(yangh[k])
        print('\n')
        return

if __name__ == '__main__':    
    # [1,2,3,4]            
    sln = Solution()
    yangh = sln.printYangHuiDirect(10)

    yangh = sln.printYangHuiRecursion(10)    
    