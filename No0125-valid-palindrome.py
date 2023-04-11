# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 07:57:19 2022

@author: Dell
"""

class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     s1 = ''
    #     for c in s:
    #         if c.isalnum():
    #             s1 = s1 + c
    #     s1 = s1.lower()
    #     return s1 == s1[::-1]

    def isPalindrome(self, s: str) -> bool:
        lptr = 0
        rptr = len(s) - 1
        
        while lptr < rptr:
            if s[lptr].isalnum():
                while rptr >= lptr:
                    if s[rptr].isalnum():
                        if s[lptr].lower() != s[rptr].lower():
                            return False
                        rptr -= 1
                        break
                    rptr -= 1
            lptr += 1
        return True
    
if __name__ == '__main__':
    
    sln = Solution()
    
    print(sln.isPalindrome("A man, a plan, a canal: Panama"))
    
    print(sln.isPalindrome("race a car"))
    
    print(sln.isPalindrome(""))