# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:03:43 2021

@author: chenxy

263. 丑数
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

 

示例 1：

输入：n = 6
输出：true
解释：6 = 2 × 3
示例 2：

输入：n = 8
输出：true
解释：8 = 2 × 2 × 2
示例 3：

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。
示例 4：

输入：n = 1
输出：true
解释：1 通常被视为丑数。
 

提示：

-2^31 <= n <= 2^31 - 1

"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: # Ugly number must be positive number!
            return False
        
        if n == 1:
            return True
        
        m = n
    
        # Check whether n can be divided by any one among 2 and 3 and 5, if not, it is not ugly number.
        if m%3 != 0 and m%2 != 0 and m%5 != 0:
            return False
    

        while (m%5)==0:
            m = m//5
        if m == 1:
            return True
                
        while (m%3)==0:
            m = m//3
        if m == 1:
            return True
        
        while (m%2)==0:
            m = m//2
        if m == 1: 
            return True        
        else:
            return False

if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()

    n = 0
    print(n, ' -> ', sln.isUgly(n))        

    n = 6
    print(n, ' -> ', sln.isUgly(n))        

    n = 8
    print(n, ' -> ', sln.isUgly(n))                
        
    n = 14
    print(n, ' -> ', sln.isUgly(n))                   
    
    n = 1
    print(n, ' -> ', sln.isUgly(n))                       
    
    n = 2**5 * 3**6 * 11
    print(n, ' -> ', sln.isUgly(n))                           

    n = -2**5 * 3**6 * 11
    print(n, ' -> ', sln.isUgly(n))                               
    
    n = 2**15 * 3**6
    print(n, ' -> ', sln.isUgly(n))                               

    n = 2**5 * 3**7 * 5**3
    print(n, ' -> ', sln.isUgly(n))                                   
    n = -2**5 * 3**7 * 5**3
    print(n, ' -> ', sln.isUgly(n))                                   
    
    n = 186479*7
    print(n, ' -> ', sln.isUgly(n))                    
    n = -186479*7
    print(n, ' -> ', sln.isUgly(n))                        
    
    n = -2147483648
    print(n, ' -> ', sln.isUgly(n))                        