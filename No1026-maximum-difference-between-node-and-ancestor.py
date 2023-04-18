# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:24:32 2023

@author: chenxy

1026. Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 10**5
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
import bisect

from utils.BinaryTree import BinaryTree, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root: TreeNode, vMax: int, vMin: int) -> int:
            nonlocal res
            if not root: return
            vMax, vMin = max(vMax, root.val), min(vMin, root.val)
            res = max(res, vMax - vMin)
            dfs(root.left, vMax, vMin)
            dfs(root.right, vMax, vMin)

        dfs(root, root.val, root.val)
        return res
        
if __name__ == '__main__':

    sln  = Solution()                
    
    root = [8,3,10,1,6,None,14,None,None,4,7,13]
    bt = BinaryTree(root)
    print(sln.maxAncestorDiff(bt.root))

    root = [1,None,2,None,0,3]
    bt = BinaryTree(root)
    print(sln.maxAncestorDiff(bt.root))    