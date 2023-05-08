# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:14:46 2023

@author: Dell

14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

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
from functools import reduce

class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        min_len = 200
        for k in range(len(strs)):
            min_len = min(min_len,len(strs[k]))
            
        if min_len == 0:
            return ""
        for k in range(min_len):
            # c = strs[0][k]
            for j in range(1,len(strs)):
                if strs[j][k] != strs[0][k]:
                    return strs[0][:k]
        return strs[0][:min_len]    

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        min_len = reduce(min,[len(strs[k]) for k in range(len(strs))])
            
        if min_len == 0:
            return ""
        for k in range(min_len):
            for j in range(1,len(strs)):
                if strs[j][k] != strs[0][k]:
                    return strs[0][:k]
        return strs[0][:min_len]   
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，
        举例abb， aba，abac，最大为abb，最小为aba。
        所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
        '''
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
    
if __name__ == '__main__':

    sln  = Solution()                
    
    strs = ["flower","flow","flight"]
    print(sln.longestCommonPrefix(strs))  
    
    strs = ["dog","racecar","car"]
    print(sln.longestCommonPrefix(strs))      
    
    strs = [""]
    print(sln.longestCommonPrefix(strs))
    
    strs = ["ab", "a"]
    print(sln.longestCommonPrefix(strs))