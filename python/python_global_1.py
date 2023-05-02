# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:11:05 2021

@author: chenxy
"""

myVar = 'hello python - global, in python_global_1 module'
def myFunction1():
    global myVar
    myVar = 'hello python - I changed you inside myFunction1'
    print('Inside myFunction1(): ',myVar)
# myFunction()
# print('Outside myFunction(): ',myVar)

# def recursionCall(k):
#     x = 'hello python - global - ' + str(k)
#     # print('k = {0}, x = {1}'.format(k,x))
#     print(x)
#     if k == 0:
#         return
#     recursionCall(k-1)

# recursionCall(12)
# print(x)    
