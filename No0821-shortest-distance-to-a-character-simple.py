# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 06:43:17 2022

@author: Dell
"""
from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_pos = []
        for k in range(len(s)):
            if s[k]==c:
                c_pos.append(k)
        # print(c_pos)
        ans = len(s)*[0]
        for i in range(c_pos[0]):
            ans[i] = c_pos[0] - i
        for i in range(c_pos[-1],len(s)):
            ans[i] = i - c_pos[-1]
        
        for k in range(0,len(c_pos)-1):
            for i in range(c_pos[k],c_pos[k+1]):
                # print(c_pos[k],c_pos[k+1])
                ans[i] = min(i-c_pos[k],c_pos[k+1]-i)
        
        return ans

if __name__ == "__main__":
    
    sln = Solution()
    
    s = "loveleetcode"
    c = "e"
    print(sln.shortestToChar(s, c))
    
    s = "aaab"
    c = "b"