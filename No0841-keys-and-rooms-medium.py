# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:08:24 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q = deque([0])
        visited = set([0])
        
        while len(q) > 0:
            node = q.popleft()
            for neighbour in rooms[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
            
        return len(visited) == len(rooms)
        
if __name__ == '__main__':
    
    sln = Solution()
    
    rooms = [[1],[2],[3],[]]
    print(sln.canVisitAllRooms(rooms))
    
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(sln.canVisitAllRooms(rooms))