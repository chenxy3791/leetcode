""" 
每日温度
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

"""
import math
import time
import numpy as np
from collections import deque


class Solution:
    #def dailyTemperatures(self, T: List[int]) -> List[int]:
    def dailyTemperatures(self, T):
        if len(T) == 0:
            return None
        if len(T) == 1:
            return [0]
        
        rslt    = [0 for _ in range(len(T))]
        print(rslt)

        myStack = deque()
        for k in range(len(T)):
            # Compare the stack top with T[k],
            # if T[k] is greater, pop out the stack top, record the corresponding result,
            # and then continue the comparison, till the stack becomes empty, or find that
            # the stack top is not less than T[k]
            while myStack:
                if T[k] > myStack[-1][1]:
                    a = myStack.pop()
                    rslt[a[0]] = k - a[0]
                else:            
                    break
            myStack.append((k,T[k]))

        # If myStack is empty, the result for corresponding element should be all 0
        while myStack:
            a = myStack.pop()
            rslt[a[0]] = 0
        return rslt
        
if __name__ == '__main__':


    sln   = Solution()

    print('\ntestcase1 ...')
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    
    tStart= time.time()
    print(sln.dailyTemperatures(temperatures))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    
