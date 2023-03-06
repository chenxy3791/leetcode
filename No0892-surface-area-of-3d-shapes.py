""" 
892. Surface Area of 3D Shapes
On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
关键是确定被隐藏掉的表面的个数
每个面邻接导致两个表面被隐藏
两个相邻节点上的塔邻接的面的个数由两个塔的立方体个数的较小值决定
对节点进行行扫描（当然列扫描也可以），计算各节点与自己右边和下边的节点上的塔的邻接面数。

不要忘了塔本身上下重叠而隐藏的面

Example 1:
Input: [[2]]
Output: 10
每个立方体表面积为6，两个摞在一起的话，有两个表面被隐藏了，所以总表面积为2*6-2=10

Example 2:
Input: [[1,2],[3,4]]
Output: 34

Example 3:
Input: [[1,0],[0,2]]
Output: 16

Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

"""
import math
import time
import numpy as np

class Solution:
    #def surfaceArea(self, grid: List[List[int]]) -> int:
    def surfaceArea(self, grid) -> int:
        if len(grid) == 0:
            return 0
        N = len(grid)
        totalArea = 0
        overlap   = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] > 0:
                    totalArea += grid[r][c] * 6 - (grid[r][c] - 1) * 2
                # print(r,c,totalArea)
                #Count the neighbouring surfaces with right nodes
                if c < N - 1:
                    overlap += min(grid[r][c], grid[r][c+1])
                #Count the neighbouring surfaces with down nodes
                if r < N - 1:
                    overlap += min(grid[r][c], grid[r+1][c])
        # print(totalArea, overlap)
        totalArea -= 2*overlap
        return totalArea
                           
if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    grid = [[2]]
    tStart= time.time()
    print(sln.surfaceArea(grid))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    grid = [[1,0],[0,2]]
    tStart= time.time()
    print(sln.surfaceArea(grid))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase3 ...')
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    tStart= time.time()
    print(sln.surfaceArea(grid))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))        

    print('\ntestcase4 ...')
    grid = [[2,2,2],[2,1,2],[2,2,2]]
    tStart= time.time()
    print(sln.surfaceArea(grid))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))          
    