# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:41:27 2023

@author: chenxy

1003. Check If Word Is Valid After Substitutions
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.

Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.

Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
 

Constraints:

1 <= s.length <= 2 * 10**4
s consists of letters 'a', 'b', and 'c'
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
    def isValid(self, s: str) -> bool:
        '''
        执行用时：92 ms, 在所有 Python3 提交中击败了16.81%的用户
        内存消耗：16.4 MB, 在所有 Python3 提交中击败了5.31%的用户
        '''
        stk = []
        for c in s:
            stk.append(c)
            if ''.join(stk[-3:]) == "abc":
                stk[-3:] = []
        return len(stk) == 0
    
    def isValid_replace(self, s: str) -> bool:
        '''
        执行用时：36 ms, 在所有 Python3 提交中击败了92.04%的用户
        内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.31%的用户
        '''
        while s != '' and 'abc' in s:
        # while 'abc' in s: # Also OK, but slower
            s = s.replace('abc','')
        return s == ''
    
    def isValid_stack(self, s: str) -> bool:
        '''
        执行用时：100 ms, 在所有 Python3 提交中击败了13.27%的用户
        内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.31%的用户
        '''
        
        stk = deque()
        
        for char in s:
            if char == 'c' and len(stk) > 1: 
                if stk[-1] == 'b' and stk[-2] == 'a':
                    stk.pop()
                    stk.pop()
                else:
                    stk.append(char)
            else:
                stk.append(char)
            # print(stk)
        return len(stk) == 0
        
    def isValid_fsm(self, s: str) -> bool:
        '''
        执行用时：168 ms, 在所有 Python3 提交中击败了5.31%的用户
        内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.31%的用户
        '''
        flag = len(s) * [0]
        flag_cnt = 0
        
        def removeABC():            
            nonlocal flag_cnt, flag, s
            k,state = 0,0

            while k < len(s):
                if state == 0:
                    if flag[k] == 0 and s[k] == 'a':
                        state = 1
                elif state == 1:
                    if flag[k] == 1:
                        state = 1
                    elif s[k] == 'a':
                        state = 1
                    elif s[k] == 'b':
                        state = 2
                    else:
                        state = 0
                elif state == 2:
                    if flag[k] == 1:
                        state = 2                       
                    elif s[k] == 'c':
                        #flag[k] = flag[k-1] = flag[k-2] = 1
                        flag[k] = 1
                        j = k-1
                        while True:
                            if flag[j] == 0 and s[j] == 'b':
                                flag[j] = 1
                                break
                            j -= 1
                        j -= 1
                        while True:
                            if flag[j] == 0 and s[j] == 'a':
                                flag[j] = 1
                                break
                            j -= 1
                            
                        flag_cnt = flag_cnt + 3
                        state = 0
                    elif s[k] == 'a':
                        state = 1
                    else:
                        state = 0                                            
                k += 1       
                # print('removeABC(): ' + f'k={k}, state={state}, flag={flag}')                                                     
        
        while len(s) > 0:
            cnt_prev = flag_cnt
            removeABC()
            print(flag,flag_cnt)
            if flag_cnt == cnt_prev:                            
                return False
            if flag_cnt == len(s):
                return True
            
if __name__ == '__main__':

    sln  = Solution()                

    s = "a"
    print(sln.isValid(s))

    s = "abc"
    print(sln.isValid(s))
    
    s = "aabcbc"
    print(sln.isValid(s))          
    
    s = "abcabcababcc"
    print(sln.isValid(s))
    
    s = "abccba"
    print(sln.isValid(s))
    
    s = "abacbcabcc"
    print(sln.isValid(s))