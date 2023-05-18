# -*- coding: utf-8 -*-
"""
Created on Thu May 18 08:04:28 2023

@author: chenxy

1073. Adding Two Negabinary Numbers
Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  
For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  
A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.

Example 2:

Input: arr1 = [0], arr2 = [0]
Output: [0]

Example 3:

Input: arr1 = [0], arr2 = [1]
Output: [1]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
arr1[i] and arr2[i] are 0 or 1
arr1 and arr2 have no leading zeros
"""
import time
import random
import time
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right        

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def arr2num(arr):
            num = 0
            weight = 1
            N   = len(arr)
            for k in range(len(arr)):
                num += arr[N-1-k] * weight
                weight *= -2
            return num
                
        def num2arr(num:int) -> List[int]:
            if num == 0:
                return [0]
            evenodd = 1
            arr  = []
            while num != 0:
                cur = (num % 2)
                arr.insert(0, cur)
                # print(cur,arr)
                num -= cur * evenodd                
                num = num // 2
                evenodd *= -1
            return arr

        return num2arr(arr2num(arr1) + arr2num(arr2))
        
        # num1 = arr2num(arr1)
        # num2 = arr2num(arr2)
        # num  = num1 + num2
        # arr  = num2arr(num)
        # print(num1,num2,num,arr)
        # return arr

if __name__ == '__main__':

    sln  = Solution()                
    
    arr1 = [1,1,1,1,1]; arr2 = [1,0,1]
    print(sln.addNegabinary(arr1,arr2))     
    
    arr1 = [0]; arr2 = [0]
    print(sln.addNegabinary(arr1,arr2))     
    
    arr1 = [0]; arr2 = [1]
    print(sln.addNegabinary(arr1,arr2))     
    