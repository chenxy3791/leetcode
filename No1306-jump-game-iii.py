# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:04:18 2022

@author: Dell
"""
from typing import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        q = deque([start])
        visited = set([start])
        while len(q) > 0:
            node = q.pop()
            if arr[node] == 0:
                return True
            left = node - arr[node]
            if left >= 0 and left not in visited:
                q.append(left)
                visited.add(left)
            
            right = node + arr[node]
            if right < len(arr) and right not in visited:
                q.append(right)
                visited.add(right)

        return False
    
if __name__ == "__main__":
    
    sln = Solution()
    
    arr = [4,2,3,0,3,1,2]
    start = 5
    print(sln.canReach(arr, start))
    
    arr = [4,2,3,0,3,1,2]
    start = 0
    print(sln.canReach(arr, start))
    
    arr = [3,0,2,1,2]
    start = 2
    print(sln.canReach(arr, start))
    
    arr = [0,1]
    start = 1
    print(sln.canReach(arr, start))