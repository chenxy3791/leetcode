# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:33:20 2023

@author: chenxy

1080. Insufficient Nodes in Root to Leaf Paths
Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, 
and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,None,None,7,8,9,None,14]

Example 2:
Input: root = [5,4,8,11,None,17,4,7,1,None,None,5,3], limit = 22
Output: [5,4,8,11,None,17,4,7,None,None,None,5]

Example 3:
Input: root = [1,2,-3,-5,None,4,None], limit = -1
Output: [1,None,-3,4]
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
-10**5 <= Node.val <= 10**5
-10**9 <= limit <= 10**9

"""
'''
根据题意可知「不足节点」的定义为：通过节点 node 的每种可能的「根-叶」路径上值的总和全都小于给定的 limit，
则该节点被称之为「不足节点」。
按照上述定义可知：
假设节点 node 为根的子树中所有的叶子节点均为「不足节点」，则可以推断出 node 一定也为「不足节点」，
即经过该节点所有“根-叶” 路径的总和都小于 limit，此时该节点需要删除；
假设节点 node 为根的子树中存在叶子节点不是「不足节点」，则可以推断出node 一定也不是「不足节点」，
因为此时一定存一条从根节点到叶子节点的路径和大于等于 limit，此时该节点需要保留。

根据上述的分析，我们用 checkSufficientLeaf(node) 来检测 node 节点为子树是否含有叶子节点不为「不足节点」，
每次进行深度优先搜索时并传入当前的路径和 sum，每次检测过程如下：

如果当前节点 node 为叶子节点，则当前 “根-叶” 路径和为 sum 加上 node 节点的值，如果当前的路径和小于 limit，
则该叶子 node 一定为「不足节点」，返回 false，否则该节点一定不为「不足节点」，返回 true；
依次检测 node 节点的左子树与右子树，如果当前节点 node 的左子树中的叶子节点均为「不足节点」，则左孩子需要删除，
否则需要保留；如果当前节点 node 的右子树中的叶子节点均为「不足节点」，则右孩子需要删除，否则需要保留。
如果当前子树中的所有叶子节点均为「不足节点」则当前节点需要删除，否则当前节点需要删除。
最终检测 root 的叶子节点是否均为「不足节点」，如果是则返回 null，否则返回 root。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/solution/gen-dao-xie-lu-jing-shang-de-bu-zu-jie-d-f4vz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
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
from utils.BinaryTree import TreeNode, binTree2Lst, lst2bintree
from functools import reduce

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def checkSufficientLeaf(node, sum, limit):
            if node == None:
                return False
            if node.left == None and node.right == None:
                return node.val + sum >= limit
            haveSufficientLeft = checkSufficientLeaf(node.left, sum + node.val, limit)
            haveSufficientRight = checkSufficientLeaf(node.right, sum + node.val, limit)
            if not haveSufficientLeft:
                node.left = None
            if not haveSufficientRight:
                node.right = None
            return haveSufficientLeft or haveSufficientRight
        haveSufficient = checkSufficientLeaf(root, 0, limit)
        return  root if haveSufficient else None
    
if __name__ == '__main__':

    sln  = Solution()                
    
    root = lst2bintree([1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14])
    limit = 1    
    print(binTree2Lst(sln.sufficientSubset(root,limit)))
    
    root = lst2bintree([5,4,8,11,None,17,4,7,1,None,None,5,3])
    limit = 22    
    print(binTree2Lst(sln.sufficientSubset(root,limit)))
    
    root = lst2bintree([1,2,-3,-5,None,4,None])
    limit = -1    
    print(binTree2Lst(sln.sufficientSubset(root,limit)))