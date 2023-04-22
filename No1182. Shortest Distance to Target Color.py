# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:38:47 2023

@author: chenxy

1182. Shortest Distance to Target Color
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.


Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).

Example 2:
Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 

Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
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
from bisect import bisect, bisect_left, bisect_right

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        '''
        执行用时：268 ms, 在所有 Python3 提交中击败了93.02%的用户
        内存消耗：32.8 MB, 在所有 Python3 提交中击败了24.42%的用户
        '''
        ret = []
        hc  = defaultdict(list)
        for k,c in enumerate(colors):
            hc[c].append(k)
            
        for q in queries:
            i,c = q[0],q[1]
            if c not in hc:
                ret.append(-1)
            else:
                #ret.append(min([ abs(j - i) for j in hc[c] ])) 
                c_idxes = hc[c]                
                tmp = bisect_left(c_idxes,i)
                # print(c,c_idxes, i, tmp)
                if tmp == 0:
                    ret.append(abs(c_idxes[0] - i))
                elif tmp == (len(c_idxes)):
                    ret.append(abs(c_idxes[-1] - i))
                else:
                    ret.append(min(abs(c_idxes[tmp-1] - i), abs(c_idxes[tmp] - i)))
        
        return ret

if __name__ == '__main__':

    sln  = Solution()                
    
    colors = [1,1,2,1,3,2,2,3,3]; queries = [[1,3],[2,2],[6,1]]
    print(sln.shortestDistanceColor(colors,queries))             
    
    colors = [1,2]; queries = [[0,3]]
    print(sln.shortestDistanceColor(colors,queries))             