# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:15:33 2022

@author: Dell
"""
from typing import List
import time
class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     def dfs(k):
    #         # print(k, s[k:])
    #         if k == len(s):
    #             return True
    #         for word in wordDict:
    #             # print(word)
    #             if s.find(word,k)==k:
    #                 if dfs(k+len(word)):
    #                     return True
    #         return False
    #     return dfs(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp    = (len(s)+1) * [False]
        dp[0] = True
        for k in range(1,len(s)+1):
            for word in wordDict:
                if k>=len(word) and s[k-len(word):k]==word:
                    if dp[k-len(word)]:
                        dp[k] = True
                        break
        # print(dp)
        return dp[len(s)]
                    
if __name__ == "__main__":
    
    sln = Solution()  
    
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(sln.wordBreak(s, wordDict))
    
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sln.wordBreak(s, wordDict))
    
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sln.wordBreak(s, wordDict))
    
    with open('No0139-testcase.py','r') as f:
        exec(f.read())  
    tstart=time.time()    
    print(sln.wordBreak(s, wordDict))
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))    