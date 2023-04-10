# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:22:17 2022

@author: Dell
"""
import time
from typing import List
from collections import deque
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        # Construct the adjacency list
        adjList = dict()
        for edge in connections:
            if edge[0] in adjList:
                adjList[edge[0]].append(edge[1])
            else:
                adjList[edge[0]] = [edge[1]]

            if edge[1] in adjList:
                adjList[edge[1]].append(edge[0])
            else:
                adjList[edge[1]] = [edge[0]]
        # n_nodes = len(adjList)
        n_edges = len(connections)
        
        # print(adjList)
        
        if n_edges < n-1:
            return -1
        
        # Count the number of islands
        visited = set()
        n_islands = 0
        for k in range(n):
            if k not in visited:
                q = deque()
                q.append(k)
                visited.add(k)
                if k in adjList:
                    while len(q)>0:
                        m = q.pop()
                        # print(k,m,adjList[m])
                        for j,adjnode in enumerate(adjList[m]):
                            if adjnode not in visited:
                                q.append(adjnode)
                                visited.add(adjnode)
                n_islands += 1
        
        return n_islands-1
    
if __name__ == '__main__':
    
    sln = Solution()
    
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    print(sln.makeConnected(n,connections))
        
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    print(sln.makeConnected(n,connections))
    
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    print(sln.makeConnected(n,connections))
    
    n = 5
    connections = [[0,1],[0,2],[3,4],[2,3]]
    print(sln.makeConnected(n,connections))