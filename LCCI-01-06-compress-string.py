""" 
程序员面试金典(第6版)
面试题 01.06. Compress String LCCI
Implement a method to perform basic string compression using the counts of repeated 
characters. For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. You can assume the string has only 
uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation: 
The compressed string is "a1b2c2d1", which is longer than the original string.
"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

class Solution:
    def compressString(self, S: str) -> str:
        if len(S) <= 1:
            return S
        cnt = 1
        oLst = []
        for k in range(1,len(S)):
            if S[k] == S[k-1]:
                cnt += 1
            else:
                print('cnt = {0}, strcnt = {1}'.format(cnt, str(cnt)))
                oLst.append(S[k-1])
                oLst.append(str(cnt))
                cnt = 1
        #Handle the last repeated characters
        if cnt > 0:
            oLst.append(S[-1])
            oLst.append(str(cnt))
            
        oStr = ''.join(oLst)
        if len(oStr) >= len(S):
            return S
        else:
            return oStr
        
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()        

    print('\nTestcase1 ...')
    S = "aabcccccaaa"
    print(sln.compressString(S))

    print('\nTestcase2 ...')
    S = "abbccd"
    print(sln.compressString(S))