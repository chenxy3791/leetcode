# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:20:49 2022

@author: Dell
"""
import time

def fib_recur(k):
    # print('fib({0})...'.format(k))
    # baseline case
    if k <= 1:
        return k
    
    return fib_recur(k-1) + fib_recur(k-2)

def fib_recur_memo(k):
    memo = dict()
    def dp(m):
        # baseline case
        if m <= 1:
            return m
        if m in memo:
            return memo[m]
        ans = dp(m-1) + dp(m-2)
        memo[m] = ans
        return ans

    return dp(k)

def fib_iter(k):
    if k <= 1:
        return k
 
    fib    = (k+1) * [0]
    fib[1] = 1
    for i in range(2,k+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[k]

if __name__ == '__main__':
    
    for k in range(0,50,10):
        tstart = time.time()
        ans = fib_recur(k)
        tstop  = time.time()
        print('fib_recur({0}) = {1}, tcost = {2:5.3f}sec'.format(k, ans, tstop-tstart))

    for k in range(200,400,40):
        tstart = time.time()
        ans = fib_recur_memo(k)
        tstop  = time.time()
        print('fib_recur_memo({0}) = {1}, tcost = {2:5.3f}sec'.format(k, ans, tstop-tstart))
        
    for k in range(200,400,40):
        tstart = time.time()
        ans = fib_iter(k)
        tstop  = time.time()
        print('fib_iter({0}) = {1}, tcost = {2:5.3f}sec'.format(k, ans, tstop-tstart))        