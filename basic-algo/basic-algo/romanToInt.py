""" 
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

import time
import math

class Solution:
    def getInt(self, s: str) -> int:
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        elif s == 'M':
            return 1000
        else:
            return None

    def romanToInt(self, s: str) -> int:
        k   = 0
        sum = 0
        while k < len(s)-1:
            if (s[k] == "I" and s[k+1] == "V") or (s[k] == "I" and s[k+1] == "X") or \
                (s[k] == "X" and s[k+1] == "L") or (s[k] == "X" and s[k+1] == "C") or \
                (s[k] == "C" and s[k+1] == "D") or (s[k] == "C" and s[k+1] == "M"):
                sum += self.getInt(s[k+1]) - self.getInt(s[k])
                k += 2
            else:
                sum += self.getInt(s[k])
                k += 1
        
        # The last character handling
        if k == len(s) - 1:
            sum += self.getInt(s[k])

        return sum

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    print('Testcase1...')
    tStart = time.time()        
    s = "III"
    print('expected = 3, actual = {0}'.format(sln.romanToInt(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    # Testcase2
    print('Testcase2...')
    tStart = time.time()        
    s = "IV"
    print('expected = 4, actual = {0}'.format(sln.romanToInt(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    # Testcase3
    print('Testcase3...')
    tStart = time.time()        
    s = "IX"
    print('expected = 9, actual = {0}'.format(sln.romanToInt(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')        
    
    # Testcase4
    print('Testcase4...')
    tStart = time.time()        
    s = "LVIII"
    print('expected = 58, actual = {0}'.format(sln.romanToInt(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    # Testcase5
    print('Testcase5...')
    tStart = time.time()        
    s = "MCMXCIV"
    print('expected = 1994, actual = {0}'.format(sln.romanToInt(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')        