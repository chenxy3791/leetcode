# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 07:36:41 2022

@author: chenxy

564. 寻找最近的回文数
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
“最近的”定义为两个整数差的绝对值最小。

示例 1:
输入: n = "123"
输出: "121"

示例 2:
输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
 
提示:
1 <= n.length <= 18
n 只由数字组成
n 不含前导 0
n 代表在 [1, 10^18 - 1] 范围内的整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-closest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
import random

class Solution:
    def nearestPalindromicNG(self, n: str) -> str:
        nLen = len(n)
        if nLen==1:
            return str(int(n)-1)
        if int(n) == 11:
            return '9'
        if int(n) == 99:
            return '101'        
        if n[0]=='1' and int(n[1:])==0:
            return str(int(n)-1)
        
        if n == n[::-1]:
            # cannot return the input string itself.
            if nLen % 2 == 1: # odd length, decrement the center one digit by 1
                return str(int(n) - 10**(nLen//2))
            else:  # even length, decrement the center two digits by 1
                return str(int(n) - 10**(nLen//2) -10**(nLen//2-1))

        for k in range(nLen//2):
            # print(k)
            m = nLen - k - 1
            n_lst = list(n)
            n_lst[m] = n_lst[k]
            n = ''.join(n_lst)
            if n == n[::-1]:
                return n

    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1)
        s = n[: l // 2 + l % 2]
        s1 = str(int(s) - 1)
        s2 = str(int(s) + 1)
        return min(
            '9' * (l - 1), 
            '1' + '0' * (l - 1) + '1',
            s + s[-1 - l % 2::-1], 
            s1 + s1[-1 - l % 2::-1], 
            s2 + s2[-1 - l % 2::-1], 
            key=lambda x: (abs(int(x) - int(n)) or 114514, int(x))
        )
    
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        selfPrefix = int(n[:(m + 1) // 2])
        for x in range(selfPrefix - 1, selfPrefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        ans = -1
        selfNumber = int(n)
        for candidate in candidates:
            if candidate != selfNumber:
                if ans == -1 or \
                        abs(candidate - selfNumber) < abs(ans - selfNumber) or \
                        abs(candidate - selfNumber) == abs(ans - selfNumber) and candidate < ans:
                    ans = candidate
        return str(ans)
                                                    
if __name__ == '__main__':        
    
    sln = Solution()  

    n = "8"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))

    n = "99"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))

    n = "999"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))

    n = "100"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))

    n = "11"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))

    n = "123"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))
    
    n = "99321"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))    
    
    n = "12321"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))        
    
    n = "123321"
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))        

    n = str(random.randint(10**18,10**19-1))    
    tStart = time.time()        
    ans = sln.nearestPalindromic(n)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(n,ans,tElapsed))            