""" 
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. 
In this case, both input and output will be given as signed integer type and 
should not affect your implementation, as the internal binary representation 
of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 2 above the input represents the signed integer -3 and the 
output represents the signed integer -1073741825.

Follow up:

If this function is called many times, how would you optimize it?

NOTE:
A bit confused.
Because python doesn't has built-in unsigned data type, so I think it will behave just like Java.
But seems not that.

"""

import time
import math

class Solution:
    def reverseBits(self, n: int) -> int:
        weight0 = 2**31

        k= 0
        sum = 0
        while k < 32:
            lsb  = n & 0x1
            #if k == 0:
            #    sum += (-1) * lsb * weight0
            #else:
            #    sum += lsb * weight0
            sum += lsb * weight0
            weight0 /= 2
            n = n >> 1
            k += 1
        return int(sum)

if __name__ == '__main__':

    sln   = Solution()

    print('Testcase1...')
    tStart = time.time()        
    n = 0b00000010100101000001111010011100
    print('expected = 964176192, actual = {0}'.format(sln.reverseBits(n)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase2...')
    tStart = time.time()        
    n = 0b11111111111111111111111111111101
    print('expected = 3221225471, actual = {0}'.format(sln.reverseBits(n)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase3...')
    tStart = time.time()        
    n = -3
    print('expected = -1073741825, actual = {0}'.format(sln.reverseBits(n)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')