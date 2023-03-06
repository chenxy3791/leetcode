""" 
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

import time
import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pow3 = 1
        while 1:
            if pow3 == n:
                return True
            elif pow3 > n:
                return False
            pow3 *= 3

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    print('Testcase1...')
    tStart = time.time()        
    n = 0
    print(sln.isPowerOfThree(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    n = 9
    print(sln.isPowerOfThree(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    n = 45
    print(sln.isPowerOfThree(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    tStart = time.time()        
    n = 3**100
    print(sln.isPowerOfThree(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')        