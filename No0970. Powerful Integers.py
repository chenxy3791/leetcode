# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:30:13 2023

@author: chenxy

970. Powerful Integers
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as x**i + y**j for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
 
Constraints:

1 <= x, y <= 100
0 <= bound <= 10**6
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
    # def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    #     x,y = (x,y) if x<=y else (y,x)
    #     i,j = 0,0
    #     x_pow = 1
    #     ret = set()
    #     while True:
    #         if x_pow > bound:
    #             break
    #         y_pow = 1
    #         while True:
    #             tmp = x_pow + y_pow
    #             if tmp > bound:
    #                 break
    #             ret.add(tmp)
    #             y_pow *= y
            
    #         x_pow *= x
            
    #     return list(ret)

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xpowLst = []
        if x == 1:
            xpowLst.append(1)
        else:
            xpow = 1
            while xpow < bound:
                xpowLst.append(xpow)
                xpow = xpow * x

        ypowLst = []
        if y == 1:
            ypowLst.append(1)
        else:
            ypow = 1
            while ypow < bound:
                ypowLst.append(ypow)
                ypow = ypow * y

        #print('xpowLst = {0}, ypowLst = {1}'.format(xpowLst, ypowLst))

        sumLst = []
        for i in range(len(xpowLst)):
            for j in range(len(ypowLst)):
                if xpowLst[i] + ypowLst[j] <= bound:
                    sumLst.append(xpowLst[i] + ypowLst[j])
                else:
                    break
        
        # Remove repetition
        if len(sumLst) == 0:
            return []

        sumLst.sort()

        #print('sumLst = ', sumLst)
        sumLst2 = [sumLst[0]]
        for i in range(1,len(sumLst)):
            if sumLst[i] != sumLst2[-1]:
                sumLst2.append(sumLst[i])

        return sumLst2        

        
if __name__ == '__main__':

    sln  = Solution()                
    
    x = 2; y = 3; bound = 10
    print(sln.powerfulIntegers(x,y,bound))             
    
    x = 3; y = 5; bound = 15
    print(sln.powerfulIntegers(x,y,bound))             
    