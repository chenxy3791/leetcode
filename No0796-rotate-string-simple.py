# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 07:01:22 2022

@author: Dell
"""

class Solution:
    def rotateString1(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        for k in range(1,len(s)):
            s = s[-1] + s[:-1]
            if s == goal:
                return True
        return False

    def rotateString2(self, s: str, goal: str) -> bool:
        # 执行用时：40 ms, 在所有 Python3 提交中击败了29.86%的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了32.72%的用户        
        if len(s) != len(goal):
            return False        
        return ((s + s[:-1]).find(goal)) >= 0

    def rotateString3(self, s: str, goal: str) -> bool:      
        # 执行用时：32 ms, 在所有 Python3 提交中击败了82.66%的用户
        # 内存消耗：15 MB, 在所有 Python3 提交中击败了31.03%的用户
        return len(s) == len(goal) and goal in (s + s[:-1])        
    
if __name__ =='__main__':
    
    sln = Solution()
    
    s = "abcdefghijklmnopqrstuvwxyz"
    goal = "opqrstuvwxyzabcdefghijklmn"
    print(sln.rotateString1(s, goal))
    print(sln.rotateString2(s, goal))
    print(sln.rotateString3(s, goal))
    print()
    
    s = "abc"
    goal = "abc"
    print(sln.rotateString1(s, goal))
    print(sln.rotateString2(s, goal))    
    print(sln.rotateString3(s, goal))
    print()
    
    s = "abcd"
    goal = "abc"
    print(sln.rotateString1(s, goal))
    print(sln.rotateString2(s, goal))       
    print(sln.rotateString3(s, goal))
    print()