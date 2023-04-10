# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 13:33:58 2022

@author: Dell
"""

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def maxConsecutiveLen(c):
            lptr = 0
            rptr = 0
            cnt  = 0
            maxlen = 0
            while rptr < len(answerKey):
                # print(lptr,rptr,cnt,maxlen)
                if answerKey[rptr] == c:
                    if cnt < k:
                        cnt += 1
                    else: # cnt == k:
                        maxlen = (rptr-lptr) if (rptr-lptr)>maxlen else maxlen
                        # Move lptr to right to skip the first c
                        while answerKey[lptr] != c:
                            lptr += 1
                        lptr += 1
                        # cnt   = k
                rptr += 1 # Common action for each step
                maxlen = (rptr-lptr) if (rptr-lptr)>maxlen else maxlen # For the last window
            # print(c, maxlen)
            return maxlen       
        
        return max(maxConsecutiveLen('F'),maxConsecutiveLen('T'))

if __name__ == '__main__':
    
    sln = Solution()
    answerKey,k = "TTFF",2
    print(sln.maxConsecutiveAnswers(answerKey, k))        

    answerKey = "TFFT"
    k = 1        
    print(sln.maxConsecutiveAnswers(answerKey, k))
    
    answerKey = "TTFTTFTT"
    k = 1
    print(sln.maxConsecutiveAnswers(answerKey, k))
    
    answerKey = "T"
    k = 1
    print(sln.maxConsecutiveAnswers(answerKey, k))