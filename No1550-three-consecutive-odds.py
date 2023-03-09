# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:11:31 2023

@author: chenxy

1550. 存在连续三个奇数的数组
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。
示例 2：

输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。
 

提示：

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

2023-03-09
执行用时：40 ms, 在所有 Python3 提交中击败了40.12%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了79.64%的用户
通过测试用例：32 / 32

执行用时：36 ms, 在所有 Python3 提交中击败了65.87%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了70.66%的用户
通过测试用例：32 / 32

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
    # def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    #     k = 0
    #     while k < (len(arr)-2):
    #         if (arr[k] % 2) == 1:
    #             if (arr[k+1] % 2) == 1:
    #                 if (arr[k+2] % 2) == 1:
    #                     return True
    #                 else:
    #                     k = k + 3
    #             else:
    #                 k = k + 2
    #         else:
    #             k = k + 1
    #     return False

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        k = 0
        while k < (len(arr)-2):
            if (arr[k] & 1) == 1:
                if (arr[k+1]  & 1) == 1:
                    if (arr[k+2]  & 1) == 1:
                        return True
                    else:
                        k = k + 3
                else:
                    k = k + 2
            else:
                k = k + 1
        return False
                    
if __name__ == '__main__':

    sln  = Solution()                
    
    arr = [2,6,4,1]
    print(sln.threeConsecutiveOdds(arr))     
    
    arr = [1,2,34,3,4,5,7,23,12]
    print(sln.threeConsecutiveOdds(arr))         
    
    arr = [1,2,34,3,4,5,8,23,12,11,13,15]
    print(sln.threeConsecutiveOdds(arr))         