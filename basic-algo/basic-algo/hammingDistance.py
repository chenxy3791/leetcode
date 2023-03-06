""" 
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

import time
import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0
        countOne = 0
        while k < 32:
            x = n & 0x1
            countOne += x
            n = n >> 1
            if n == 0:
                break

        return countOne

    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        return (self.hammingWeight(z))


if __name__ == '__main__':

    sln   = Solution()

    print('Testcase1...')
    tStart = time.time()        
    x = 1
    y = 4
    print('expected = 2, actual = {0}'.format(sln.hammingDistance(x,y)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase2...')
    tStart = time.time()        
    x = 2**31 - 1
    y = 0
    print('expected = 31, actual = {0}'.format(sln.hammingDistance(x,y)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')