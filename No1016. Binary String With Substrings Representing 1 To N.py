# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:43:56 2023

@author: chenxy

1016. Binary String With Substrings Representing 1 To N
Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "0110", n = 3
Output: true
Example 2:

Input: s = "0110", n = 4
Output: false
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= n <= 10**9
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
    def queryString(self, s: str, n: int) -> bool:
        for k in range(1,n+1):
            # print(bin(k)[2:])
            if s.find(bin(k)[2:]) < 0:
                return False
        return True
        
if __name__ == '__main__':
        
    sln  = Solution()                

    s = "0110"; n = 3
    print(sln.queryString(s,n))           
    
    s = "0110"; n = 4
    print(sln.queryString(s,n))           