# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 08:45:03 2023

@author: chenxy

1653. 使字符串平衡的最少删除次数
给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。

你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，
且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。

请你返回使 s 平衡 的 最少 删除次数。

示例 1：

输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
示例 2：

输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。
 

提示：

1 <= s.length <= 105
s[i] 要么是 'a' 要么是 'b'​ 。​

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

class Solution:
    def minimumDeletions_1(self, s: str) -> int:
        memo = dict()        
        def dp(substr):
            if substr in memo:
                return memo[substr]
            if len(substr)==1:
                return 0
            
            if substr[0] == 'b':
                rslt1 = 1 + dp(substr[1:])
                rslt2 = substr.count('a')
                rslt  = min(rslt1,rslt2)
            else:
                rslt  = dp(substr[1:])
                
            memo[substr] = rslt
            return rslt
        return dp(s)

    def minimumDeletions_2(self, s: str) -> int:
        memo = dict()        
        def dp(k):
            if s[k:] in memo:
                return memo[k]
            if k==len(s)-1:
                return 0
            
            if s[k] == 'b':
                rslt1 = 1 + dp(k+1)
                rslt2 = s[k:].count('a')
                rslt  = min(rslt1,rslt2)
            else:
                rslt  = dp(k+1)
                
            memo[k] = rslt
            return rslt
        return dp(0)

    def minimumDeletions(self, s: str) -> int:
        mindel = 0 # 令dp表示将s[0,i]变平衡最少需要删除的次数
        countB = 0 
        for c in s:
            if c == 'a':
                mindel = min(mindel+1, countB) # 末尾出现a的时候，2个选择：1、删除这个a，然后将s[0,i-1]变平衡；2、保留这个a，删除前面所有的b
            else:
                countB += 1 # 出现b的时候，最后面的b不需要删除，dp不变，b的个数加1就好
        return mindel
    
if __name__ == '__main__':

    sln  = Solution()                
    
    s = "aababbab"
    print(sln.minimumDeletions(s))
    
    s = "bbaaaaabb"
    print(sln.minimumDeletions(s))
    
    s = "b"
    print(sln.minimumDeletions(s))
    
    s = "babbabbbabbbbabbbbba"
    print(sln.minimumDeletions(s))
    
    #open text file in read mode
    fptr = open("No1653_testdata.txt", "r")
    #read whole file to a string
    s = fptr.read()     
    #close file
    fptr.close()     
    print(s, len(s))
    tStart= time.time()
    # print(sln.minimumDeletions(s[:5000]))    
    print(sln.minimumDeletions(s))    
    tStop= time.time()
    print("Time cost is {0}".format(tStop-tStart))    
    