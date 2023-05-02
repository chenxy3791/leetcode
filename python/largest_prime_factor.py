# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:00:05 2021

@author: chenxy

Ref: https://stackoverflow.com/questions/15347174/python-finding-prime-factors
"""

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n