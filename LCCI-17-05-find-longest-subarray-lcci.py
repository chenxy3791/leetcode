# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:13:55 2023

@author: chenxy

面试题 17.05.  字母与数字
给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

示例 1:

输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]

输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
示例 2:

输入: ["A","A"]

输出: []
提示：array.length <= 100000

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
    def findLongestSubarray(self, array: List[str]) -> List[str]:

if __name__ == '__main__':

    sln  = Solution()                
    
    array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    print(sln.findLongestSubarray(array))
    
    