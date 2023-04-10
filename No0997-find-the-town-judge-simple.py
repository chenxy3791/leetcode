# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:35:37 2022

@author: Dell
"""

import time
from typing import List
from collections import deque

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_deg = dict()
        non_judge = set()
        
        for [ai,bi] in trust:
            non_judge.add(ai)
            if ai in trust_deg:
                trust_deg.pop(ai)
            
            if bi not in non_judge:
                if bi in trust_deg:
                    trust_deg[bi] = trust_deg[bi] + 1
                else:
                    trust_deg[bi] = 1
        
        if len(trust_deg)==1:
            a = trust_deg.popitem()
            if a[1] == n - 1:
                return a[0]
        return -1
    
if __name__ == "__main__":
    
    sln = Solution()
    
    n = 2
    trust = [[1,2]]
    print(sln.findJudge(n, trust))
    
    n = 3
    trust = [[1,3],[2,3]]
    print(sln.findJudge(n, trust))
    
    n = 3
    trust = [[1,3],[2,3],[3,1]]
    print(sln.findJudge(n, trust))
            