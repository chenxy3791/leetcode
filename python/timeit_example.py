# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:55:31 2021

@author: chenxy
"""

# importing the required module
import timeit

# code snippet to be executed only once
# mysetup = "from math import sqrt"

# Example1
# code snippet whose execution time is to be measured
mycode1 = '''
mylist = list(range(1000))
for k in range(1000):
    if k in mylist:
        pass		
'''

mycode2 = '''
myset = set(range(1000))
for k in range(1000):
    if k in myset:
        pass		
'''

mycode3 = '''
mydict = dict.fromkeys(list(range(1000)),'')
for k in range(1000):
    if k in mydict:
        pass		
'''

# timeit statement
print('tCost for mycode1: ', timeit.timeit(stmt = mycode1, number = 1000) )
print('tCost for mycode2: ', timeit.timeit(stmt = mycode2, number = 1000) )
print('tCost for mycode3: ', timeit.timeit(stmt = mycode3, number = 1000) )


# Example2
mysetup1 = "from math import sqrt"
mycode1 = '''
mylist = []
for k in range(1000):
    mylist.append(sqrt(k))
'''

mysetup2 = "import numpy as np"
mycode2 = '''
mylist = []
for k in range(1000):
    mylist.append(np.sqrt(k))
'''

mysetup3 = "import numpy as np"
mycode3 = '''
myrslt = np.sqrt(np.array(list(range(1000))))
'''

print('tCost for mycode1: ', timeit.timeit(setup = mysetup1, stmt = mycode1, number = 1000) )
print('tCost for mycode2: ', timeit.timeit(setup = mysetup2, stmt = mycode2, number = 1000) )
print('tCost for mycode3: ', timeit.timeit(setup = mysetup3, stmt = mycode3, number = 1000) )


# Example3, timeit.repeat()
print('\nExample3: ...')
mysetup3 = '''
from math import sqrt
def example3(N):
    mylist = []
    for k in range(N):
        mylist.append(sqrt(k))
'''
mycode3 = '''
example3(1000)
'''
print('tCost for mycode3: ', timeit.repeat(setup = mysetup3, stmt = mycode3, number = 1000, repeat=100) )
# import matplotlib.pyplot as plt
# import scipy.stats as stats
# print('max = {0}, min = {1}, mean = {2}'.format())
# plt.show()

# Command line
# python -m timeit -s "from math import sqrt" -n 10000 -r 10 'x=sqrt(12345678)'