""" 
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""

import time

class Solution:
    
    #def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid) -> int:
        def neighbours(a):
            neighb = []
            if a[0] > 0: # up
                neighb.append((a[0]-1,a[1]))
            if a[0] < nRow - 1: # down
                neighb.append((a[0]+1,a[1]))            
            if a[1] > 0: # left
                neighb.append((a[0],a[1]-1))            
            if a[1] < nCol - 1: # right
                neighb.append((a[0],a[1]+1))            
            return neighb

        nRow = len(grid)
        if nRow == 0:
            return 0
        nCol = len(grid[0])
        if nCol == 0:            
            return 0

        visited = []
        islands = 0
        for i in range(nRow):
            for j in range(nCol):
                if ((i,j) not in visited) and (grid[i][j]) == '1':
                    #print('(i,j) = ({0},{1})'.format(i,j))
                    qGrids = [(i,j)]
                    visited.append((i,j))
                    while len(qGrids) > 0:
                        a = qGrids.pop(0)
                        if grid[a[0]][a[1]] == '0':
                            continue
                        # Add a's neighbours to qGrid
                        neighb = neighbours(a)
                        #print('({0},{1}) neighbs = {2}'.format(a[0],a[1],neighb))
                        for n in neighb:
                            if (n not in visited):
                                qGrids.append(n)
                                visited.append(n)
                    islands += 1
        return islands       

class Solution1:
    #def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid) -> int:
        nRow = len(grid)
        if nRow == 0:
            return 0
        nCol = len(grid[0])
        if nCol == 0:            
            return 0
        # print('numIslands(): nRow = {0}, nCol = {1}'.format(nRow,nCol))

        def neighbours(a):
            neighb = []
            if a[0] > 0: # up
                neighb.append((a[0]-1,a[1]))
            if a[0] < (nRow - 1): # down
                neighb.append((a[0]+1,a[1]))            
            if a[1] > 0: # left
                neighb.append((a[0],a[1]-1))            
            if a[1] < (nCol - 1): # right
                neighb.append((a[0],a[1]+1))                                    
            return neighb

        islands = 0        
        for i in range(nRow):
            for j in range(nCol):
                if (grid[i][j]) == '0':
                    continue
                #print('New search round start from: (i,j) = ({0},{1})'.format(i,j))
                qGrids = [(i,j)]
                grid[i][j] = '0'
                while len(qGrids) > 0:
                    a = qGrids.pop(0)    
                    #assert(grid[a[0]][a[1]] == '1')                
                    # Add a's neighbours to qGrid
                    neighb = neighbours(a)
                    #print('({0},{1}) neighbs = {2}'.format(a[0],a[1],neighb))
                    for n in neighb:
                        if grid[n[0]][n[1]] == '1':
                            # assert (n[0]<nRow and n[1]<nCol), "n = {0}".format(n)
                            qGrids.append(n)
                            grid[n[0]][n[1]] = '0'
                islands += 1
        return islands

if __name__ == '__main__':

    import numpy as np    
    import os
    import copy

    sln  = Solution()
    sln1  = Solution1()    

    print('\nTestcase#1 ...... start!')
    grid = [['1', '0',  '0',  '0'],    
            ['0', '0',  '1',  '0'],    
            ['0', '1',  '1',  '0'],    
            ['0', '0',  '0',  '1']]
    print(len(grid), len(grid[0]))
    print(sln.numIslands(grid))
    print(sln1.numIslands(grid))

    print('\nTestcase#2 ...... start!')
    grid = [['1', '1',  '1',  '1',  '0'],    
            ['1', '1',  '0',  '1',  '0'],    
            ['1', '1',  '0',  '0',  '0'],    
            ['0', '0',  '0',  '0',  '0']]
    print(len(grid), len(grid[0]))            
    print(sln.numIslands(grid))
    print(sln1.numIslands(grid))

    print('\nTestcase#3 ...... start!')
    nRow = 100
    nCol = 100
    a    = np.random.randint(0,2,[nRow, nCol])    
    a    = a.tolist()
    grid = []
    for b in a:
        grid.append(list(map(str,b)))    
    tStart = time.time()           
    print(sln.numIslands(grid))
    tElapsed = time.time() - tStart        
    print('Solution(): tElapsed = {2}(sec)'.format(len(grid),len(grid[0]),tElapsed))

    tStart = time.time()           
    print(sln1.numIslands(grid))
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(len(grid),len(grid[0]),tElapsed))

    print('\nTestcase#4 ...stress test... start!')        
    # Reference: https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files
    filename = 'No200-numIslands_testdata.py'
    exec(compile(open(filename).read(),'dummy','exec'))        
    # tStart = time.time()       
    # print(sln.numIslands(grid))
    # tElapsed = time.time() - tStart        
    # print('Solution(): tElapsed = {2}(sec)'.format(len(grid),len(grid[0]),tElapsed))

    tStart = time.time()       
    print(sln1.numIslands(grid))
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(len(grid),len(grid[0]),tElapsed))