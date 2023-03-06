""" 
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
] 
"""

import time
import math

class Solution:
    #def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(self, n: int):
        k = 1
        next3 = 3
        next5 = 5
        rslt  = []
        while k <= n:
            if k == next3 and k == next5:
                rslt.append('FizzBuzz')
                next3 += 3
                next5 += 5
            elif k == next3:
                rslt.append('Fizz')
                next3 += 3
            elif k == next5:
                rslt.append('Buzz')                
                next5 += 5
            else:
                rslt.append(str(k))
            k += 1

        return rslt

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    tStart = time.time()        
    print('Testcase1...')
    n = 30
    print(sln.fizzBuzz(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
