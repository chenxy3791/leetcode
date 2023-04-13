"""
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 
Constraints:
n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4

"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it
import bisect

class Solution:
    def maxAreaNaive(self, height: List[int]) -> int:

        if len(height) == 2:
            return min(height)
        aMax = 0;
        for k in range(len(height)-1):
            for j in range(k+1,len(height)):
                area = min(height[k],height[j]) * (j-k)
                if area > aMax:
                    aMax = area
        return aMax

    def maxArea(self, height: List[int]) -> int:

        fptr = 0
        bptr = len(height) - 1
        aMax = 0
        while bptr > fptr:
            #print(fptr, bptr)
            if height[bptr] < height[fptr]:
                area = (bptr - fptr) * height[bptr]
                bptr -= 1
            else:
                area = (bptr - fptr) * height[fptr]
                fptr += 1                        
            if area > aMax:
                aMax = area            
        return aMax                

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    height = [1,8,6,2,5,4,8,3,7]    
    print('Expected = 49; result = {0}'.format(sln.maxArea(height)))

    print('Testcase2...')
    import random
    import time
    height = []
    for i in range(5000):
        n = random.randint(1,1000)
        height.append(n)
    print(height[:10])         
    tStart = time.time()        
    print('Expected = ???; result = {0}'.format(sln.maxArea(height)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')