# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 08:36:03 2023

@author: chenxy
1012. 至少有 1 位重复的数字
给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。

示例 1：
输入：n = 20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

示例 2：
输入：n = 100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

示例 3：
输入：n = 1000
输出：262

提示：1 <= n <= 10**9
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
import bisect

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:

if __name__ == '__main__':

    sln  = Solution()                
    
    n = 20
    print(sln.numDupDigitsAtMostN(n))
    
    n = 100
    print(sln.numDupDigitsAtMostN(n))    
    
    n = 1000
    print(sln.numDupDigitsAtMostN(n))        