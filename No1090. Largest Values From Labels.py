# -*- coding: utf-8 -*-
"""
Created on Tue May 23 08:44:10 2023

@author: chenxy

1090. Largest Values From Labels
There is a set of n items. 
You are given two integer arrays values and labels where the value and the label 
of the ith element are values[i] and labels[i] respectively. 
You are also given two integers numWanted and useLimit.

Choose a subset s of the n elements such that:

The size of the subset s is less than or equal to numWanted.
There are at most useLimit items with the same label in s.
The score of a subset is the sum of the values in the subset.

Return the maximum score of a subset s.

Example 1:
Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth items.

Example 2:
Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third items.

Example 3:
Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
Output: 16
Explanation: The subset chosen is the first and fourth items.
 

Constraints:

n == values.length == labels.length
1 <= n <= 2 * 10**4
0 <= values[i], labels[i] <= 2 * 10**4
1 <= numWanted, useLimit <= n
"""
'''
要找出一个子集s，其中元素个数不大于numWanted，每个label的个数不超过useLimit
(换言之，每个label的重复使用次数不超过useLimit)
要求s的和最大化

换个说法: 
    有一筐水果，里面有苹果、香蕉、鸭梨(labels)，每个水果的重量用values数组表示； 
    允许拿总计不超过numWanted个水果，且每一类水果最多拿useLimit个； 
    请问最重可以拿走多重的水果？
排序后用一个字典维护类别计数贪心即可。

细节

由于题目中的 values 和 labels 是分成两个数组给出的，直接排序会比较困难。
可以额外开辟一个同样长度为 n 的数组，存储下标，并直接在该数组上进行排序即可。

'''

import time
import random
from typing import List, Optional	
from collections import defaultdict, Counter
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
import bisect
import sys
from utils.BinaryTree import TreeNode, binTree2Lst, lst2bintree
from functools import reduce

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        idx = list(range(n))
        idx.sort(key=lambda i: -values[i])

        ans = choose = 0
        cnt = Counter()
        for i in range(n):
            label = labels[idx[i]]
            if cnt[label] == useLimit: # 当前类别达到允许上限，不能再取，跳过
                continue;
            
            choose += 1
            ans += values[idx[i]]
            cnt[label] += 1
            if choose == numWanted: # 取完所有限额，结束
                break
        return ans
        
if __name__ == '__main__':

    sln  = Solution()                
    
    values = [5,4,3,2,1]; labels = [1,1,2,2,3]; numWanted = 3; useLimit = 1
    print(sln.largestValsFromLabels(values,labels,numWanted,useLimit))        
    
    values = [5,4,3,2,1]; labels = [1,3,3,3,2]; numWanted = 3; useLimit = 2
    print(sln.largestValsFromLabels(values,labels,numWanted,useLimit))        
    
    values = [9,8,8,7,6]; labels = [0,0,0,1,1]; numWanted = 3; useLimit = 1
    print(sln.largestValsFromLabels(values,labels,numWanted,useLimit))        