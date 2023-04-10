# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 07:34:05 2022

@author: Dell
"""
from typing import List
from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def diff_is_one(s1,s2)->bool:
            cnt=0
            for k in range(len(s1)):
                if s1[k]!=s2[k]:
                    cnt+=1
            return cnt==1
        if end not in bank:
            return -1
        if start not in bank:
            bank.insert(0, start)
        for k in range(len(bank)):
            if bank[k]==end:
                end_idx=k
        adjlist = [ [] for k in range(len(bank)) ]
        for k in range(len(bank)):
            for j in range(k,len(bank)):
                if diff_is_one(bank[k], bank[j]):
                    adjlist[k].append(j)
                    adjlist[j].append(k)
        # print(bank,adjlist)
        q = deque([(0,0)])
        visited = set([0])
        while len(q)>0:
            node,layer = q.popleft()
            if node == end_idx:
                return layer
            for nxt in adjlist[node]:
                if nxt not in visited:
                    q.append((nxt,layer+1))
                    visited.add(nxt)
        return -1
    
if __name__ == "__main__":
    
    sln = Solution()
    
    start= "AACCGGTT"
    end=   "AACCGGTA"
    bank= ["AACCGGTA"]
    print(sln.minMutation(start, end, bank))
        
    start= "AACCGGTT"
    end=   "AAACGGTA"
    bank= ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(sln.minMutation(start, end, bank))
    
    start= "AAAAACCC"
    end=   "AACCCCCC"
    bank= ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(sln.minMutation(start, end, bank))
    
    start= "AACCGGTT"
    end=   "AACCGGTA"
    bank=  []
    print(sln.minMutation(start, end, bank))
    
    start= "AACCGGTT"
    end=   "AACCGGTA"
    bank=  ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(sln.minMutation(start, end, bank))