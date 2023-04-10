# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:51:48 2022

@author: Dell
"""

import time
from typing import List
from collections import deque

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        # construct adjacency list
        adjlist = [[] for k in range(n)]
        for road in roads:
            adjlist[road[0]].append(road[1])
            adjlist[road[1]].append(road[0])
        
        # Search for the nodes with the max degree and the second-to-max degree
        maxdeg = -1
        maxlist= []
        secdeg = -1
        seclist= []
        for k in range(n):
            d = len(adjlist[k])
            if d > maxdeg:
                secdeg  = maxdeg
                seclist = maxlist
                maxlist = [k]
                maxdeg  = d
            elif d == maxdeg:
                maxlist.append(k)
            elif len(maxlist)==1:
                if d > secdeg:
                    seclist = [k]
                    secdeg  = d
                elif d == secdeg:
                    seclist.append(k)
        # print(adjlist)
        # print(maxlist,maxdeg, seclist,secdeg)
        # Calculate the max rank
        if len(maxlist)>1:
            for k in maxlist:
                for j in maxlist:
                    # print(k,j)
                    if k!=j and (j not in adjlist[k]):
                        return 2*maxdeg
            return 2*maxdeg-1
        else:
            for k in maxlist:
                for j in seclist:
                    if j not in adjlist[k]:
                        return maxdeg+secdeg
            return maxdeg+secdeg-1
        
if __name__ == "__main__":
    
    sln = Solution()
    
    n = 2
    roads = [[0,1]]           
    print(sln.maximalNetworkRank(n, roads))
    
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]           
    print(sln.maximalNetworkRank(n, roads))
                
    n = 5
    roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    print(sln.maximalNetworkRank(n, roads))
    
    n = 8
    roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    print(sln.maximalNetworkRank(n, roads))