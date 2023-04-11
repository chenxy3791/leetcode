# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 08:07:36 2022

@author: Dell
"""
import time
from typing import List
from collections import deque
class Solution:
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = dict()
        for edge in edges:
            if edge[0] in d:
                d[edge[0]] += 1
            else:
                d[edge[0]]  = 1
                
            if edge[1] in d:
                d[edge[1]] += 1
            else:
                d[edge[1]]  = 1
        
        num_lefts = n
        q = deque()
        while num_lefts>2:
            for node in d:
                if d[node] == 1:
                    q.append(node)
                    num_lefts -= 1 # Remove one node equivalently
                    d[node]    = -1 # For distinguishing with the last one node whose degree will become 0
            # if len(q) <= 2:
            #     break
            while len(q) > 0:
                node = q.popleft()
                for edge in edges:
                    if edge[0] == node:
                        d[edge[1]] -= 1
                    if edge[1] == node:
                        d[edge[0]] -= 1
        ans = []
        for node in d:
            if d[node] == 1 or d[node] == 0:
                ans.append(node)
        return ans

    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        d = dict()
        for edge in edges:
            if edge[0] in d:
                d[edge[0]] += 1
            else:
                d[edge[0]]  = 1
                
            if edge[1] in d:
                d[edge[1]] += 1
            else:
                d[edge[1]]  = 1
        
        num_lefts = n
        q = deque()
        while num_lefts>2:
            nodes = list(d.keys())
            for node in nodes:
                if d[node] == 1:
                    q.append(node)
                    num_lefts -= 1 # Remove one node equivalently
                    d.pop(node)
            while len(q) > 0:
                node = q.popleft()
                for edge in edges:
                    if edge[0] == node and edge[1] in d:
                        d[edge[1]] -= 1
                    if edge[1] == node and edge[0] in d:
                        d[edge[0]] -= 1
        ans = []
        for node in d:
            if d[node] == 1 or d[node] == 0:
                ans.append(node)
        return ans

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        remainNodes = n
        while remainNodes > 2:
            remainNodes -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q

if __name__ == '__main__':
    
    sln = Solution()

    n = 1
    edges = []
    print(sln.findMinHeightTrees(n,edges))

    n = 3
    edges = [[0,1],[0,2]]
    print(sln.findMinHeightTrees(n,edges))

    n = 4
    edges = [[1,0],[1,2],[1,3]]
    print(sln.findMinHeightTrees(n,edges))
            
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print(sln.findMinHeightTrees(n,edges))    
        
    with open('No0310-testpattern.py','r') as f:
        exec(f.read())      
    tstart=time.time()    
    print(sln.findMinHeightTrees(n,edges))
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))       