# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:28:51 2023

@author: chenxy
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。

 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
示例 3：

输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。

执行用时：48 ms, 在所有 Python3 提交中击败了59.36%的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了53.85%的用户
 
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: 
            return False
        s = deque()
        s.append((root, root.val))
        while len(s) == 0:
            node, pathsum = s.pop()
            # left child
            if node.left:
                left_pathsum = pathsum + node.left.val
                if left_pathsum == targetSum:
                    return True
                s.append(node.left)
            # right child
            if node.right:
                right_pathsum = pathsum + node.right.val
                if right_pathsum == targetSum:
                    return True
                s.append(node.right)
        return False
        
if __name__ == '__main__':

    sln  = Solution()                
    
    t = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    # Need convert the list-representation into a real tree and assign root
    
    targetSum = 22
    print(sln.pathSum(root,targetSum))