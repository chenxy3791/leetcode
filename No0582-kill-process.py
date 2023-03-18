# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 08:38:39 2023

@author: chenxy
582. 杀掉进程
系统中存在 n 个进程，形成一个有根树结构。给你两个整数数组 pid 和 ppid ，其中 pid[i] 是第 i 个进程的 ID ，ppid[i] 是第 i 个进程的父进程 ID 。
每一个进程只有 一个父进程 ，但是可能会有 一个或者多个子进程 。只有一个进程的 ppid[i] = 0 ，意味着这个进程 没有父进程 。
当一个进程 被杀掉 的时候，它所有的子进程和后代进程都要被杀掉。
给你一个整数 kill 表示要杀掉​​进程的 ID ，返回杀掉的所有进程 ID 的列表。可以按 任意顺序 返回答案。

示例 1：

输入：pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
输出：[5,10]
解释：涂为红色的进程是应该被杀掉的进程。
示例 2：

输入：pid = [1], ppid = [0], kill = 1
输出：[1]
 
提示：

n == pid.length
n == ppid.length
1 <= n <= 5 * 10**4
1 <= pid[i] <= 5 * 10**4
0 <= ppid[i] <= 5 * 10**4
仅有一个进程没有父进程
pid 中的所有值 互不相同
题目数据保证 kill 在 pid 中
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
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        '''
        执行用时：4316 ms, 在所有 Python3 提交中击败了5.97%的用户
        内存消耗：26.1 MB, 在所有 Python3 提交中击败了40.30%的用户
        '''
        visited = len(pid) * [0]
        inv_pid = dict()
        for k in range(len(pid)):
            inv_pid[pid[k]] = k
        # print(inv_pid)
        rslt = []
        for k in range(len(pid)):
            if visited[k] == 1:
                pass
            # search up to root or kill
            curPtr  = k
            # curnode = pid[]
            curlist = []
            while True:
                # print('curPtr = ', curPtr)
                visited[curPtr] = 1
                curlist.append(pid[curPtr])
                if ppid[curPtr] == 0: 
                    # print('root found, curPtr = {0}, curNode = {1}'.format(curPtr,pid[curPtr]))
                    break
                elif ppid[curPtr] == kill:                    
                    rslt = rslt + curlist
                    # print('kill found, curPtr = {0}, curNode = {1}, rslt = {2}'.format(curPtr,pid[curPtr],rslt))
                    break
                else:
                    curPtr = inv_pid[ppid[curPtr]]
        rslt.append(kill)
        return list(set(rslt))
                
if __name__ == '__main__':

    sln  = Solution()                
    
    pid = [1,3,10,5]
    ppid = [3,0,5,3]
    kill = 5
    print(sln.killProcess(pid,ppid,kill))
    
    pid = [1]
    ppid = [0]
    kill = 1
    print(sln.killProcess(pid,ppid,kill))
    