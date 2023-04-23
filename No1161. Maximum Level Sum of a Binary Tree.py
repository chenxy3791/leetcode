# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:03:56 2023

@author: Dell

1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 
Constraints:

The number of nodes in the tree is in the range [1, 10**4].
-10**5 <= Node.val <= 10**5
"""
import time
import random
from typing import List, Optional	
from collections import defaultdict
import time
import numpy as np
from math import sqrt,inf
from collections import deque
import itertools as it
import bisect
import sys
from utils.BinaryTree import TreeNode
from utils.BinaryTree import BinaryTree
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        执行用时：280 ms, 在所有 Python3 提交中击败了37.99%的用户
        内存消耗：19.8 MB, 在所有 Python3 提交中击败了28.49%的用户
        '''
        q = deque()
        q.append(tuple([root,1]))
        max_sum, max_layer, cur_layer_sum, prev_layer = float('-inf'),0,float('-inf'),0
        while len(q) > 0:
            node,layer = q.popleft()
            if layer == prev_layer + 1:
                if max_sum < cur_layer_sum:
                    # print(max_sum,cur_layer_sum,prev_layer,layer)
                    max_sum, max_layer = cur_layer_sum, prev_layer
                cur_layer_sum = 0
            cur_layer_sum += node.val
            if node.left != None:
                q.append(tuple([node.left,layer+1]))
            if node.right != None:
                q.append(tuple([node.right,layer+1]))
            prev_layer = layer
        # The last layer
        # print(max_sum,cur_layer_sum,layer)
        if max_sum < cur_layer_sum:
            max_layer = layer
        return max_layer
    
if __name__ == '__main__':        
    
    sln = Solution()    
    
    x   = [1,7,0,7,-8,None,None]
    xBST = BinaryTree(x)    
    print(sln.maxLevelSum(xBST.root))        
    
    x = [1,2,3]
    xBST = BinaryTree(x)    
    print(sln.maxLevelSum(xBST.root)) 
    
    x = [-100,-200,-300,-20,-5,-10,None]
    xBST = BinaryTree(x)    
    print(sln.maxLevelSum(xBST.root))