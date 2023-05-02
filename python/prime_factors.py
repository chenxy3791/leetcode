# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:51:14 2021

@author: chenxy
"""

import timeit

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

if __name__ == '__main__':        
    
    N = 1000
    pfs = prime_factors(N)
    # largest_prime_factor = max(pfs) # The largest element in the prime factor list
    print('N={0}, pfs={1}'.format(N,pfs))
    
    # timeit.timeit(prime_factors(1000))