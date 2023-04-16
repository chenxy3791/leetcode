# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:44:59 2023

@author: Dell

13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
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
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for k,c in enumerate(s):
            if k < len(s)-1 and d[s[k]] < d[s[k+1]]:
                ret -= d[s[k]]
            else:
                ret += d[s[k]]
        return ret
            
    def romanToIntNaive(self, s: str) -> int:
        ptr = 0
        ret = 0
        while ptr < len(s):
            if s[ptr] == 'I':
                if ptr+1 < len(s) and s[ptr+1] == 'V':
                    ret += 4
                    ptr += 2
                elif ptr+1 < len(s) and s[ptr+1] == 'X':
                    ret += 9
                    ptr += 2
                else:
                    ret += 1
                    ptr += 1
            elif s[ptr] == 'X':
                if ptr+1 < len(s) and s[ptr+1] == 'L':
                    ret += 40
                    ptr += 2
                elif ptr+1 < len(s) and s[ptr+1] == 'C':
                    ret += 90
                    ptr += 2
                else:
                    ret += 10
                    ptr += 1
            elif s[ptr] == 'C':
                if ptr+1 < len(s) and s[ptr+1] == 'D':
                    ret += 400
                    ptr += 2
                elif ptr+1 < len(s) and s[ptr+1] == 'M':
                    ret += 900
                    ptr += 2
                else:
                    ret += 100
                    ptr += 1
            elif s[ptr] == 'V':
                ret += 5
                ptr += 1
            elif s[ptr] == 'L':
                ret += 50
                ptr += 1
            elif s[ptr] == 'D':
                ret += 500
                ptr += 1
            elif s[ptr] == 'M':
                ret += 1000
                ptr += 1
        return ret
        
if __name__ == '__main__':

    sln  = Solution()                
    
    s = "III"
    print(sln.romanToInt(s))
    
    s = "LVIII"
    print(sln.romanToInt(s))
    
    s = "MCMXCIV"
    print(sln.romanToInt(s))