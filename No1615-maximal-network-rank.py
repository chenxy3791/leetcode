# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 08:31:34 2023

@author: chenxy
1615. 最大网络秩
n 座城市和一些连接这些城市的道路 roads 共同组成一个基础设施网络。每个 roads[i] = [ai, bi] 都表示在城市 ai 和 bi 之间有一条双向道路。

两座不同城市构成的 城市对 的 网络秩 定义为：与这两座城市 直接 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 一次 。

整个基础设施网络的 最大网络秩 是所有不同城市对中的 最大网络秩 。

给你整数 n 和数组 roads，返回整个基础设施网络的 最大网络秩 。

示例 1：
输入：n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
输出：4
解释：城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。

示例 2：
输入：n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
输出：5
解释：共有 5 条道路与城市 1 或 2 相连。
示例 3：

输入：n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
输出：5
解释：2 和 5 的网络秩为 5，注意并非所有的城市都需要连接起来。
 

提示：

2 <= n <= 100
0 <= roads.length <= n * (n - 1) / 2
roads[i].length == 2
0 <= ai, bi <= n-1
ai != bi
每对城市之间 最多只有一条 道路相连

执行用时：64 ms, 在所有 Python3 提交中击败了85.21%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了60.56%的用户

"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        def isConnected(i,j,neighbors):
            return (i in neighbors[j]) or (j in neighbors[i])
        
        cityRank = n * [0]
        neighbors = defaultdict(list)
        for i in range(len(roads)):
            cityRank[roads[i][0]] = cityRank[roads[i][0]] + 1
            cityRank[roads[i][1]] = cityRank[roads[i][1]] + 1
            neighbors[roads[i][0]].append(roads[i][1])
            neighbors[roads[i][1]].append(roads[i][0])
        
        idx1 = []
        idx2 = []
        max1 = max2 = 0
        for i in range(n):
            if cityRank[i] > max1:
                max2 = max1
                idx2 = idx1.copy()
                max1 = cityRank[i]
                idx1 = [i]
            elif cityRank[i] == max1:
                idx1.append(i)
            else:
                if cityRank[i] > max2:
                    max2 = cityRank[i]                    
                    idx2 = [i]
                elif cityRank[i] == max2:
                    idx2.append(i)

        # print(cityRank)
        # print(idx1,max1,idx2,max2)        

        if len(idx1) > 1:
            # print("case1: There two or more cities having the max city rank")
            # Check whether there are unconnected pairs
            unconnected = False
            for i in range(len(idx1)):
                for j in range(i+1,len(idx1)):
                    if not isConnected(idx1[i],idx1[j], neighbors):
                        unconnected = True
                        break
            return 2 * max1 - (0 if unconnected else 1)
        elif len(idx2) > 1:
            # print("case2: There two or more cities having the second to max city rank")
            unconnected = False            
            for j in range(len(idx2)):
                if not isConnected(idx1[0],idx2[j], neighbors):
                    unconnected = True
                    break
            return max1 + max2 - (0 if unconnected else 1)
        else: #len(idx1)==1 and len(idx2)==1:
            # print("case3: Only one max and one second-to-max")
            unconnected = not isConnected(idx1[0], idx2[0], neighbors)
            return max1 + max2 - (0 if unconnected else 1)
                    
if __name__ == '__main__':

    sln  = Solution()                
    
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]    
    print(sln.maximalNetworkRank(n,roads))
    
    n = 5
    roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]    
    print(sln.maximalNetworkRank(n,roads))
    
    n = 8
    roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    print(sln.maximalNetworkRank(n,roads))