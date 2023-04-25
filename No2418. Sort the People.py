# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 07:53:17 2023

@author: chenxy

2418. Sort the People
You are given an array of strings names, and an array heights that consists of distinct positive integers. 
Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.


Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

Constraints:

n == names.length == heights.length
1 <= n <= 10**3
1 <= names[i].length <= 20
1 <= heights[i] <= 10**5
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
from bisect import bisect, bisect_left, bisect_right

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        d = dict()
        for k,h in enumerate(heights):
            d[heights[k]] = names[k]
        heights.sort(reverse=True)
        ret = []
        for k in range(len(heights)):
            ret.append(d[heights[k]])
        
        return ret

if __name__ == '__main__':

    sln  = Solution()                
    
    names = ["Mary","John","Emma"]; heights = [180,165,170]
    print(sln.sortPeople(names,heights))           
    
    names = ["Alice","Bob","Bob"]; heights = [155,185,150]
    print(sln.sortPeople(names,heights))           
    
    