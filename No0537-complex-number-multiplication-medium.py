# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 07:36:27 2022

@author: chenxy

537. 复数乘法
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
实部 是一个整数，取值范围是 [-100, 100]
虚部 也是一个整数，取值范围是 [-100, 100]
i^2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。

示例 1：
输入：num1 = "1+1i", num2 = "1+1i"
输出："0+2i"
解释：(1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

示例 2：
输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i^2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 

提示：
num1 和 num2 都是有效的复数表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/complex-number-multiplication
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_sep = num1.split('+')
        real1 = int(num1_sep[0])
        imag1 = int(num1_sep[1][:-1])
        
        num2_sep = num2.split('+')
        real2 = int(num2_sep[0])
        imag2 = int(num2_sep[1][:-1])        
        
        ans_real = real1 * real2 - imag1 * imag2
        ans_imag = real1 * imag2 + imag1 * real2
        print(ans_real, ans_imag, str(ans_real), str(ans_imag).join('i'))        
        ans = ''.join([str(ans_real), '+', str(ans_imag), 'i'])
        
        return ans

    # Official solution
    def complexNumberMultiply2(self, num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i'


if __name__ == '__main__':        
    
    sln = Solution()    
    
    num1 = "1+1i"
    num2 = "1+1i"
    print('num1={0}, num2={1}, num1*num2={2}'.format(num1,num2, sln.complexNumberMultiply(num1,num2)))

    num1 = "1+-1i"
    num2 = "1+-1i"          
    print('num1={0}, num2={1}, num1*num2={2}'.format(num1,num2, sln.complexNumberMultiply(num1,num2)))
    
    num1 = "0+-1i"
    num2 = "1+0i"          
    print('num1={0}, num2={1}, num1*num2={2}'.format(num1,num2, sln.complexNumberMultiply(num1,num2)))