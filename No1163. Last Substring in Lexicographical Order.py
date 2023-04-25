# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:09:12 2023

@author: chenxy

1163. Last Substring in Lexicographical Order
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: s = "leetcode"
Output: "tcode"
 

Constraints:

1 <= s.length <= 4 * 10**5
s contains only lowercase English letters.

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
    def lastSubstring_timeout(self, s: str) -> str:
        '''
        Time-out.
        '''
        ret = s[-1]        
        for j in range(len(s)-2,-1,-1):
            if ord(s[j]) < ord(ret[0]):
                pass
            elif ord(s[j]) > ord(ret[0]):
                ret = s[j:]
            else:
                update = False
                for i in range(1,len(ret)):
                    if ord(s[j+i]) > ord(ret[i]):
                        ret = s[j:]
                        update = True
                        break
                    elif ord(s[j+i]) < ord(ret[i]):
                        update = True
                        break
                if not update:
                    ret = s[j:]
        return ret

    def lastSubstring_timeout2(self, s: str) -> str:
        '''
        Time-out.
        '''
        p_ret = len(s) - 1
        for j in range(len(s)-2,-1,-1):
            if ord(s[j]) < ord(s[p_ret]):
                pass
            elif ord(s[j]) > ord(s[p_ret]):
                p_ret = j
            else:
                update = False
                for i in range(1,len(s)-p_ret):
                    print(p_ret,i,len(s))
                    if ord(s[j+i]) > ord(s[p_ret+i]):
                        p_ret = j
                        update = True
                        break
                    elif ord(s[j+i]) < ord(s[p_ret+i]):
                        update = True
                        break
                if not update:
                    p_ret = j
        return s[p_ret:]

    def lastSubstring(self, s: str) -> str:
        '''
        official solution.
        '''
        i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1
        return s[i:]

    
if __name__ == '__main__':

    sln  = Solution()                
    
    s = "abab"
    print(sln.lastSubstring(s))         
    
    s = "leetcode"
    print(sln.lastSubstring(s))         