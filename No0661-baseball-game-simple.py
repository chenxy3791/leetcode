# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 08:37:49 2022

@author: Dell
"""
from typing import List
 
class Solution:
    def calPoints1(self, ops: List[str]) -> int:
        # The first round for 'C' processing
        wptr = 0
        for op in ops:
            if op != 'C':
                ops[wptr] = op
                wptr += 1
            else:
                wptr -= 1
        # print(ops[:wptr])
        
        # The second round
        sum = 0
        for k in range(wptr):
            if ops[k] == '+':
                ops[k] = ops[k-1] + ops[k-2]                
            elif ops[k] == 'D':
                ops[k] = 2 * ops[k-1]
            else:
                ops[k] = int(ops[k])
            sum += ops[k]
        return sum

    def calPoints2(self, ops: List[str]) -> int:
        sum = 0
        k   = 0 
        for j in range(len(ops)):
            # print('j = ',j,k,ops)
            if ops[j] == '+':
                ops[k] = ops[k-1] + ops[k-2]                
                sum   += ops[k]
                k     += 1
            elif ops[j] == 'D':
                ops[k] = 2 * ops[k-1]
                sum   += ops[k]
                k     += 1
            elif ops[j] == 'C':
                k     -= 1
                sum   -= ops[k]
            else:
                ops[k] = int(ops[j])
                sum   += ops[k]
                k     += 1
        # print(ops)
        return sum        
        
if __name__ == '__main__':
    
    sln = Solution()
    
    ops = ["1"]
    print(sln.calPoints1(ops))
    ops = ["1"]    
    print(sln.calPoints2(ops))  
    
    ops = ["5","2","C","D","+"]
    print(sln.calPoints1(ops))
    ops = ["5","2","C","D","+"]
    print(sln.calPoints2(ops))        
    
    ops = ["5","-2","4","C","D","9","+","+"]
    print(sln.calPoints1(ops))
    ops = ["5","-2","4","C","D","9","+","+"]
    print(sln.calPoints2(ops))
    
    ops = ["5","2","C","D","+","C"]
    print(sln.calPoints1(ops))     
    ops = ["5","2","C","D","+","C"]           
    print(sln.calPoints2(ops))