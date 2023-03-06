# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 07:32:10 2022

@author: chenxy

1601. 最多可达成的换楼请求数目
我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。
给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 toi 的楼。
一开始所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足每栋楼员工净变化为 0 。
意思是每栋楼离开的员工数目等于该楼搬入的员工数数目。
比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，
应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。
请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。

示例 1：
图1

输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
输出：5
解释：请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。

示例 2：
图2
输入：n = 3, requests = [[0,0],[1,2],[2,1]]
输出：3
解释：请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。

示例 3：
输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
输出：4
 
提示：
1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import sys
import time
import random
import collections
import itertools as it
from   typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def judge(requests):
            d = n*[0]
            for req in requests:
                d[req[0]] -= 1
                d[req[1]] += 1                
            return min(d)==0 and max(d)==0
        
        for k in range(len(requests),0,-1):
            # print(k)
            for reqs in it.combinations(requests, k):        
                # print(reqs)
                if judge(reqs):
                    return k
        return 0
            
if __name__ == '__main__':        
            
    sln = Solution()

    # n    = 1
    # reqs = [[0,0]]
    # tStart = time.time()        
    # print('reqs=',reqs,' ans=', sln.maximumRequests(n,reqs))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')   

    n = 3
    reqs = [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]
    tStart = time.time()        
    print('reqs=',reqs,' ans=', sln.maximumRequests(n,reqs))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')   
    
    n    = 5
    reqs = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    tStart = time.time()        
    print('reqs=',reqs,' ans=', sln.maximumRequests(n,reqs))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')   

    n    = 3
    reqs = [[0,0],[1,2],[2,1]]
    tStart = time.time()        
    print('reqs=',reqs,' ans=', sln.maximumRequests(n,reqs))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')       
    
    n    = 4
    reqs = [[0,3],[3,1],[1,2],[2,0]]
    tStart = time.time()        
    print('reqs=',reqs,' ans=', sln.maximumRequests(n,reqs))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')     
    
    n    = 20
    reqs = []
    for k in range(16):
        tmp = [random.randint(0,n-1),random.randint(0,n-1)]
        reqs.append(tmp)
    tStart = time.time()        
    print('reqs=',reqs,' ans=', sln.maximumRequests(n,reqs))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')         