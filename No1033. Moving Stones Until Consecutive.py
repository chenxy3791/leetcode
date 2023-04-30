# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:02:33 2023

@author: chenxy

1033. Moving Stones Until Consecutive
There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.
 

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
Example 2:

Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.
Example 3:

Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
 

Constraints:

1 <= a, b, c <= 100
a, b, and c have different values.
"""

import time
import random
import time
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        res = [2, z - x - 2]
        if ((z - y) == 1 and (y - x) == 1):
            res[0] = 0
        elif ((z - y) <= 2 or (y - x) <= 2):
            res[0] = 1
        return res
        
if __name__ == '__main__':

    sln  = Solution()                
    
    a = 1; b = 2; c = 5
    print(sln.numMovesStones(a,b,c))              
    
    a = 4; b = 3; c = 2
    print(sln.numMovesStones(a,b,c))              
    
    a = 3; b = 5; c = 1
    print(sln.numMovesStones(a,b,c))              