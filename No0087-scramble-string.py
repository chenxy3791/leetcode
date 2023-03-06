# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:49:23 2021

@author: chenxy
87. 扰乱字符串
使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。

 

示例 1：

输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
示例 2：

输入：s1 = "abcde", s2 = "caebd"
输出：false
示例 3：

输入：s1 = "a", s2 = "a"
输出：true
 

提示：

s1.length == s2.length
1 <= s1.length <= 30
s1 和 s2 由小写英文字母组成
"""
import typing
import time
import random
import sys
    
class Solution:
    def isScrambleNoMemo(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            raise ValueError(len(s1), len(s2))
        
        if len(s1)==1:
            return s1 == s2
        
        for k in range(1,len(s1)):
            # print('isScramble({0},{1}, k = {2})'.format(s1,s2,k))
            s11,s12 = s1[0:k], s1[k:]
            
            s21,s22 = s2[0:k], s2[k:]            
            f1 = self.isScrambleNoMemo(s11, s21) and self.isScrambleNoMemo(s12, s22)
            
            s21,s22 = s2[len(s1)-k:], s2[0:len(s1)-k]
            f2 = self.isScrambleNoMemo(s11, s21) and self.isScrambleNoMemo(s12, s22)
            
            if f1 or f2:
                return True
        
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            raise ValueError(len(s1), len(s2))

        memo = dict()
        
        def dp(k1,k2,L):
            # Check the equivalence between s1[k1:k1+L-1] and s2[k2:k2+L-1]
            # print('dp({0},{1},{2})'.format(k1,k2,L))
            if (k1,k2,L) in memo:
                return memo[k1,k2,L]

            if L==1:
                return s1[k1] == s2[k2]

            for l in range(1,L):
                # print('isScramble({0},{1}, k = {2})'.format(s1,s2,k))
           
                f1 = dp(k1,k2,l) and dp(k1+l,k2+l,L-l)
                if f1:
                    memo[k1,k2,L] = True
                    return True
                f2 = dp(k1,k2+L-l,l) and dp(k1+l,k2,L-l)
                if f2:
                    memo[k1,k2,L] = True
                    return True
            
            memo[k1,k2,L] = False
            return False            
                    
        if len(s1)==1:
            return s1 == s2

        
        return dp(0,0,len(s1))
        
if __name__ == '__main__':        
    
    sln = Solution()        
    
    s1 = "gr"
    s2 = "rg"    
    print(s1,s2, ' -> ', sln.isScramble(s1,s2))
    
    s1 = "great"
    s2 = "rgeat"    
    print(s1,s2, ' -> ', sln.isScramble(s1,s2))

    s1 = "abcde"
    s2 = "caebd"    
    print(s1,s2, ' -> ', sln.isScramble(s1,s2))    

    s1 = "a"
    s2 = "a"    
    print(s1,s2, ' -> ', sln.isScramble(s1,s2))        

    t1 = time.time()
    s1 = "abcdefghijklmn"
    s2 = "hijklmngdefabc"    
    print(s1,s2, ' -> ', sln.isScrambleNoMemo(s1,s2))        
    t2 = time.time()    
    print(t2-t1)        
    print(s1,s2, ' -> ', sln.isScramble(s1,s2))        
    t3 = time.time()    
    print(t3-t2)        

    t1 = time.time()
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "stuvwxyzlmnopqrbcdefghijka"    
    print(s1,s2, ' -> ', sln.isScrambleNoMemo(s1,s2))        
    t2 = time.time()    
    print(t2-t1)        
    print(s1,s2, ' -> ', sln.isScramble(s1,s2))        
    t3 = time.time()    
    print(t3-t2)            