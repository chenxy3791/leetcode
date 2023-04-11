# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 07:34:32 2022

@author: Dell
"""
import time
from typing import List
from sortedcontainers import SortedList
from heapq import heappop, heappush
class Solution:

    def busiestServers1(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # s[j] = [req_cnt(已处理请求数), last_due]
        nums_task = len(arrival)
        s = [3*[0] for i in range(k)]
        for i in range(nums_task):
            for m in range(k):
                j = (m+i) % k
                if s[j][1] <= arrival[i]:
                    s[j][0] += 1
                    s[j][1]  = arrival[i] + load[i]
                    break
        maxcnt = -1
        maxidx = []
        for m in range(k):
            if maxcnt < s[m][0]:
                maxcnt = s[m][0]
                maxidx = [m]
            elif maxcnt == s[m][0]:
                maxidx.append(m)

        return maxidx

    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heappush(busy, (start + t, id))
            available.remove(id)
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]

if __name__ == '__main__':
    
    sln = Solution()
    
    k = 3
    arrival = [1,2,3,4,5]
    load = [5,2,3,3,3] 
    print(sln.busiestServers(k, arrival, load))
    
    k = 3
    arrival = [1,2,3,4]
    load = [1,2,1,2]
    print(sln.busiestServers(k, arrival, load))        
    
    k = 3
    arrival = [1,2,3]
    load = [10,12,11]
    print(sln.busiestServers(k, arrival, load))
    
    k = 3
    arrival = [1,2,3,4,8,9,10]
    load = [5,2,10,3,1,2,2]
    print(sln.busiestServers(k, arrival, load))
    
    k = 1
    arrival = [1]
    load = [1]
    print(sln.busiestServers(k, arrival, load))
    
    # execfile('No1606-testcase.py')
    with open('No1606-testcase.py','r') as f:
        exec(f.read())    
    tstart=time.time()    
    print(sln.busiestServers(k, arrival, load))
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))

    tstart=time.time()    
    print(sln.busiestServers1(k, arrival, load))
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))    