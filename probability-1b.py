# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:48:42 2022

@author: Dell
"""
import numpy as np
k = 1
while True:
    y = 2*k
    x = int(np.ceil((1+np.sqrt(2))*y))
    
    if 2*x*(x-1) == (x+y)*(x+y-1):
        print('The minimal (x,y) pair is: ({0},{1})'.format(x,y) )
        break
    k = k + 1