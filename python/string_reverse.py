# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:19:27 2021

@author: chenxy
"""

import timeit
from statistics import mean
    
def rev_str_thru_slicing(aStr):
    return aStr[::-1]

def rev_str_thru_join_revd(aStr):
    return "".join(reversed(aStr))	

def rev_str_thru_list_reverse(aStr):
    lst = list(aStr)
    lst.reverse()
    return(''.join(lst))

def rev_str_thru_recursion(aStr):
    if len(aStr) == 0:
        return aStr
    else:
        return rev_str_thru_recursion(aStr[1:]) + aStr[0]

if __name__ == '__main__':
    
    #1. Decreasing slicing
    print('Decreasing slicing:   ','HelloPython'[::-1])
    
    #2. User-defined function based on decreasing slicing
    myStr = "HelloPython"
    print('User-defined function based on:   ',rev_str_thru_slicing(myStr))    

    #3. Using reversed() function
    print('Using reversed() function:    ',rev_str_thru_join_revd(myStr))	
    
    #4. Using list reverse() method
    print('Using list reverse() method:    ',rev_str_thru_list_reverse(myStr))
    
    #4. Using recursive function    
    print('Using recursive function:    ',rev_str_thru_recursion(myStr))
    
    # Performance comparison
    s = myStr * 10
    repeatCount = 10

    SLICING_PERF = timeit.repeat(lambda: rev_str_thru_slicing(s), repeat=repeatCount)
    print(min(SLICING_PERF), mean(SLICING_PERF), max(SLICING_PERF), SLICING_PERF)

    J_R_PERF = timeit.repeat(lambda: rev_str_thru_join_revd(s), repeat=repeatCount)
    print(min(J_R_PERF), mean(J_R_PERF), max(J_R_PERF), J_R_PERF)

    LIST_PERF = timeit.repeat(lambda: rev_str_thru_list_reverse(s), repeat=repeatCount)
    print(min(LIST_PERF), mean(LIST_PERF), max(LIST_PERF), LIST_PERF)

    RECUR_PERF = timeit.repeat(lambda: rev_str_thru_recursion(s), repeat=repeatCount)
    print(min(RECUR_PERF), mean(RECUR_PERF), max(RECUR_PERF), RECUR_PERF)    
    
    ratio0 = mean(SLICING_PERF)/mean(SLICING_PERF)
    ratio1 = mean(J_R_PERF)/mean(SLICING_PERF)
    ratio2 = mean(LIST_PERF)/mean(SLICING_PERF)
    ratio3 = mean(RECUR_PERF)/mean(SLICING_PERF)
    print('SLICING_PERF:J_R_PERF:LIST_PERF:RECUR_PERF = {0}:{1}:{2}:{3}'.format(ratio0,ratio1,ratio2,ratio3))