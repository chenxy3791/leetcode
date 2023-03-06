# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:59:53 2021

@author: chenxy

7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0
 
提示：-2^31 <= x <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def reverse_1(self, x: int) -> int:
        if(abs(x) < 10):            
            return x

        xsign = 1
        if x < 0:
            xsign = -1
        
        xabs = abs(x)

        ret = 0

        while xabs > 0:
            ret = ret*10 + xabs%10
            xabs = xabs // 10
        
        # Note, ret represent absolute value at this point!
        if ret > (2**31-1):
            ret = 0
        
        return ret * xsign

    def reverse(self, x: int) -> int:
        # One-digit integer doesn't need reverse
        if(abs(x) < 10):            
            return x

        x_str = str(x)
        if x_str[0] == '-':
            rev_str = ''.join(['-',x_str[1:][::-1]])
        else:
            rev_str = x_str[::-1]
        ret = int(rev_str)
        
        if ret > (2**31-1) or ret < -2**31:
            ret = 0
        
        return ret
        
if __name__ == '__main__':        
            
    sln = Solution()

    x = 123    
    print(x, ' -> ', sln.reverse(x))            

    x = -123    
    print(x, ' -> ', sln.reverse(x))                

    x = 120    
    print(x, ' -> ', sln.reverse(x))                
    
    x = 0    
    print(x, ' -> ', sln.reverse(x))                    

    x = 1    
    print(x, ' -> ', sln.reverse(x))                    

    x = -1    
    print(x, ' -> ', sln.reverse(x))                    

    x = 2**31 - 1    
    print(x, ' -> ', sln.reverse(x))                    
    
    x = -(2**31 - 1)    
    print(x, ' -> ', sln.reverse(x))                        
    
    x = 1534236469
    print(x, ' -> ', sln.reverse(x))                        