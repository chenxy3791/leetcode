# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 13:49:29 2022

@author: chenxy

2100. 适合打劫银行的日子
你和一群强盗准备打劫银行。
给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天执勤警卫的数量。
日子从 0 开始编号。同时给你一个整数 time 。
如果第 i 天满足以下所有条件，我们称它为一个适合打劫银行的日子：

第 i 天前和后都分别至少有 time 天。
第 i 天前连续 time 天警卫数目都是非递增的。
第 i 天后连续 time 天警卫数目都是非递减的。
更正式的，第 i 天是一个合适打劫银行的日子当且仅当：
security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。

示例 1：
输入：security = [5,3,3,3,5,6,2], time = 2
输出：[2,3]
解释：
第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。

示例 2：
输入：security = [1,1,1,1,1], time = 0
输出：[0,1,2,3,4]
解释：
因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。

示例 3：
输入：security = [1,2,3,4,5,6], time = 2
输出：[]
解释：
没有任何一天的前 2 天警卫数目是非递增的。
所以没有适合打劫银行的日子，返回空数组。

示例 4：
输入：security = [1], time = 5
输出：[]
解释：
没有日子前面和后面有 5 天时间。
所以没有适合打劫银行的日子，返回空数组。
 
提示：
1 <= security.length <= 10^5
0 <= security[i], time <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    def goodDaysToRobBank(self, security: List[int], t: int) -> List[int]:
        def judgeWin(win):
            for k in range(1,t+1):
                if win[k] > win[k-1]:
                    return -1, k  # -1 indicates the first error occurs in the first half
            for k in range(1,t+1):
                if win[k+t] < win[k+t-1]:
                    return -2, k  # -2 indicates the first error occurs in the second half
            return 0,0

        if t == 0:
            return [k for k in range(len(security))]
        
        ans       = []
        prevFlg   = -1
        start     = 0
        while start < len(security)-2*t:
            win = security[start:start+2*t+1]
            # print(start, win)
            if prevFlg==0:
                if win[t] == win[t-1] and win[2*t] >= win[2*t-1]:
                    ans.append(start + t)
                    start += 1
                    prevFlg  = 0
                elif win[t] != win[t-1]:
                    prevFlg  = -1
                    start    = start + t                                                        
                else:
                    prevFlg  = -2
                    start    = start + t                        
            else: 
                prevFlg, prevNgIdx = judgeWin(win)
                if prevFlg==0:
                    ans.append(start+t)
                    start += 1
                elif prevFlg==-1:
                    start += prevNgIdx
                else:
                    start += prevNgIdx
            print(prevFlg, prevNgIdx, start)                    
        return ans

class Solution:
# =============================================================================
# 执行用时：252 ms, 在所有 Python3 提交中击败了30.59%的用户
# 内存消耗：32.8 MB, 在所有 Python3 提交中击败了21.76%的用户    
# =============================================================================
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            if security[n - i - 1] <= security[n - i]:
                right[n - i - 1] = right[n - i] + 1
        return [i for i in range(time, n - time) if left[i] >= time and right[i] >= time]

                
if __name__ == '__main__':            
    sln = Solution()
    
    security = [5,3,3,3,5,6,2]
    t = 2    
    print(security,t, ' : ', sln.goodDaysToRobBank(security,t))

    security = [1,1,1,1,1]
    t = 0
    print(security,t, ' : ', sln.goodDaysToRobBank(security,t))

    security = [4,3,2,1]
    t = 1
    print(security,t, ' : ', sln.goodDaysToRobBank(security,t))

    security = [1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8]
    t = 2
    print(security,t, ' : ', sln.goodDaysToRobBank(security,t))
    
    # security = [1,2,3,4,5,6]
    # t = 2
    # print(security,t, ' : ', sln.goodDaysToRobBank(security,t))
    
    # security = [1] 
    # t = 5
    # print(security,t, ' : ', sln.goodDaysToRobBank(security,t))
    
    # security = [random.randint(0,10**3) for x in range(10**3)]  
    # # t = random.randint(0,10)
    # t = 3

    # tStart = time.time()        
    # print(security,t, ' : ', sln.goodDaysToRobBank(security,t))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')         