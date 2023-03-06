# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:51:20 2021

@author: chenxy

1006. 笨阶乘
通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。

相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。

例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。

另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。

实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。

 

示例 1：

输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1
示例 2：

输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 

提示：

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  （答案保证符合 32 位整数。）

"""

class Solution:
    def clumsy(self, N: int) -> int:
        # 2021-04-01
        # 执行用时：216 ms, 在所有 Python3 提交中击败了5.43%的用户
        # 内存消耗：15.1 MB, 在所有 Python3 提交中击败了26.09%的用户        
        cnt = 0
        s   = list()
        s.append(N)
        
        while cnt < N-1:
            if cnt%4 == 0:
                op = '*'
            elif cnt%4 == 1:
                op = '//'
            elif cnt%4 == 2:
                op = '+'
            else:
                op = '-'
                
            if op == '*':
                op1 = s.pop()
                op2 = N-cnt-1
                rslt = op1 * op2
                s.append(rslt)
                cnt = cnt + 1
            elif op == '//':
                op1 = s.pop()
                op2 = N-cnt-1
                rslt = op1 // op2
                s.append(rslt)
                cnt = cnt + 1
            else:
                s.append(op)
                s.append(N-cnt-1)
                cnt = cnt + 1
        
        # Take data and operator from stack according to the order they were put in and do the calculation
        rslt = s.pop(0)
        while len(s) >= 2:
            op  = s.pop(0)
            op2 = s.pop(0)
            if op == '+':
                rslt = rslt + op2
            else:
                rslt = rslt - op2
        return rslt
            
if __name__ == '__main__':        
    #import time
    sln = Solution()

    print('1 -> ',sln.clumsy(1))    
    print('2 -> ',sln.clumsy(2))    
    print('3 -> ',sln.clumsy(3))    
    print('4 -> ',sln.clumsy(4))    
    print('5 -> ',sln.clumsy(5))    
            
            
            
                    
            