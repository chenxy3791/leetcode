# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 10:52:45 2023

@author: chenxy

1042. Flower Planting With No Adjacent
You have n gardens, labeled from 1 to n, and an array paths where,
paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. 
In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

 

Example 1:
Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

Example 2:
Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:
Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 
Constraints:
1 <= n <= 10**4
0 <= paths.length <= 2 * 10**4
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
Every garden has at most 3 paths coming into or leaving it.
"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it
import bisect
class Solution:
    # def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
    #     # Adj list creation
    #     adjLst = defaultdict(List)
    #     for path in paths:
    #         adjLst[path[0]].append(path[1])
    #         adjLst[path[1]].append(path[0])
            
    #     # Initialization        
    #     s = deque()
    #     s.append((0,0,0,0))
    #     visited = {(0,0,0):0}
        
    #     while len(s) > 0:
    #         garden, flower, parent, layer = s.pop()
            
    #         if layer == n:
    #             # Traverse back to recover the feasible flower list and return
                
    #             return 
            
    #         for g in adjLst[garden]:
    #             for f in [1,2,3,4]:
    #                 if f == flower:
    #                     continue
    #                 if (g,f) not in visited:
    #                     s.append()
    #                     visited.add()
            
    #     assert(0) # Should not come here, because the feasible solution is assured to exist.
        
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # 贪心法: 对于当前的某一个花园，剔除掉与它邻接花园的花的种类，从剩下的种类中选一种即可。
        # 1. 构建邻接矩阵G; 2. 用res列表保存当前花园花的种类
        res = [0]*n
        G = [[] for _ in range(n)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(n):
            # 对于当前花园, 排除掉邻接的花园的花种类就ok了，然后pop出一种
            res[i] = ({1,2,3,4} - {res[j] for j in G[i]}).pop()
        return res
    
if __name__ == '__main__':

    sln  = Solution()                
    
    # n = 3
    # paths = [[1,2],[2,3],[3,1]]
    # print(sln.gardenNoAdj(n,paths))    
    
    # n = 4
    # paths = [[1,2],[3,4]]
    # print(sln.gardenNoAdj(n,paths))    
    
    n = 4
    paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    print(sln.gardenNoAdj(n,paths))    