# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:48:25 2022

@author: Dell
"""

import numpy as np

nomi  = np.prod(range(52,39,-1),dtype='float32')
denom = np.prod(range(1,14),dtype='float32')
combinations_52_13 =  nomi/ denom
p     = 4/combinations_52_13
print(nomi, denom, combinations_52_13,p) 