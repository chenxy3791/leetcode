# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:30:18 2021

@author: chenxy
"""

# myDict = {[1,2,3]:'123', 'name':'chenxy'}
# mySet  = set()
# mySet.add([1,2,3])

myDict = {tuple([1,2,3]):'123', 'name':'chenxy'}
mySet  = set()
mySet.add(tuple([1,2,3]))
print(myDict)
print(mySet)