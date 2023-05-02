# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:04:00 2021

@author: chenxy
"""

import itertools as it

# myDict = {'one': 24, 'two': 13, 'three': 54, 'four': 9}
# keyWithMaxValue = max(myDict, key=myDict.get)
# print(keyWithMaxValue)

# # enumerate
# a = 'I am a python fan'
# for k in range(len(a)):
#     print(a[k],end=' ')
# print('\n')    

# for c in a:
#     print(c,end=' ')
# print('\n')    
    
# for k,c in enumerate(a):
#     print('{0}:{1}'.format(k,c))
# print('\n')   

# for k,c in enumerate(a, start=-4):
#     print('{0}:{1}'.format(k,c))
# print('\n')   
    
# enumobj = enumerate(a);
# print(list(enumobj))

# Convert iterator to list
# myIterator = it.product('AB', repeat=2)
# print(myIterator)
# print('list(myIterator) = ',list(myIterator))
# print('List Comprehension: ',[i for i in myIterator])
# print('[*myIterator] = ',[*myIterator])

myIterator = iter(range(10))
print('Iterator unpacking operator: ',[*myIterator])
print('List Comprehension: ',[i for i in myIterator])
print('Type constructor: ',list(myIterator))