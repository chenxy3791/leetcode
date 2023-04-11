# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:24:26 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

class Solution:
    # def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
    #     adjlist = [[] for k in range(n)]
    #     for edge in connections:
    #         adjlist[edge[0]].append(edge[1])
    #         adjlist[edge[1]].append(edge[0])
        
    #     q = deque([0])
    #     visited = set([0])
    #     revcnt  = 0
    #     while len(q)>0:
    #         city = q.popleft()
    #         for nxt in adjlist[city]:
    #             if nxt not in visited:
    #                 q.append(nxt)
    #                 visited.add(nxt)
    #                 if [city, nxt] in connections:
    #                     # This edge should be reversed.
    #                     revcnt += 1
    #     return revcnt

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adjlist = [[] for k in range(n)]
        edge_set = set()
        for edge in connections:
            adjlist[edge[0]].append(edge[1])
            adjlist[edge[1]].append(edge[0])
            edge_set.add(tuple(edge))
        
        q = deque([0])
        visited = set([0])
        revcnt  = 0
        while len(q)>0:
            city = q.popleft()
            for nxt in adjlist[city]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
                    # if [city, nxt] in connections:
                    if (city,nxt) in edge_set:
                        # This edge should be reversed.
                        revcnt += 1
        return revcnt
    
if __name__ == "__main__":

    sln = Solution()

    n = 6 
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]    
    print(sln.minReorder(n, connections))
    
    n = 5
    connections = [[1,0],[1,2],[3,2],[3,4]]
    print(sln.minReorder(n, connections))
    
    n = 3
    connections = [[1,0],[2,0]]
    print(sln.minReorder(n, connections))