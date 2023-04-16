# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:24:30 2023

@author: chenxy
1157. Online Majority Element In Subarray
Design a data structure that efficiently finds the majority element of a given subarray.

The majority element of a subarray is an element that occurs threshold times or more in the subarray.

Implementing the MajorityChecker class:

MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.
 

Example 1:

Input
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
Output
[null, 1, -1, 2]

Explanation
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2
 

Constraints:

1 <= arr.length <= 2 * 10**4
1 <= arr[i] <= 2 * 10**4
0 <= left <= right < arr.length
threshold <= right - left + 1
2 * threshold > right - left + 1
At most 10**4 calls will be made to query.
"""

import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it
from bisect import bisect,bisect_right,bisect_left

# class MajorityChecker:

#     def __init__(self, arr: List[int]):
#         self.arr = arr.copy()
#         # self.prefix = defaultdict(int)
        
#     def query2(self, left: int, right: int, threshold: int) -> int:
#         count = defaultdict(int)
        
#         for k in range(left, right+1):
#             count[self.arr[k]] += 1
#             if count[self.arr[k]] >= threshold:
#                 return self.arr[k]
#         return -1

#     def query(self, left: int, right: int, threshold: int) -> int:
#         '''
#         Only applicable for the case of "2 * threshold > right - left + 1"
#         '''
#         major = count = 0
#         for k in range(left, right+1):
#             if self.arr[k] == major:
#                 count += 1
#             elif count > 0:
#                 count -= 1
#             else:
#                 major = self.arr[k]
#                 count = 1
                
#         count = 0
#         for k in range(left, right+1):
#             if self.arr[k] == major:
#                 count += 1
#         return major if count >= threshold else -1

class Node:
    def __init__(self, x: int = 0, cnt: int = 0):
        self.x = x
        self.cnt = cnt
    
    def __iadd__(self, that: "Node") -> "Node":
        if self.x == that.x:
            self.cnt += that.cnt
        elif self.cnt >= that.cnt:
            self.cnt -= that.cnt
        else:
            self.x = that.x
            self.cnt = that.cnt - self.cnt
        return self

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.loc = defaultdict(list)

        for i, val in enumerate(arr):
            self.loc[val].append(i)
        
        self.tree = [Node() for _ in range(self.n * 4)]
        self.seg_build(0, 0, self.n - 1)

    def query(self, left: int, right: int, threshold: int) -> int:
        loc_ = self.loc

        ans = Node()
        self.seg_query(0, 0, self.n - 1, left, right, ans)
        pos = loc_[ans.x]
        occ = bisect_right(pos, right) - bisect_left(pos, left)
        return ans.x if occ >= threshold else -1
    
    def seg_build(self, idx: int, l: int, r: int):
        arr_ = self.arr
        tree_ = self.tree

        if l == r:
            tree_[idx] = Node(arr_[l], 1)
            return
        
        mid = (l + r) // 2
        self.seg_build(idx * 2 + 1, l, mid)
        self.seg_build(idx * 2 + 2, mid + 1, r)
        tree_[idx] += tree_[idx * 2 + 1]
        tree_[idx] += tree_[idx * 2 + 2]

    def seg_query(self, idx: int, l: int, r: int, ql: int, qr: int, ans: Node):
        tree_ = self.tree

        if l > qr or r < ql:
            return
        
        if ql <= l and r <= qr:
            ans += tree_[idx]
            return

        mid = (l + r) // 2
        self.seg_query(idx * 2 + 1, l, mid, ql, qr, ans)
        self.seg_query(idx * 2 + 2, mid + 1, r, ql, qr, ans)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/online-majority-element-in-subarray/solution/zi-shu-zu-zhong-zhan-jue-da-duo-shu-de-y-k1we/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。                

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

if __name__ == '__main__':

    # sln  = Solution()                
    
    arr = [1, 1, 2, 2, 1, 1]
    obj = MajorityChecker(arr)
    print(obj.query(0, 5, 4))
    print(obj.query(0, 3, 3))
    print(obj.query(2, 3, 2))
    