# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:29:06 2023

@author: chenxy

547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

"""
import os
import time
import random
import time
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Reachability problem
        (1) number of islands, i.e, number of connected sub-graphs
        (2) For each connected sub-graph, using either BFS or DFS is OK, because we should travers all reachable neighbour cities.
        '''
        visited = set()
        cnt     = 0
        q       = deque() # using queue instead of stack for BFS
        
        for city in range(len(isConnected)):
            if city not in visited:
                cnt += 1
                q.append(city)
                visited.add(city)
                while len(q) > 0:
                    cur = q.popleft()
                    for neighb,flag in enumerate(isConnected[cur]):
                        if neighb not in visited and flag == 1:
                            visited.add(neighb)
                            q.append(neighb)
        return cnt

    def findCircleNum_union_find(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            # Find the group to which the index belongs
            if groupID[index] != index:
                groupID[index] = find(groupID[index])
            return groupID[index]
        
        def union(index1: int, index2: int):
            # Join index1 into the group which index2 belongs to
            groupID[find(index1)] = find(index2)
        
        # Initialization.
        # Start from the state in which each province belongs to the own-group
        # Each group has one province with the same index as its initial root.
        groupID      = list(range(len(isConnected)))
        
        # For each group, find the (directly or indirectly) connected province and
        # join itself into the later group
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        numGroup = sum(groupID[i] == i for i in range(len(isConnected)))
        return numGroup
                        
if __name__ == '__main__':

    sln  = Solution()                

    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(sln.findCircleNum(isConnected))    

    isConnected = [[1,0,0],[0,1,0],[0,0,1]]   
    print(sln.findCircleNum(isConnected))        