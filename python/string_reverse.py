# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:19:27 2021

@author: chenxy
"""

import timeit
from statistics import mean
    
def rev_str_thru_slicing(aStr):
    '''
    Python中的string slicing的语法如下：string[start:stop:step]
    省略start和stop的设置，step置为’-1’的话就可以得到原字符串的一个逆序的副本。
    '''
    return aStr[::-1]

def rev_str_thru_join_revd(aStr):
    '''
    内置的函数reversed()对字符串进行逆序处理，但是它不是直接返回原字符串的逆序副本，
    而是生成一个iterator。可以用”join()”操作符对这个iterator作进一步的处理以生成字符串逆序副本。
    '''
    return "".join(reversed(aStr))	

def rev_str_thru_list_reverse(aStr):
    '''
    Python中的List有reverse() method，所以可以按以下步骤实现字符串逆序：
    (1)	将字符串转换为字符列表
    (2)	对字符列表进行逆序处理
    (3)	将逆序字符列表再变换回字符串
    '''
    lst = list(aStr)
    lst.reverse()
    return(''.join(lst))

def rev_str_thru_recursion(aStr):
    '''
    最后还有一种超级费力的方式，就是用递归函数调用的方式（只有秀编程技巧的价值）。
    '''
    if len(aStr) == 0:
        return aStr
    else:
        return rev_str_thru_recursion(aStr[1:]) + aStr[0]

if __name__ == '__main__':
    
    #1. Decreasing slicing
    print('Decreasing slicing:   ','HelloPython'[::-1])
    
    #2. User-defined function based on decreasing slicing
    myStr = "HelloPython"
    print('User-defined function based on:   ',rev_str_thru_slicing(myStr))    

    #3. Using reversed() function
    print('Using reversed() function:    ',rev_str_thru_join_revd(myStr))	
    
    #4. Using list reverse() method
    print('Using list reverse() method:    ',rev_str_thru_list_reverse(myStr))
    
    #4. Using recursive function    
    print('Using recursive function:    ',rev_str_thru_recursion(myStr))
    
    # Performance comparison
    s = myStr * 10
    repeatCount = 10

    SLICING_PERF = timeit.repeat(lambda: rev_str_thru_slicing(s), repeat=repeatCount)
    print(min(SLICING_PERF), mean(SLICING_PERF), max(SLICING_PERF), SLICING_PERF)

    J_R_PERF = timeit.repeat(lambda: rev_str_thru_join_revd(s), repeat=repeatCount)
    print(min(J_R_PERF), mean(J_R_PERF), max(J_R_PERF), J_R_PERF)

    LIST_PERF = timeit.repeat(lambda: rev_str_thru_list_reverse(s), repeat=repeatCount)
    print(min(LIST_PERF), mean(LIST_PERF), max(LIST_PERF), LIST_PERF)

    RECUR_PERF = timeit.repeat(lambda: rev_str_thru_recursion(s), repeat=repeatCount)
    print(min(RECUR_PERF), mean(RECUR_PERF), max(RECUR_PERF), RECUR_PERF)    
    
    ratio0 = mean(SLICING_PERF)/mean(SLICING_PERF)
    ratio1 = mean(J_R_PERF)/mean(SLICING_PERF)
    ratio2 = mean(LIST_PERF)/mean(SLICING_PERF)
    ratio3 = mean(RECUR_PERF)/mean(SLICING_PERF)
    print('SLICING_PERF:J_R_PERF:LIST_PERF:RECUR_PERF = {0}:{1}:{2}:{3}'.format(ratio0,ratio1,ratio2,ratio3))
    
    
    '''
    In this section, we’ll perform a simple comparison between these four defined methods to identify their efficiency. We’ll analyze the performance using a Python module called “timeit”. It provides the time taken for the execution of the code snippets. “repeat” option of the “timeit” module helps to repeat the code execution one million times. We can comprehend the output as an average time taken by executing the code snippet one million times.
    最后，基于python的timeit模块对以上几种字符串逆序处理方法进行一个统计意义上的性能对比。
    Timeit的repeat选项用于对代码进行重复执行，然后可以对运行所耗费的时间进行统计平均以得到平均执行时间。
    Repeat的单位是1百万次，即repeat设为1时待评估的对象代码会被重复执行1百万次。

    '''