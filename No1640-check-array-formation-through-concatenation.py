# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:17:29 2022

@author: Dell
"""
from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for p in pieces:
            # print(p)
            k = 0
            while k<len(arr):
                if arr[k] == p[0]:
                    # Found p[0] in arr, then compare the rest
                    for j in range(1,len(p)):
                        if k+j>=len(arr) or arr[k+j] != p[j]:
                            return False
                    # The same segment is found for p.
                    break
                else:
                    k += 1
            # Didn't found p[0] in arr.
            if k == len(arr):
                return False
        return True

if __name__ == '__main__':
    
    sln = Solution()

    arr = [15]
    pieces = [[15]]
    print(sln.canFormArray(arr,pieces))
    
    arr = [15]
    pieces = [[25]]
    print(sln.canFormArray(arr,pieces))    
    
    arr = [15,88]
    pieces = [[88],[15]]
    print(sln.canFormArray(arr,pieces))
    
    arr = [49,18,16]
    pieces = [[16,18,49]]
    print(sln.canFormArray(arr,pieces))
                    
    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]    
    print(sln.canFormArray(arr,pieces))