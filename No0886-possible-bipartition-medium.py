# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:29:20 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

# class Solution:
#     def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
#         adjlist = [set() for k in range(n+1)] # index 0 is not used
#         for edge in dislikes:
#             adjlist[edge[0]].add(edge[1])
#             adjlist[edge[1]].add(edge[0])
        
        
#         visited = (n+1)*[0] # index 0 is not used
        
#         cnt = 0
#         for k in range(1,n+1):
#             if visited[k] == 0:
#                 q = deque([k])
#                 visited[k] = 1
#                 while len(q)>0:
#                     node = q.pop()
#                     for m in range(1,n+1):
#                         if m!=node and (m not in adjlist[node]) and visited[m]==0:
#                             q.append(m)
#                             visited[m] = 1
#                 cnt = cnt + 1
#         print(cnt)
#         return cnt <= 2
    
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1:
            return True
        # construct adjacency list
        adjlist = [[] for k in range(n+1)]
        for dislike in dislikes:
            adjlist[dislike[0]].append(dislike[1])
            adjlist[dislike[1]].append(dislike[0])
            
        color = (n+1) * [-1]
        for k in range(1,n+1):
            if color[k] < 0:
                q = deque([k])
                color[k] = 0
                while len(q)>0:
                    node = q.pop()
                    for adj in adjlist[node]:
                        if color[adj] < 0:
                            color[adj] = 1 - color[node]
                            q.append(adj)
                        else:
                            if color[adj] == color[node]:
                                return False
        return True
                    
if __name__ == "__main__":
    
    sln = Solution()
    
    n = 4
    dislikes = [[1,2],[1,3],[2,4]]
    print(sln.possibleBipartition(n, dislikes))
    
    n = 3
    dislikes = [[1,2],[1,3],[2,3]]
    print(sln.possibleBipartition(n, dislikes))
    
    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(sln.possibleBipartition(n, dislikes))