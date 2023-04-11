# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 06:58:52 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
        
#         q = deque([0])
#         ans = []
#         while len(q)>0:
#             x = q.pop()
#             ans.append(x)
#             # for k in range(10):
#             for k in range(9,-1,-1):
#                 y = 10*x+k
#                 if 0 < y <= n:
#                     q.append(y)
#         return ans[1:]

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/lexicographical-numbers/solution/zi-dian-xu-pai-shu-by-leetcode-solution-98mz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    
    sln = Solution()
    n   = 5*10**4
    tstart = time.time()
    ans = sln.lexicalOrder(n)
    tstop = time.time()
    print('n={0}, ans={1}, tcost={2:4.2f}'.format(n,ans,tstop-tstart))
    