# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:50:11 2021

@author: chenxy
"""

# # Problem1 - level 1
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(l)
# # print (','.join(l))

# # Problem2 - level 1
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# print('请输入一个数字：')
# x=int(input())
# print (fact(x))

# Problem3 - level 1
# print('请输入一个数字：')
# x=int(input())
# myDict = dict()
# for k in range(1,x+1):
#     myDict[k] = k*k
# print(myDict)    

# Problem4 - level 1
# Input example: 34岁,67年,55岁,33岁,12日,98年
import re
print('请输入一组数字：')
values=input()
l=values.split(",")
print(l)
k=re.findall(r'[0-9]+',values)
t=tuple(k)
print (k)
print (t)