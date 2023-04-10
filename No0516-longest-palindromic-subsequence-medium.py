# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:09:20 2022

@author: Dell
"""
from typing import List
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo= dict()
        def dp(i,j):
            # print('dp: i = {0}, j={1}'.format(i,j))
            if (i,j) in memo:
                return memo[i,j]
            if i==j:
                return 1
            if i>j:
                return 0
            
            if s[i]==s[j]:
                memo[(i,j)] = dp(i+1,j-1) + 2
                return memo[(i,j)]
            else:
                # case2-1
                k = j-1
                tmp1 = 1
                while k > i:
                    if s[k] == s[i]:
                        tmp1 = dp(i+1,k-1) + 2
                        break
                    else:
                        k = k - 1
                # case2-2
                k = i+1
                tmp2 = 1
                while k < j:
                    if s[k] == s[j]:
                        tmp2 = dp(k+1,j-1) + 2
                        break
                    else:
                        k = k + 1
                # case2-3
                tmp3 = dp(i+1,j-1)
                memo[(i,j)] = max(tmp1,tmp2,tmp3)
                return memo[(i,j)]
            
        return dp(0,len(s)-1)
                
if __name__ == "__main__":
    
    sln = Solution()    

    s = "bb"
    print(sln.longestPalindromeSubseq(s))
    
    s = "bbbab"
    print(sln.longestPalindromeSubseq(s))
    
    s = "cbbd"
    print(sln.longestPalindromeSubseq(s))
    
    s= "abcdef"
    print(sln.longestPalindromeSubseq(s))