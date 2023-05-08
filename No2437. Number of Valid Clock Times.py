# -*- coding: utf-8 -*-
"""
Created on Tue May  9 07:40:52 2023

@author: chenxy

2437. Number of Valid Clock Times
You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

 

Example 1:

Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
Example 2:

Input: time = "0?:0?"
Output: 100
Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
Example 3:

Input: time = "??:??"
Output: 1440
Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.
 

Constraints:

time is a valid string of length 5 in the format "hh:mm".
"00" <= hh <= "23"
"00" <= mm <= "59"
Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.
"""
import os
# import time
import random
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right
from   functools import reduce

class Solution:
    def countTime(self, time: str) -> int:
        '''
        The number of possible digits in different place is different
        time[0]: 0,1,2
        time[1]: depends on time[0]
            time[0]=0: 0,1,2,3,...,9
            time[0]=1: 0,1,2,3,...,9
            time[0]=2: 0,1,2,3
        time[3]: 0,1,2,3,4,5
        time[4]: 0,1,2,3,4,5,6,...,9
        
        '''
        prod = 1
        if time[3] == '?':
            prod *= 6
        if time[4] == '?':
            prod *= 10
        if time[0] == '?' and time[1] != '?':
            prod *= 3 if int(time[1]) < 4 else 2
        elif time[0] != '?' and time[1] == '?':
            prod *= 4 if time[0] == '2' else 10
        elif time[0] == '?' and time[1] == '?':
            prod *= 24            
                            
        return prod
    
if __name__ == '__main__':
        
    sln  = Solution()                

    time = "?5:00"
    print(sln.countTime(time))            
    
    time = "0?:0?"
    print(sln.countTime(time))            

    time = "??:??"
    print(sln.countTime(time))                