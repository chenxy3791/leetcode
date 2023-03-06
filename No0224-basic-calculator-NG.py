# -*- coding: utf-8 -*-
"""
Spyder Editor

224. 基本计算器
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

"""

# Definition for singly-linked list.
class Solution:
    
    def calculateSimple(self, cLst) -> int:
        #print('calculateSimple(): ', cLst)#
        state = 'IDLE'
        nxtState = 'IDLE'        
        opLst= []
        for k in range(len(cLst)):
            #print('k = ', k, ' cLst[k] = ', cLst[k], ' nxtState = ', nxtState)
            if cLst[k] == ' ':
                #print('Skip the space')
                continue
            
            state = nxtState
            if state == 'IDLE':
                nxtState = 'OP1'
                opLst.append(int(cLst[k]))
            elif state == 'OP1':
                nxtState = 'OPCODE'
                opLst.append(cLst[k])
            elif state == 'OPCODE':
                nxtState = 'OP1'
                # Make the calculation
                oprand2 = int(cLst[k])
                opcode  = opLst.pop()
                oprand1 = opLst.pop()
                if opcode == '+':
                    num = oprand1 + oprand2
                else:
                    num = oprand1 - oprand2
                opLst.append(num)
        #print(opLst, len(opLst))                
        assert(len(opLst) == 1)
        return opLst[0]               
                                            
    def calculate(self, s: str) -> int:
        lstStack = []
        for k in range(len(s)):
            #print('k = ', k, ' s[k] = ', s[k], ' lstStack = ', lstStack)
            if s[k] == ' ':
                #print('Skip the space')
                continue
            
            if s[k] != ')':
                lstStack.append(s[k])
            else:
                for k in range(len(lstStack)-1,-1,-1):
                    if lstStack[k] == '(':
                        break
                rslt = self.calculateSimple(lstStack[k+1:])
                lstStack = lstStack[0:k]
                lstStack.append(str(rslt))                
                        
        rslt = self.calculateSimple(lstStack)
                    
        return rslt
                        
if __name__ == '__main__':        
    #import time
    sln = Solution()

    s = ['1', '+', '1']
    print(s, ' = ', sln.calculateSimple(s))

    s = "1"
    print(s, ' = ', sln.calculate(s))
    
    s = "1 + 1"
    #print(s, ' = ', sln.calculateSimple(s))
    print(s, ' = ', sln.calculate(s))
    
    s = " 2-1 + 2 "
    #print(s, ' = ', sln.calculateSimple(s))
    print(s, ' = ', sln.calculate(s))
                
    s = "(1+(4+5+2)-3)+(6+8)"
    print(s, ' = ', sln.calculate(s))

    s = "( (1+(4+5+2)-3)+(6+8) + (1+(4+5+2)-3) )"
    print(s, ' = ', sln.calculate(s))
    
    s = ["2147483647"]
    print(s, ' = ', sln.calculateSimple(s))    

    s = "2147483647"
    print(s, ' = ', sln.calculate(s))        