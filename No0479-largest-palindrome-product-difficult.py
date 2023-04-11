# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 05:52:56 2022

@author: Dell
"""
import time
class Solution:
    # def largestPalindrome(self, n: int) -> int:
    #     if n == 1:
    #         return 9
    #     upper = 10 ** n - 1
    #     for left in range(upper, upper // 10, -1):  # 枚举回文数的左半部分
    #         p, x = left, left
    #         while x:
    #             p = p * 10 + x % 10  # 翻转左半部分到其自身末尾，构造回文数 p
    #             x //= 10
    #         x = upper
    #         while x * x >= p:
    #             if p % x == 0:  # x 是 p 的因子
    #                 return p % 1337
    #             x -= 1

    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9        
        
        # case1: 2n digits number
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1): 
            # The left(upper) half of the palindrome
            x = str(left)
            p = int(x + x[::-1])
            
            x = upper
            # while x*x >= p and x >= 10 ** (n-1):
            while x*x >= p:
                if p%x == 0:
                    print('The answer is 2n digits number')
                    return p%1337
                x -= 1
        
        # case2: 2n-1 digits number
        upper1 = 10 ** (n-1) - 1
        for left in range(upper1, upper1 // 10, -1): 
            # The left(upper) half of the palindrome
            x = str(left)
            for k in range(10):
                p = int(x + str(k) + x[::-1])
                x = upper
                # while x*x >= p and x >= 10 ** (n-1):
                while x*x >= p:
                    if p%x == 0:
                        print('The answer is (2n-1) digits number')
                        return p%1337
                    x -= 1                            
            

if __name__ == "__main__":
    
    sln = Solution()
    
    for k in range(1,9):
        tstart = time.time()
        ans = sln.largestPalindrome(k)
        tstop  = time.time()
        print('k={0}, ans={1}, tcost={2:4.2f}'.format(k,ans,tstop-tstart))