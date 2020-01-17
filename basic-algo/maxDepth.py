# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:04:13 2019

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，返回它的最大深度 3 。

@author: chenxy
"""

import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Recursively find the depth of one binary tree.
        """
        if root == None:
            return 0
                
        leftSubTreeDepth = self.maxDepth(root.left)
        rightSubTreeDepth = self.maxDepth(root.right)
        
        return 1 + max(leftSubTreeDepth, rightSubTreeDepth)
    