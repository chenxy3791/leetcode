# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:08:25 2023

@author: chenxy

2423. Remove Letter To Equalize Frequency
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.
 

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
 

Constraints:

2 <= word.length <= 100
word consists of lowercase English letters only.
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
    def equalFrequency(self, word: str) -> bool:
        
        h = defaultdict(int)
        for c in word:
            h[c] += 1
        
        cnts = list(h.values())
        # print(cnts)                       
        if cnts.count(1) == len(word):
            return True
        if len(cnts) == 1:
            return True
        # if cnts.count(1) == len(cnts)-1 and cnts.count(2) == 1:
        #     return True
        
        for k,cnt in enumerate(cnts):
            if cnt != 1:
                if (cnts.count(cnt) == len(cnts) - 1) and (cnts.count(1)==1):
                    return True
                else:
                    break

        min_cnt = min(cnts)
        cnts_ = [cnts[k]-min_cnt for k in range(len(cnts))]
        # print(cnts,cnts_)
        if cnts_.count(1) == 1 and cnts_.count(0) == len(cnts)-1:
            return True
        return False

    # def equalFrequency(self, word: str) -> bool:
    #     charCount = [0] * 26
    #     for c in word:
    #         charCount[ord(c) - ord('a')] += 1
    #     freqCount = Counter(c for c in charCount if c > 0)
    #     for c in charCount:
    #         if c == 0: continue
    #         freqCount[c] -= 1
    #         if freqCount[c] == 0:
    #             del freqCount[c]
    #         if c - 1 > 0:
    #             freqCount[c - 1] += 1
    #         if len(freqCount) == 1:
    #             return True
    #         if c - 1 > 0:
    #             freqCount[c - 1] -= 1
    #         if freqCount[c - 1] == 0:
    #             del freqCount[c - 1]
    #         freqCount[c] += 1
    #     return False
                                
if __name__ == '__main__':

    sln  = Solution()                
    
    word = "abcc"
    print(sln.equalFrequency(word))              
    
    word = "aazz"
    print(sln.equalFrequency(word))                  
    
    word = "abc"
    print(sln.equalFrequency(word))                  
    
    word = "ddaccb"
    print(sln.equalFrequency(word))                  
    
    word = "cccd"
    print(sln.equalFrequency(word))                  
    
    word = "ccccccc"
    print(sln.equalFrequency(word))                  
    
    word = "cccaa"
    print(sln.equalFrequency(word))                  
    
    word = "abcdefghijklmnopqrstuvwxyznabcdefghijklmnopqrstuvwxyz"
    print(sln.equalFrequency(word))                  