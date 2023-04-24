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

    def lastSubstring(self, s: str) -> str:
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
    
if __name__ == '__main__':

    sln  = Solution()                
    
    s = "abab"
    print(sln.lastSubstring(s))         
    
    s = "leetcode"
    print(sln.lastSubstring(s))         