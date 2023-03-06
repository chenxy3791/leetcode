# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 07:23:42 2022

@author: chenxy

2055. 蜡烛之间的盘子
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

示例 1:
输入：s = "**|**|***|", queries = [[2,5],[5,9]]
输出：[2,3]
解释：
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。

示例 2:
输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
输出：[9,0,0,0,0]
解释：
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。
 
提示：
3 <= s.length <= 10^5
s 只包含字符 '*' 和 '|' 。
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= lefti <= righti < s.length

"""
import time
# import random
from typing import List	
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
# import itertools as it

class Solution:
    def platesBetweenCandles1(self, s: str, queries: List[List[int]]) -> List[int]:
        def oneQuery(begin, end):
            left,right = begin,end            
            while s[left] != "|" and left < end:
                left +=1
            while s[right] != "|" and right > begin:
                right -=1
            cnt = 0
            for k in range(left+1,right):
                if s[k]=='*':
                    cnt += 1
            return cnt
        ans = []
        for k in range(len(queries)):
            ans.append(oneQuery(queries[k][0],queries[k][1]))
        
        return ans

    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        # Pre-processing
        num_left  = dict()
        plate_cnt = 0
        ans       = []
        for k in range(len(s)):
            if s[k] == '*':
                plate_cnt += 1
            if s[k] == '|':
                num_left[k] = plate_cnt

        for k in range(len(queries)):
            left,right = queries[k][0],queries[k][1]
            while s[left] != "|" and left < queries[k][1]:
                left +=1
            while s[right] != "|" and right > queries[k][0]:
                right -=1            
            if left >= right:
                ans.append(0)
            else:
                ans.append(num_left[right] - num_left[left])
        
        return ans

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Pre-processing
        num1  = dict()
        num2  = dict()
        
        plate_cnt = 0
        prev      = -1
        plate_cnt_prev = 0
        
        for k in range(len(s)):
            if s[k] == '*':
                plate_cnt += 1
            if s[k] == '|':
                num1[k] = plate_cnt        
                num2[k] = plate_cnt                     
                for m in range(prev+1,k):
                    num1[m] = plate_cnt        
                for m in range(prev+1,k):
                    num2[m] = plate_cnt_prev        
                prev = k
                plate_cnt_prev = plate_cnt
        # special handling if the last character is not candle.
        if s[-1] != '|': 
            for m in range(prev+1,len(s)):
                num1[m] = plate_cnt        
                num2[m] = plate_cnt_prev    
                    
        # print('num1 = ',num1)
        # print('num2 = ',num2)
        ans = []
        for k in range(len(queries)):
            # print(k)
            tmp = max(0,num2[queries[k][1]]-num1[queries[k][0]])
            ans.append(tmp)
        return ans
                            
if __name__ == '__main__':            
    sln = Solution()
    
    s = "**|**|***|"
    queries = [[2,5],[5,9]]
    print('s = {0}, queries = {1}, ans = {2}'.format(s,queries, sln.platesBetweenCandles(s,queries)))        

    s = "***|**|*****|**||**|*"
    queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    print('s = {0}, queries = {1}, ans = {2}'.format(s,queries, sln.platesBetweenCandles(s,queries)))            
    

    s = "*|*||||**|||||||*||*||*||**|*|*||*"
    queries = [[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]]    
    print('s = {0}, queries = {1}, ans = {2}'.format(s,queries, sln.platesBetweenCandles(s,queries)))                