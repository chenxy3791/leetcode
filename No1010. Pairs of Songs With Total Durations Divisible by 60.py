# -*- coding: utf-8 -*-
"""
Created on Sun May  7 07:42:46 2023

@author: Dell

1010. Pairs of Songs With Total Durations Divisible by 60
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 10**4
1 <= time[i] <= 500
通过次数25,380提交次数53,680

"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
from bisect import bisect, bisect_left, bisect_right

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        h = defaultdict(int)
        
        for k,t in enumerate(time):
            h[t%60] += 1
        print(h)
        total_cnt = 0
        for key in h:
            if key == 0 or key == 30:
                total_cnt += h[key] * (h[key] - 1) 
            else:
                if (60-key) in h:
                    total_cnt += h[60-key] * h[key]
        
        # Note: each pair is counted twice in the above processing.
        # print(total_cnt)
        return total_cnt // 2
        
if __name__ == "__main__":
    
    sln = Solution()  
    
    time = [30,20,150,100,40]
    print(sln.numPairsDivisibleBy60(time))
    
    time = [60,60,60]
    print(sln.numPairsDivisibleBy60(time))
    
    time = [418,204,77,278,239,457,284,263,372,279,476,416,360,18]
    print(sln.numPairsDivisibleBy60(time))