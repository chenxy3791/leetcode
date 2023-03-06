""" 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

import time
import math

class Solution:
    def isMatch(self, c1:str, c2:str):
        #print(c1,c2)
        if (c1 == '(' and c2 == ')') or (c1 == '[' and c2 == ']') or (c1 == '{' and c2 == '}'):
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        charLst = []
        for k in range(len(s)):
            if k == 0:
                charLst.append(s[k])                
            else:
                if len(charLst) > 0:
                    if self.isMatch(charLst[-1], s[k]):
                        charLst.pop()
                    else:
                        charLst.append(s[k])
                else:
                    charLst.append(s[k])
        #print(charLst)
        if len(charLst) == 0:
            return True
        else:
            return False

if __name__ == '__main__':

    sln   = Solution()

    print('Testcase1...')
    tStart = time.time()        
    s = "()"
    print('expected = True, actual = {0}'.format(sln.isValid(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase2...')
    tStart = time.time()        
    s = "()[]{}"
    print('expected = True, actual = {0}'.format(sln.isValid(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase3...')
    tStart = time.time()        
    s = "(]"
    print('expected = False, actual = {0}'.format(sln.isValid(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    print('Testcase4...')
    tStart = time.time()        
    s = "([)]"
    print('expected = False, actual = {0}'.format(sln.isValid(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    print('Testcase5...')
    tStart = time.time()        
    s = "{[]}"
    print('expected = True, actual = {0}'.format(sln.isValid(s)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')       