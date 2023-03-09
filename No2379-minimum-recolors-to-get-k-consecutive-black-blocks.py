# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 08:20:29 2023

@author: chenxy

2379. 得到 K 个黑块的最少涂色次数
给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。

给你一个整数 k ，表示想要 连续 黑色块的数目。

每一次操作中，你可以选择一个白色块将它 涂成 黑色块。

请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。

 

示例 1：

输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。
示例 2：

输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。
 

提示：

n == blocks.length
1 <= n <= 100
blocks[i] 要么是 'W' ，要么是 'B' 。
1 <= k <= n

2023-03-09
执行用时：40 ms, 在所有 Python3 提交中击败了51.63%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了26.09%的用户
通过测试用例：122 / 122

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
    def minimumRecolors(self, blocks: str, k: int) -> int:                
        if k > len(blocks):
            return 0        
        cur_W2B = blocks[:k].count('W')
        min_W2B = cur_W2B
        for j in range(1,len(blocks)-k+1):
            # print(j, blocks[j:j+k])            
            if blocks[j-1] == 'W':
                cur_W2B = cur_W2B - 1
            if blocks[j+k-1] == 'W':
                cur_W2B = cur_W2B + 1
            
            min_W2B = min(min_W2B, cur_W2B)
            if min_W2B == 0: # early stop
                break
        
        return min_W2B
        
if __name__ == '__main__':

    sln  = Solution()                
    
    blocks = "WBBWWBBWBW"
    k      = 7
    print(sln.minimumRecolors(blocks,k))        
    
    blocks = "WBWBBBW"
    k      = 2
    print(sln.minimumRecolors(blocks,k))        
    
    blocks = "WBBWWBBWBWBBBBBBB"
    k      = 7
    print(sln.minimumRecolors(blocks,k))        