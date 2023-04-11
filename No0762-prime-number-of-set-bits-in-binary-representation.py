# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 07:41:15 2022

@author: Dell
"""

def countOnes(num):
    # a = [int(c) for c in bin(num)[2:]]
    # return sum(a)
    cnt = 0
    while num > 0:
        cnt += num & 1
        num = num // 2
    return cnt

import time
import random
import itertools as it
class Solution:
    def countPrimeSetBits1(self, left: int, right: int) -> int:
        # def countOnes(num):
        #     a = [int(c) for c in bin(num)[2:]]
        #     return sum(a)
        
        def countOnes(num):
            cnt = 0
            while num > 0:
                cnt += num & 1
                num = num // 2
            return cnt
        
        primeLst = set([2,3,5,7,11,13,17,19,23,29,31])
        cnt = 0
        for num in range(left,right+1):
            if countOnes(num) in primeLst:
                cnt = cnt + 1
        return cnt

    def countPrimeSetBits1(self, left: int, right: int) -> int:
        # def countOnes(num):
        #     cnt = 0
        #     while num > 0:
        #         cnt += num & 1
        #         num = num // 2
        #     return cnt
        
        primeLst = set([2,3,5,7,11,13,17,19,23,29,31])
        cnt = 0
        for num in range(left,right+1):
            if bin(num).count('1') in primeLst:
                cnt = cnt + 1
        return cnt

    def countPrimeSetBits2(self, left: int, right: int) -> int:
        primeLst = set([2,3,5,7,11,13,17,19])
        cnt = 0
        maxlen = len(bin(right))-2
        # minlen = len(bin(left))-2
        # print(minlen, maxlen)
        for k in primeLst:
            if k > maxlen:
                continue
            # print('k = ',k)
            for item in it.combinations([2**m for m in range(maxlen)], k):
                curnum = 0                
                for i in item[::-1]:
                    curnum += i
                    if curnum > right:
                        break
                # print(item, curnum)
                if curnum >= left and curnum <= right:
                    cnt += 1
        return cnt
    
if __name__ == '__main__':
    
    # print(countOnes(10))
    # print(countOnes(10012))
    
    sln = Solution()
    left = 6
    right = 10
    print(sln.countPrimeSetBits1(left,right))
    print(sln.countPrimeSetBits2(left,right))
    
    left = 10
    right = 15
    print(sln.countPrimeSetBits1(left,right))
    print(sln.countPrimeSetBits2(left,right))
    
    for k in range(10):
        left    = random.randint(1,10**6-10**4)
        right   = left + 10**4
        tstart  = time.time()
        ans     = sln.countPrimeSetBits1(left,right)
        tstop   = time.time()
        print('left,right=({0},{1}), ans1 = {2}, tcost = {3:4.2f}(sec)'.format(left,right,ans, tstop-tstart))
        tstart  = time.time()
        ans     = sln.countPrimeSetBits2(left,right)
        tstop   = time.time()
        print('left,right=({0},{1}), ans2 = {2}, tcost = {3:4.2f}(sec)'.format(left,right,ans, tstop-tstart))
    