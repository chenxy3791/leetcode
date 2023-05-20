# -*- coding: utf-8 -*-
"""
Created on Sat May 20 08:34:43 2023

@author: chenxy

1373. Maximum Sum BST in Binary Tree
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
Input: root = [4,3,None,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 
Constraints:

The number of nodes in the tree is in the range [1, 4 * 10**4].
-4 * 10**4 <= Node.val <= 4 * 10**4


brute-force:
    if root is BST:
        return sum of all nodes
    else:
        return max(maxSumBST(root.left),maxSumBST(root.right))            
keypoint: BST judge
problem:  may cause too deep resursion tree.

"""
import time
import random
from typing import List, Optional	
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
import bisect
import sys
from utils.BinaryTree import TreeNode, BinaryTree
from functools import reduce
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxSumBST(self, root: Optional[TreeNode]) -> int:
#         '''
#         vals中存储以该节点为二叉搜索树根节点时，该子树值的大小
#         若该节点不构成二叉搜索树，则置为-inf
#         '''

#         vals = defaultdict(int)
#         # mx, mn 分别存储该节点及其子树的最大值,最小值,用于判断是否二叉树
#         mx = defaultdict(lambda: -inf)
#         mn = defaultdict(lambda: inf)
#         def dfs(node: Optional[TreeNode]) -> None:
#             if node.left: dfs(node.left)
#             if node.right: dfs(node.right)

#             # 左右节点均有
#             if node.left and node.right:
#                 if mx[node.left] < node.val < mn[node.right]:
#                     vals[node] += vals[node.left] + vals[node.right]
#                 else:
#                     vals[node] = -inf
#             # 只有左节点
#             elif node.left and (not node.right):
#                 if mx[node.left] < node.val:
#                     vals[node] += vals[node.left]
#                 else:
#                     vals[node] = -inf
#             # 只有右节点
#             elif node.right and (not node.left):
#                 if mn[node.right] > node.val:
#                     vals[node] += vals[node.right]
#                 else:
#                     vals[node] = -inf
#             # 维护数据值
#             mx[node] = max(mx[node.left], mx[node.right], node.val)
#             mn[node] = min(mn[node.left], mn[node.right], node.val)
#             vals[node] += node.val

#         dfs(root)

#         return max(max(vals.values()), 0)        

class SubTree:
    def __init__(self, is_bst, min_value, max_value, sum_value):
        self.is_bst = is_bst
        self.min_value = min_value
        self.max_value = max_value
        self.sum_value = sum_value

class Solution:
    INF = 0x3f3f3f3f

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return SubTree(True, self.INF, -self.INF, 0)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left.is_bst and right.is_bst and root.val > left.max_value and root.val < right.min_value:
            sum = root.val + left.sum_value + right.sum_value
            self.res = max(self.res, sum)
            return SubTree(True, min(left.min_value, root.val), max(root.val, right.max_value), sum)
        else:
            return SubTree(False, 0, 0, 0)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/solution/er-cha-sou-suo-zi-shu-de-zui-da-jian-zhi-lii4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
if __name__ == '__main__':

    sln  = Solution()                
    
    data = [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
    xBT = BinaryTree(data)    
    print(sln.maxSumBST(xBT.root))           
    
    data = [4,3,None,1,2]
    xBT = BinaryTree(data)    
    print(sln.maxSumBST(xBT.root))           
    
    data = [-4,-2,-5]
    xBT = BinaryTree(data)    
    print(sln.maxSumBST(xBT.root))           