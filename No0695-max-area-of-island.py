""" 
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
"""
解题思路：
图论中的求连通区域的问题。
扫描每一个未被访问的node，以之为起点，进行深度优先搜索，所能访问到的node总数即为该岛屿的面积。
然后比较各岛屿的面积求最大值即可。
深度优先搜索或广度优先搜索都可以。
"""
from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Assuming non-empty input matrix.
        maxSize = 0
        nrow = len(grid)
        ncol = len(grid[0])

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print('i = {0}, j = {1}'.format(i,j))
                if (i,j) in visited or grid[i][j] == 0:
                    continue

                q = [(i,j)]
                visited.add((i,j))
                cursize = 0
                while len(q) > 0:
                    a = q.pop()
                    cursize += 1
                    # Add all non-0 neighbours of a into q, if not in visted                                                                                
                    # UP
                    if a[0]-1 >= 0:
                        b = (a[0]-1,a[1])
                        if b not in visited and grid[b[0]][b[1]] == 1:
                            visited.add(b)                        
                            q.append(b)           
                    # DOWN
                    if a[0]+1 < nrow:
                        b = (a[0]+1,a[1])
                        if b not in visited and grid[b[0]][b[1]] == 1:
                            visited.add(b)                        
                            q.append(b)
                    # LEFT
                    if a[1]-1 >= 0:
                        b = (a[0],a[1]-1)
                        if b not in visited and grid[b[0]][b[1]] == 1:
                            visited.add(b)                        
                            q.append(b)           
                    # RIGHT
                    if a[1]+1 < ncol:                    
                        b = (a[0],a[1]+1)
                        if b not in visited and grid[b[0]][b[1]] == 1:
                            visited.add(b)                        
                            q.append(b)           
                if cursize > maxSize:
                    maxSize = cursize

        return maxSize

    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        
        R,C       = len(grid),len(grid[0])
        maxArea   = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):                
                if grid[r][c] == 1:
                    area = 1
                    # print(grid,r,c)
                    q = deque([(r,c)])
                    grid[r][c] = 0
                    while len(q)>0:
                        # (r0,c0) = q.popleft() # Used as queue, to implement BFS
                        (r0,c0) = q.pop() # Used as stack, to implement DFS
                        for x,y in [(r0-1,c0),(r0+1,c0),(r0,c0-1),(r0,c0+1)]:
                            if 0<=x<R and 0<=y<C and grid[x][y]==1:
                                q.append((x,y))
                                grid[x][y] = 0
                                area += 1
                    maxArea = area if area > maxArea else maxArea
        return maxArea
        
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()        

    print('\nTestcase1 ...')
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sln.maxAreaOfIsland(grid))
    print(sln.maxAreaOfIsland2(grid))
    
    print('\nTestcase2 ...')
    grid = [[0,0,0,0,0,0,0,0]]
    print(sln.maxAreaOfIsland(grid))
    print(sln.maxAreaOfIsland2(grid))