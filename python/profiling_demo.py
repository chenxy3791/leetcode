# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:41:38 2021

@author: chenxy
"""

import numpy as np
import time
import timeit

def test_func(N: int):
    rng = np.random.default_rng()
    a   = rng.integers(2*N,size=N)
    b   = np.sort(a)
    # print(b[:100])    

# Case 1
tStart = time.time()        
test_func(10000000)
tCost = time.time() - tStart        
print('tCost = ', tCost, ' (sec)')

# Case 2
tStart = time.monotonic()   
test_func(10000000)
tCost = time.monotonic() - tStart        
print('tCost = ', tCost, ' (sec)')

# Case 3
tStart = time.process_time()
test_func(10000000)
tCost = time.process_time() - tStart        
print('tCost = ', tCost, ' (sec)')

# Case 4
tStart = time.perf_counter()
test_func(10000000)
tCost = time.perf_counter() - tStart        
print('tCost = ', tCost, ' (sec)')

# Difference between process_time and perf_counter
print(time.process_time()); time.sleep(10); print(time.process_time())
print(time.perf_counter()); time.sleep(10); print(time.perf_counter())

# Case 5. For better formatting
import time
start_time = time.time()
test_func(1000000000)
elapsed_time = time.time() - start_time
print('tCost(H:M:S) = ',time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

# Case 6
import datetime
start = datetime.datetime.now()
test_func(10000000)
end = datetime.datetime.now()
elapsed = end - start
print('tCost =  {0} (sec) : {1} (milisec)'.format( elapsed.seconds,elapsed.microseconds) )