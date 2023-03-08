# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 08:25:19 2023

@author: chenxy

673. 最长递增子序列的个数
给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。

注意 这个数列必须是 严格 递增的。

 

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
 

提示: 

1 <= nums.length <= 2000
-10**6 <= nums[i] <= 10**6

"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        

if __name__ == '__main__':

    sln  = Solution()                
    
    # s = "aababbab"
    # print(sln.minimumDeletions(s))
    
    # s = "bbaaaaabb"
    # print(sln.minimumDeletions(s))
    
    # s = "b"
    # print(sln.minimumDeletions(s))
    
    # s = "babbabbbabbbbabbbbba"
    # print(sln.minimumDeletions(s))
    
    # #open text file in read mode
    # fptr = open("No1653_testdata.txt", "r")
    # #read whole file to a string
    # s = fptr.read()     
    # #close file
    # fptr.close()     
    # print(s, len(s))
    # tStart= time.time()
    # # print(sln.minimumDeletions(s[:5000]))    
    # print(sln.minimumDeletions(s))    
    # tStop= time.time()
    # print("Time cost is {0}".format(tStop-tStart))            