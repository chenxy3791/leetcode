# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:45:45 2023

@author: Dell

20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.

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
    def isValid1(self, s: str) -> bool:
        q = deque()
        for k in range(len(s)):
            c = s[k]
            # print(c)
            if c in ['(','{','[']:
                q.append(c)
            else:
                if len(q) == 0:
                    return False
                d = q.pop()
                if c == ')':
                    if d != '(':
                        return False
                elif c == '}':
                    if d != '{':
                        return False
                else:
                    if d != '[':
                        return False
        return len(q) == 0

    def isValid2(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: 
                stack.append(c)
            elif dic[stack.pop()] != c: 
                return False 
        return len(stack) == 1


if __name__ == '__main__':

    sln  = Solution()                
    
    s = "()"
    print(sln.isValid(s))        
    
    s = "()[]{}"
    print(sln.isValid(s)) 
    
    s = "(]"
    print(sln.isValid(s)) 
