# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 07:32:36 2022

@author: chenxy

258. 各位相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

示例 1:
输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。

示例 2:
输入: num = 0
输出: 0
 
提示：0 <= num <= 2**31 - 1
 
进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
class Solution:
    def addDigits(self, num: int) -> int:
        # print('addDigits({0})'.format(num))
        if num < 10:
            return num
        else:
            digitsum = 0
            while num > 0:
                digitsum += num%10
                num = num // 10
            if digitsum < 10:
                return digitsum
            else:
                return self.addDigits(digitsum)

    def addDigits1(self, num: int) -> int:
        return num % 9

if __name__ == '__main__':        
    
    sln = Solution()  

    num = 38
    tStart = time.time()        
    ans = sln.addDigits(num)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(num,ans,tElapsed))

    num = 251
    tStart = time.time()        
    ans = sln.addDigits(num)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(num,ans,tElapsed))                
    
    num = 2**31-1
    tStart = time.time()        
    ans = sln.addDigits(num)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(num,ans,tElapsed))             

    print(sln.addDigits1(38))       
    print(sln.addDigits1(251))       
    print(sln.addDigits1(2**31-1))       