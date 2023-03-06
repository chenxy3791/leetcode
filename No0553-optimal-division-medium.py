# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:09:04 2022

@author: chenxy

553. 最优除法

给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。
但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，
才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。

示例：

输入: [1000,100,10,2]
输出: "1000/(100/10/2)"
解释:
1000/(100/10/2) = 1000/((100/10)/2) = 200
但是，以下加粗的括号 "1000/((100/10)/2)" 是冗余的，
因为他们并不影响操作的优先级，所以你需要返回 "1000/(100/10/2)"。

其他用例:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

说明:
输入数组的长度在 [1, 10] 之间。
数组中每个元素的大小都在 [2, 1000] 之间。
每个测试用例只有一个最优除法解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
import random
from collections import deque
from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        
        max_memo = dict()
        min_memo = dict()

        def dp_min(start,end): # Not including end
            #print('dp_min:', start, end)
            if (start,end) in min_memo:
                return min_memo[(start,end)]
            if end == start+1:
                return nums[start], str(nums[start])
            min_v = float('inf') # because the maximun number in input is 1000
            for i in range(start+1,end):
                numerator,num_expr = dp_min(start,i)
                denominator,deno_expr = dp_max(i,end)
                tmp = numerator/denominator # No need of the judge of "denominator == 0", because each number is in [2,1000]
                if min_v > tmp:
                    min_v = tmp
                    min_expr = '('+ num_expr +')' + '/' + '('+ deno_expr +')'
                min_memo[(start,end)] = (min_v,min_expr)
            return min_v, min_expr
        
        def dp_max(start,end): # Not including end
            #print('dp_max:', start, end)
            if (start,end) in max_memo:
                return max_memo[(start,end)]
            if end == start+1:
                return nums[start], str(nums[start])
            max_v = 0
            for i in range(start+1,end):
                numerator, num_expr    = dp_max(start,i)
                denominator, deno_expr = dp_min(i,end)
                tmp = numerator/denominator
                if max_v < tmp:
                    max_v = tmp
                    max_expr = '('+ num_expr +')' + '/' + '('+ deno_expr +')'
                max_memo[(start,end)] = (max_v,max_expr)
            return max_v,max_expr
        
        max_v,max_expr = dp_max(0,len(nums))
        # print(max_v, max_expr)        
        # Remove the redundancy
        s = deque()
        for k in range(len(max_expr)):
            # print(s)
            c = max_expr[k]
            if c != ')':
                s.append(c)
            else:
                tmp = [c]
                while 1:
                    d = s.pop()
                    tmp.insert(0,d)
                    if d == '(':
                        tmp = ''.join(tmp)                        
                        # print(tmp)
                        if tmp[1:-1].isnumeric():
                            s.append(tmp[1:-1])                            
                        elif k<len(max_expr)-1 and max_expr[k+1]=='/':
                            s.append(tmp[1:-1])
                        else:
                            s.append(tmp)                            
                        break
        final_expr = []
        while len(s) > 0:            
            final_expr.insert(0,s.pop())
        return ''.join(final_expr)

if __name__ == '__main__':        
    
    sln = Solution()    

    # nums = [2]
    # tStart = time.time()        
    # print(nums, ' -> ', sln.optimalDivision(nums))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')    

    # nums = [10,2]
    # tStart = time.time()        
    # print(nums, ' -> ', sln.optimalDivision(nums))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')    

    # nums = [100,10,2]
    # tStart = time.time()        
    # print(nums, ' -> ', sln.optimalDivision(nums))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')    
        
    nums = [1000,100,10,2]
    tStart = time.time()        
    print(nums, ' -> ', sln.optimalDivision(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    nums = [123,5,100,20]
    tStart = time.time()        
    print(nums, ' -> ', sln.optimalDivision(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    
    
    # nums = [random.randint(2, 1001) for _ in range(10)]
    # tStart = time.time()        
    # print(nums, ' -> ', sln.optimalDivision(nums))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')        