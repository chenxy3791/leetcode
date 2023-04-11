# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 06:45:43 2022

@author: Dell
"""
from typing import List
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Assuming 0 for red, 1 for blue, None for neither 0 nor 1
        q       = deque([(None,0,0)])
        visited = set([None,0])
        dist    = n * [-1]
        while len(q)>0:
            inEdgeColor,node,layer = q.popleft()
            # if node not in dist:
            if dist[node] < 0:
                dist[node] = layer
            if inEdgeColor != 0:
                for edge in redEdges:
                    if node==edge[0]:
                        if (0,edge[1]) not in visited:
                            q.append((0,edge[1],layer+1))
                            visited.add((0,edge[1]))
                            
            if inEdgeColor != 1:
                for edge in blueEdges:
                    if node==edge[0]:
                        if (1,edge[1]) not in visited:
                            q.append((1,edge[1],layer+1))
                            visited.add((1,edge[1]))               

        return dist

if __name__ == "__main__":
    import time
    sln = Solution()
    
    n = 3
    red_edges = [[0,1],[1,2]]
    blue_edges = []
    print(sln.shortestAlternatingPaths(n, red_edges, blue_edges))
    
    n = 3
    red_edges = [[0,1]]
    blue_edges = [[2,1]]
    print(sln.shortestAlternatingPaths(n, red_edges, blue_edges))
    
    n = 3
    red_edges = [[1,0]]
    blue_edges = [[2,1]]
    print(sln.shortestAlternatingPaths(n, red_edges, blue_edges))
    
    n = 3
    red_edges = [[0,1]]
    blue_edges = [[1,2]]
    print(sln.shortestAlternatingPaths(n, red_edges, blue_edges))
    
    n = 3
    red_edges = [[0,1],[0,2]]
    blue_edges = [[1,0]]
    print(sln.shortestAlternatingPaths(n, red_edges, blue_edges))
    
    n = 5
    red_edges = [[0,1],[3,2],[1,0],[4,3],[2,4]]
    blue_edges = [[2,4],[2,2],[1,3]]
    print(sln.shortestAlternatingPaths(n, red_edges, blue_edges))