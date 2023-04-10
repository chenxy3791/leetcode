# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:19:02 2022

@author: Dell
"""
import time
from typing import List
from collections import deque
# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         def bfs(start):
#             q       = deque([[start]])
#             # visited = set([0])
#             while True:
#                 path = q.popleft()
#                 # print("path = {0}", path)
#                 if len(set(path))==len(graph):
#                     return len(path)-1
#                 for neighbor in graph[path[-1]]:
#                     q.append(path + [neighbor])
            
#         minpath = bfs(0)
#         for k in range(1,len(graph)):
#             pathlen = bfs(k)
#             # print(k,pathlen)
#             minpath = pathlen if pathlen < minpath else minpath
#         return minpath

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n))
        seen = {(i, 1 << i) for i in range(n)}
        ans = 0
        
        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            # 搜索相邻的节点
            for v in graph[u]:
                # 将 mask 的第 v 位置为 1
                mask_v = mask | (1 << v)
                if (v, mask_v) not in seen:
                    q.append((v, mask_v, dist + 1))
                    seen.add((v, mask_v))
        
        return ans

if __name__ == "__main__":

    sln = Solution()
    
    graph = [[1,2,3],[0],[0],[0]]
    print(sln.shortestPathLength(graph))
    
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    print(sln.shortestPathLength(graph))
    
    graph = [[1,4],[0,3,4,7,9],[6,10],[1,10],[1,0],[6],[7,2,5],[6,1,8],[7],[1],[2,3]]
    tstart = time.time()
    ans = sln.shortestPathLength(graph)
    tstop  = time.time()
    print('ans={0}, tcost={1:4.2f}'.format(ans,tstop-tstart))