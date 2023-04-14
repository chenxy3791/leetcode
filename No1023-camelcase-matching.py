# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 07:50:56 2023

@author: chenxy
1023. Camelcase Matching

Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters into pattern so that it equals the query. You may insert each character at any position and you may not insert any characters.
 
Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Constraints:

1 <= pattern.length, queries.length <= 100
1 <= queries[i].length <= 100
queries[i] and pattern consist of English letters.
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
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:        
        '''
        执行用时：60 ms, 在所有 Python3 提交中击败了7.06%的用户
        内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.41%的用户
        '''
        def match(query, pattern):
            qPtr = 0
            for c in pattern:
                while 1:
                    if c == query[qPtr]:                    
                        qPtr += 1
                        break
                    else:
                        if query[qPtr].isupper():
                            return False
                        else:
                            qPtr += 1
                    if qPtr == len(query):
                        return False
            
            for k in range(qPtr,len(query)):
                if query[k].isupper():
                        return False
            return True
        
        ret = []
        for q in queries:
            ret.append(match(q,pattern))            
        
        return ret

if __name__ == '__main__':

    sln  = Solution()                
    
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]; pattern = "FB"
    print(sln.camelMatch(queries,pattern))           
    
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]; pattern = "FoBa"
    print(sln.camelMatch(queries,pattern))               
    
    Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]; pattern = "FoBaT"
    print(sln.camelMatch(queries,pattern))               