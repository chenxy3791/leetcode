# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:03:43 2021

@author: chenxy

264. 丑数 II
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

 

示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。
 

提示：

1 <= n <= 1690

"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
# =2021-04-11==================================================================
# 执行结果：通过 显示详情
# 执行用时：7176 ms, 在所有 Python3 提交中击败了5.03%的用户
# 内存消耗：15 MB, 在所有 Python3 提交中击败了35.89%的用户        
# =============================================================================
        if n == 1:
            return 1
        
        ugly = [1]
        
        for k in range(1,n):
            a_tmp = ugly[k-1]//2
            for j in range(len(ugly)):
                if ugly[j] > a_tmp:
                    a_tmp = ugly[j]
                    break

            b_tmp = ugly[k-1]//3
            for j in range(len(ugly)):
                if ugly[j] > b_tmp:
                    b_tmp = ugly[j]                
                    break

            c_tmp = ugly[k-1]//5
            for j in range(len(ugly)):
                if ugly[j] > c_tmp:
                    c_tmp = ugly[j]                                    
                    break
                
            # print(k, a_tmp, b_tmp, c_tmp)
            ugly.append(min(2*a_tmp, 3*b_tmp, 5*c_tmp))                     
                            
        return ugly[-1]
            
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()
    
    tStart = time.time()        
    print(sln.nthUglyNumber(10))        
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    print(sln.nthUglyNumber(11))        
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
    
    tStart = time.time()        
    print(sln.nthUglyNumber(19))        
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    
    
    tStart = time.time()        
    print(sln.nthUglyNumber(1700))        
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')        