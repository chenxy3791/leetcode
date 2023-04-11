# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 06:02:14 2022

@author: Dell
"""
from typing import List
import random

# class Solution:
#     def __init__(self, nums: List[int]):
#         self.d = dict()
#         for k,num in enumerate(nums):
#             if num in self.d:
#                 self.d[num].append(k)
#             else:
#                 self.d[num] = [k]

#     def pick(self, target: int) -> int:
#         return random.choice(self.d[target])        

# Using defaultdict is slower than dict()?
# from collections import defaultdict
# class Solution:
#     def __init__(self, nums: List[int]):
#         self.d = defaultdict(list)
#         for k,num in enumerate(nums):
#                 self.d[num].append(k)

#     def pick(self, target: int) -> int:
#         return random.choice(self.d[target])    

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if random.randrange(cnt) == 0:
                    ans = i
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

if __name__ == "__main__":
    
    nums = [1,2,3,3,3]
    sln = Solution(nums)
    print(sln.pick(1))
    print(sln.pick(2))
    for k in range(10):
        print(sln.pick(3))