# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 06:54:03 2022

@author: Dell
"""
import time
from typing import List
from collections import deque
# # Incorrect implementation
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         paths = []
#         N     = len(graph)
#         print(N, graph)
#         def dfs(path):
#             nonlocal paths 
#             nonlocal N
#             nonlocal graph
#             print('dfs(): ', path, graph)
#             # Traverse all neighbor nodes of the last node except those already in path
#             for node in graph[path[-1]]:
#                 print('dfs(): ', path, graph[path[-1]], node)
#                 if node == N-1:
#                     # One path found
#                     paths.append(path.append(node))
#                 else:
#                     if node not in path:
#                         dfs(path.append(node))
#         dfs([0])
#         return paths


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        N     = len(graph)
        print(N, graph)
        def dfs(path):
            nonlocal paths 
            nonlocal N
            nonlocal graph
            # print('dfs(): ', path, graph)
            # Traverse all neighbor nodes of the last node except those already in path
            for node in graph[path[-1]]:
                if node == N-1:
                    # One path found
                    paths.append(path+[node])
                else:
                    if node not in path:
                        dfs(path+[node])
        dfs([0])
        return paths
                    
if __name__ == '__main__':
    sln = Solution()
    
    graph = [[1,2],[3],[3],[]]               
    print(sln.allPathsSourceTarget(graph))     
    
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(sln.allPathsSourceTarget(graph))
                