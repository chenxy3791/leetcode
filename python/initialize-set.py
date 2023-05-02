# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:15:55 2021

@author: chenxy
"""

s = set((1, 2, 3))  # create set from tuple
s = set([1, 2, 3])  # create set from list
s = set('ABC')      # create set from string
s = set() # Create an empty set

s = {1, 2, 3}
print(s)        # {1, 2, 3}

s = {}
print(type(s))  # <class 'dict'>

x = [1, 2, 3]   # list
s = {*x}
print(s)        # { 1, 2, 3}