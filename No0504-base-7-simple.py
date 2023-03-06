# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 07:48:17 2022

@author: chenxy

504. 七进制数
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:
输入: num = 100
输出: "202"

示例 2:

输入: num = -7
输出: "-10"
 
提示：-10^7 <= num <= 10^7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/base-7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = []
        sign = 1 if num >= 0 else -1
        num  = sign * num
        
        while num >= 7:
            # print(base7,num)
            base7.append(str(num%7))
            num = num // 7
        base7.append(str(num))
        if sign == -1:
            base7.append('-')
        # print(base7)
        return ''.join(base7[::-1])

if __name__ == '__main__':            
    sln = Solution()
    
    num = 100
    print('num = {0}, ans = {1}'.format(num, sln.convertToBase7(num)))

    num = -7
    print('num = {0}, ans = {1}'.format(num, sln.convertToBase7(num)))    
    
    num = 0
    print('num = {0}, ans = {1}'.format(num, sln.convertToBase7(num)))        
    
    num = random.randint(0,10**7)
    print('num = {0}, ans = {1}'.format(num, sln.convertToBase7(num)))        