""" 
409. Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

解题思路：
构成Palindrome的字符除了最中间的字符（当长度为奇数时）以外，其余是成对出现。
所以扫描寻找成对出现的字符，假设有N对。
如果最后还剩下其它字符，则答案为2*N+1；如果没有的话就是2*N

"""
import math
import time
import random
import string
import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        sl = list(s)
        sl.sort()

        totallen = 0
        ptr = 0
        while ptr < len(sl)-1:
            if sl[ptr]==sl[ptr+1]:
                totallen += 2
                ptr += 2
            else:
                ptr += 1
        if totallen == len(s):
            return totallen
        else:
            return totallen+1
                                       
if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    s = "abccccdd"
    tStart= time.time()
    print(sln.longestPalindrome(s))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))

    print('\ntestcase2 ...')
    s = "a"
    tStart= time.time()
    print(sln.longestPalindrome(s))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))

    print('\ntestcase3 ...')
    s = ""
    tStart= time.time()
    print(sln.longestPalindrome(s))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))

    print('\ntestcase4 ...')
    N = 1000
    s = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(N)])
    print(s)
    tStart= time.time()
    print(sln.longestPalindrome(s))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))    

    print('\ntestcase5 ...')
    s = "aba"
    tStart= time.time()
    print(sln.longestPalindrome(s))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))    