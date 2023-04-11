# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:45:02 2022

@author: Dell
"""
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = (max(nums)+1) * [0]
        for num in nums:
            total[num] = total[num] + num

        N = len(total)
        memo = dict()
        def dp(k):
            if k in memo:
                return memo[k]
            if k>(N-1):
                return 0
            ans = max(total[k]+dp(k+2), dp(k+1))
            memo[k] = ans
            return ans
        return dp(0)
        
        
# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
        
#         d = dict()
#         for k,num in enumerate(nums):
#             if num in d:
#                 d[num] = d[num] + num
#             else:
#                 d[num] = num
                
#         memo = dict()
#         def dp(d0):
#             if len(d0)==0:
#                 return 0
#             if len(d0)==1:
#                 return d0.popitem()[1]
#             if tuple(d0.keys()) in memo:
#                 return memo[tuple(d0.keys())]
#             # print(d0)
            
#             d1 = d0.copy()
#             d2 = d0.copy()
#             k0,v0 = d1.popitem()           
#             # Don't take this key
#             # print(k0,v0,d1)
#             v1 = dp(d1)

#             # Take this key, and hence remove k0+/-1
#             neibourKey = []
#             d2.pop(k0)
#             for key2 in d2:
#                 if key2 == k0+1 or key2 == k0-1:
#                     neibourKey.append(key2)
#             for key in neibourKey:
#                 # print(key)
#                 d2.pop(key)
#             # print(d2)
#             v2 = v0 + dp(d2)
            
#             ans = max(v1,v2)
#             memo[tuple(d0.keys())] = ans
#             return ans
        
#         return dp(d)

if __name__ == "__main__":
    
    sln = Solution()    
    
    nums = [3,1]
    print(sln.deleteAndEarn(nums))         
    
    nums = [3,4,2]
    print(sln.deleteAndEarn(nums))               
    
    nums = [2,2,3,3,3,4]
    print(sln.deleteAndEarn(nums))