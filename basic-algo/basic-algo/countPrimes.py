""" 
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

import time
import math

class Solution:
    def countPrimes1(self, n: int) -> int:
        # Judged as Time-Out.
        lst = [k for k in range(n)]
        for k in range(2,int(n/2)+1):
            m = 2
            while (m*k) < n:
                #print('k = {0}, m = {1}'.format(k,m))
                lst[m*k] = None
                m += 1
        cntPrimes = 0
        for k in range(2,n):
            if lst[k] != None:
                cntPrimes += 1
                
        return cntPrimes

    def countPrimes2(self, n: int) -> int:
        # Somehow improved, but fail again.
        lst = [k for k in range(n)]
        for k in range(2,int(n/2)+1):
            m = 2*k
            while m < n:
                #print('k = {0}, m = {1}'.format(k,m))
                lst[m] = None
                m += k
        cntPrimes = 0
        for k in range(2,n):
            if lst[k] != None:
                cntPrimes += 1
                
        return cntPrimes

    def countPrimes3(self, n: int) -> int:
        # Greatly improved, Passed.
        lst = [k for k in range(n)]
        for k in range(2,int(n/2)+1):
            if lst[k] == None:
                continue
            m = 2*k
            while m < n:
                #print('k = {0}, m = {1}'.format(k,m))
                lst[m] = None
                m += k
        cntPrimes = 0
        for k in range(2,n):
            if lst[k] != None:
                cntPrimes += 1
                
        return cntPrimes

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    print('Testcase1...')
    tStart = time.time()        
    n = 1500000
    print(sln.countPrimes1(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    n = 1500000
    print(sln.countPrimes2(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    n = 1500000
    print(sln.countPrimes3(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    