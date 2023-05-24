# -*- coding: utf-8 -*-
"""
Created on Wed May 24 08:22:22 2023

@author: chenxy

1377. Frog Position After T Seconds
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 

Example 2:
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
 

Constraints:

1 <= n <= 100
edges.length == n - 1
edges[i].length == 2
1 <= ai, bi <= n
1 <= t <= 50
1 <= target <= n

"""
import time
import random
from typing import List, Optional	
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
import bisect
import sys
from utils.BinaryTree import TreeNode, binTree2Lst, lst2bintree
from functools import reduce

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # 1. 建图
        g = [[] for _ in range(n + 1)]
        g[1].append(0)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 2. DFS 递归
        #      参数：（当前节点，当前节点父节点，当前概率，当前秒数）
        ans = 0
        def dfs(x: int, fa: int, p: float, cnt: int):
            if cnt > t: return 
            if x == target:
                nonlocal ans
                ans = p if cnt == t or len(g[x]) == 1 else 0
            for y in g[x]:
                if y != fa:
                    dfs(y, x, p * (1 / (len(g[x]) - 1)), cnt + 1)
        # 递归入口
        dfs(1, 0, 1, 0)
        return ans
        
if __name__ == '__main__':

    sln  = Solution()            
    
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 2
    target = 4
    print(sln.frogPosition(n,edges,t,target))   
    
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 1
    target = 7
    print(sln.frogPosition(n,edges,t,target))   