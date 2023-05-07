# -*- coding: utf-8 -*-
"""
Created on Sat May  6 08:23:32 2023

@author: chenxy

1419. Minimum Number of Frogs Croaking
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, 
that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. 
The frogs have to print all five letters to finish a croak. 
If the given string is not a combination of a valid "croak" return -1.

Example 1:
Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.

Example 2:
Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
 
Constraints:
1 <= croakOfFrogs.length <= 10**5
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
"""
import os
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
    def minNumberOfFrogs_slow(self, croakOfFrogs: str) -> int:
        d = {"c":0, "r":1, "o":2, "a":3, "k":4 }
        lst_of_lst = []
        
        max_cnt = 0
        cnt = 0
        for c in croakOfFrogs:            
            # print(c,lst_of_lst)
            fail = True
            if c == 'c':
                lst_of_lst.append([0])
                # fail = False
                cnt = cnt + 1
                max_cnt = max(cnt,max_cnt)
                continue
                
            for i,lst in enumerate(lst_of_lst):
                if d[c] == lst[-1] + 1:
                    if c == 'k':
                        lst_of_lst.pop(i)
                        cnt = cnt - 1
                        # max_cnt = max(cnt,max_cnt)
                    else:
                        lst.append(d[c])                    
                    fail = False
                    break
            if fail:
                print(lst_of_lst,c)
                return -1
        print(lst_of_lst)
        return max_cnt if len(lst_of_lst) == 0 else -1

    def minNumberOfFrogs_slower(self, croakOfFrogs: str) -> int:
        '''
        Slower than the above one! Why?
        '''
        d = {"c":0, "r":1, "o":2, "a":3, "k":4 }
        tails = []
        
        max_cnt = 0
        cnt = 0
        for c in croakOfFrogs:            
            # print(c,lst_of_lst)
            fail = True
            for i,tail in enumerate(tails):
                if d[c] == (tail + 1) % 5:
                    tails[i] = d[c]
                    fail = False
                    break
            if fail:
                if c == 'c':
                    tails.append(0)
                else:
                    return -1
                            
        # print(tails)
        for tail in tails:
            if tail !=4:
                return -1
        return len(tails)

    def minNumberOfFrogs_OK_not_fast_enough(self, croakOfFrogs: str) -> int:
        
        d = {"c":0, "r":1, "o":2, "a":3, "k":4 }
        # tails = defaultdict(int) # {tail: count}
        h = 5 * [0]
        
        for s in croakOfFrogs:            
            # print(c,lst_of_lst)
            c   = d[s]
            c_1 = (c-1)%5
            
            if h[c_1] > 0:
                h[c-1] -= 1
                h[c]   += 1
            else:
                if s == 'c':
                    h[0] += 1
                else:
                    return -1
        if h[0]==h[1]==h[2]==h[3]==0:
            return h[4]
        else:
            return -1

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        d = {"c":0, "r":1, "o":2, "a":3, "k":4 }
        # tails = defaultdict(int) # {tail: count}
        h = 5 * [0]
        
        for s in croakOfFrogs:            
            # print(c,lst_of_lst)
            c   = d[s]
            
            if c == 0:
                h[c] += 1
                if h[4] > 0:
                    h[4] -= 1
            else:                            
                if h[c-1] > 0:
                    h[c-1] -= 1
                    h[c]   += 1
                else:
                    return -1
        if h[0]==h[1]==h[2]==h[3]==0:
            return h[4]
        else:
            return -1
            
if __name__ == '__main__':

    sln  = Solution()                

    croakOfFrogs = "croakcroak"
    print(sln.minNumberOfFrogs(croakOfFrogs))                
    
    croakOfFrogs = "crcoakroak"
    print(sln.minNumberOfFrogs(croakOfFrogs))                
    
    croakOfFrogs = "croakcrook"
    print(sln.minNumberOfFrogs(croakOfFrogs))                 
    
    croakOfFrogs = "croakcroa"
    print(sln.minNumberOfFrogs(croakOfFrogs))                 
          
    file_path = "./No1419-testdata.txt" 
    #check if file is present
    if os.path.isfile(file_path):
        #open text file in read mode
        text_file = open(file_path, "r")
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close() 
        croakOfFrogs = data[1:-1]
        # print(croakOfFrogs)
        print(len(croakOfFrogs), croakOfFrogs[:10])

    tStart= time.time()
    print(sln.minNumberOfFrogs(croakOfFrogs))             
    tStop = time.time()
    print("Time cost is {0}".format(tStop-tStart))            
    