# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:11:05 2021

@author: chenxy
"""

# Example 1
# def myFunction():
#     print('Inside myFunction(): ',myVar)
# myVar = 'hello python - global'
# myFunction()
# print('Outside myFunction(): ',myVar)

# Example 2
# def myFunction():
#     print('Inside myFunction(): ',myVar)
# myFunction()
# myVar = 'hello python - global'
# print('Outside myFunction(): ',myVar)

# Example 3
# myVar = 'hello python - global'
# def myFunction():
#     myVar = 'hello python - local'
#     print('Inside myFunction(): ',myVar)
# myFunction()
# print('Outside myFunction(): ',myVar)

# Example 4
# myVar = 'hello python - global'
# def myFunction():
#     global myVar
#     myVar = 'hello python - I changed you inside myFunction'
#     print('Inside myFunction(): ',myVar)
# myFunction()
# print('Outside myFunction(): ',myVar)

# Example 5
from python_global_1 import *
def myFunction():
    print('Inside myFunction(): ',myVar)
myFunction()
print('Outside myFunction(): ',myVar)

# def recursionCall(k):
#     x = 'hello python - global - ' + str(k)
#     # print('k = {0}, x = {1}'.format(k,x))
#     print(x)
#     if k == 0:
#         return
#     recursionCall(k-1)

# recursionCall(12)
# print(x)    
