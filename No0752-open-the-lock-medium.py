# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:38:44 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends or '0000' in deadends:
            return -1
        deadset = set(deadends)
        q = deque([('0000',0)])
        while len(q)>0:
            node,layer = q.popleft()
            if node == target:
                return layer
            # print(node,layer)
            for k in range(4):
                for i in [1,-1]:
                    nxt = node[:k] + str((int(node[k])+i) % 10) + node[k+1:]
                    if nxt not in deadset:
                        q.append((nxt,layer+1))
                        deadset.add(nxt)
        return -1
    
if __name__ == "__main__":
    
    sln = Solution()
    
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(sln.openLock(deadends, target))
    
    deadends = ["8888"]
    target = "0009"
    print(sln.openLock(deadends, target))
    
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    print(sln.openLock(deadends, target))

