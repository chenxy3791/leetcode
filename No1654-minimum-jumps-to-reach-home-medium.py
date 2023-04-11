# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:49:38 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # Assumption: 0:forward jump, 1: backward jump
        pos_max = max(max(forbidden)+a+b, x)
        forbidden_s = set(forbidden)
        q = deque([(-1,0,0)]) # (prev_operation,position,layer)
        forbidden_s.add(0)
        while len(q) > 0:
            op,pos,layer = q.popleft()
            # print(op,pos,layer)
            
            if pos == x:
                return layer
            newpos = pos+a
            if newpos not in forbidden_s and newpos <= pos_max:
                q.append((0,newpos,layer+1))
                forbidden_s.add(newpos)
            newpos = pos-b
            if op!=1 and newpos>=0 and newpos not in forbidden_s:
                q.append((1,newpos,layer+1))
                # forbidden_s.add(newpos)
            
        return -1
    
if __name__ == "__main__":
    
    sln = Solution()
    
    forbidden = [14,4,18,1,15]
    a = 3
    b = 15
    x = 9
    print(sln.minimumJumps(forbidden, a, b, x))
    
    forbidden = [8,3,16,6,12,20]
    a = 15
    b = 13
    x = 11
    print(sln.minimumJumps(forbidden, a, b, x))
    
    forbidden = [1,6,2,14,5,17,4]
    a = 16
    b = 9
    x = 7
    print(sln.minimumJumps(forbidden, a, b, x))
    
    forbidden = [128,178,147,165,63,11,150,20,158,144,136]
    a = 61
    b = 170
    x = 135
    print(sln.minimumJumps(forbidden, a, b, x))
    
    forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
    a = 29
    b = 98
    x = 80
    print(sln.minimumJumps(forbidden, a, b, x))
    
    forbidden = [3]
    a = 14
    b = 5
    x = 90
