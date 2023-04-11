# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 04:48:52 2022

@author: Dell
"""
import time
from typing import List

class Solution:
    def canReorderDoubled1(self, arr: List[int]) -> bool:
        if len(arr)%2 != 0:
            return False
        # First, sorting the input array
        arr.sort()
        # Brute-force search
        while len(arr) > 0:
            num = arr.pop(0)
            pairFound = False
            if num >= 0:
                for j in range(0,len(arr)):
                    if arr[j] == 2*num:
                        arr.pop(j)
                        pairFound = True
                        break
                if not pairFound:
                    return False
            else:
                for j in range(0,len(arr)):
                    if 2*arr[j] == num:
                        arr.pop(j)
                        pairFound = True
                        break
                if not pairFound:
                    return False                
        return True
    
    def canReorderDoubled2(self, arr: List[int]) -> bool:
        if len(arr)%2 != 0:
            return False
        # First, sorting the input array
        arr.sort()
        # Brute-force search
        flaged = len(arr) * [False]
        nextStart = 0
        for k in range(len(arr)):
            if flaged[k]:
                continue
            num = arr[k]
            pairFound = False
            if num >= 0:
                for j in range(nextStart,min(len(arr),len(arr)//2+k+1)):
                    if arr[j] == 2*num:
                        nextStart = j+1
                        pairFound = True
                        flaged[j] = True
                        break
                if not pairFound:
                    return False
            else:
                for j in range(nextStart,min(len(arr),len(arr)//2+k+1)):
                    if 2*arr[j] == num:
                        nextStart = j+1
                        pairFound = True
                        flaged[j] = True
                        break
                if not pairFound:
                    return False                
        return True      
        
if __name__ == '__main__':
    
    sln = Solution()

    arr = []
    print(sln.canReorderDoubled1(arr))
    print(sln.canReorderDoubled2(arr))
    
    arr = [3,1,3,6]
    print(sln.canReorderDoubled1(arr))
    print(sln.canReorderDoubled2(arr))

    arr = [2,1,2,6]    
    print(sln.canReorderDoubled1(arr))
    print(sln.canReorderDoubled2(arr))

    arr = [4,-2,2,-4]            
    print(sln.canReorderDoubled1(arr))
    print(sln.canReorderDoubled2(arr))

    with open('No0954-testpattern.py','r') as f:
        exec(f.read())      
    tstart=time.time()    
    print(sln.canReorderDoubled1(arr))
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))      
    
    tstart=time.time()    
    print(sln.canReorderDoubled2(arr))
    tstop=time.time()
    print('tcost = {0:5.3f}(sec)'.format(tstop-tstart))       