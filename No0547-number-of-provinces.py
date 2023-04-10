# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:52:08 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

class Solution:

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
          
    def findCircleNum_dfsbfs(self, isConnected: List[List[int]]) -> int:
        if len(isConnected)==0:
            return 0
        
        N         = len(isConnected)
        islandCnt = 0
        q         = deque()
        visited   = set()
        for node in range(N):
            # print(node, visited)
            # find the next unvisited node
            if node not in visited:
                # print("Start node of the next island: ", node)
                # Start from this node to search the connected sub-graph
                q.append(node)
                visited.add(node)
                while len(q) > 0:
                    tmp = q.pop()
                    for k in range(N):
                        if isConnected[tmp][k]==1 and k not in visited:
                            q.append(k)
                            visited.add(k)
                islandCnt += 1
                
        return islandCnt        
    
if __name__ == '__main__':
    
    sln = Solution()
    
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(sln.findCircleNum_union_find(isConnected))
    
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    print(sln.findCircleNum_union_find(isConnected))