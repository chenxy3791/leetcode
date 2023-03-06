""" 
836. Rectangle Overlap
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the 
coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its 
top-right corner.

Two rectangles overlap if the area of their intersection is positive.  
To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.

解题思路：
右下角坐标取较小值
左上角坐标取较大值
然后看围出来的面积 = (x_rigthbtm - x_btmleft) * (y_rigthbtm - y_btmleft)
面积大于0则表示有overlap

"""
import math
import time
import numpy as np

class Solution:
    #def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        x1_btmleft  = rec1[0]
        y1_btmleft  = rec1[1]
        x2_btmleft  = rec2[0]
        y2_btmleft  = rec2[1]

        x1_topright = rec1[2]
        y1_topright = rec1[3]
        x2_topright = rec2[2]
        y2_topright = rec2[3]

        x_btmleft  = max(x1_btmleft, x2_btmleft)
        y_btmleft  = max(y1_btmleft, y2_btmleft)
        x_topright = min(x1_topright, x2_topright)
        y_topright = min(y1_topright, y2_topright)

        s = (x_topright - x_btmleft) * (y_topright - y_btmleft)
        #print('s = {0}: {1}, {2}, {3}, {4}'.format(s, x_topright, x_btmleft, y_topright, y_btmleft))
        return (s > 0) and (x_topright >= x_btmleft)

if __name__ == '__main__':


    sln   = Solution()

    print('\ntestcase1 ...')
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    tStart= time.time()
    print(sln.isRectangleOverlap(rec1, rec2))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStart))    

    
    print('\ntestcase2 ...')
    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    tStart= time.time()
    print(sln.isRectangleOverlap(rec1, rec2))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStart))    

