# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 17:56:44 2021

@author: chenxy
"""
import sys
import time
import datetime
import math
import random
from   typing import List
# from   queue import Queue
from   collections import deque
import itertools as it
from   math import sqrt, floor, ceil
import numpy 

class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1,int(vertex.value**.5)+1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i==0:                   
                    return new_vertex.step
                    
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
                                        
        return -1

if __name__ == '__main__':        
    
    sln = Solution()
    
    # for n in range(10,4999,117):
    # for n in range(1000,1001):

    n = 4696
    # tStart = time.time()
    # nums = sln.numSquares_recursion(n)
    # tCost = time.time() - tStart
    # print('numSquares_recursion({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))

    tStart = time.time()
    nums = sln.numSquares(n)
    tCost = time.time() - tStart
    print('numSquares({0}) = {1}, tCost = {2}(sec)'.format(n,nums,tCost))