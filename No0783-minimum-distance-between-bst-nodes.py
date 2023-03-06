# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:52:07 2021

@author: chenxy

783. 二叉搜索树节点最小距离
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

示例 1：

输入：root = [4,2,6,1,3]
输出：1
示例 2：


输入：root = [1,0,48,null,null,12,49]
输出：1
 

提示：

树中节点数目在范围 [2, 100] 内
0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
import math
from myPackage.TreeNode import TreeNode
from myPackage.TreeNode import BinaryTree

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root == None or (root.left == None and root.right == None):
            return math.inf
        
        ret = math.inf

        leftNode = root.left        
        if leftNode != None:
            d1 = self.minDiffInBST(leftNode)
            # Search for the rightmost leave of left subtree        
            while leftNode.right != None:
                leftNode = leftNode.right
            d2 = abs(root.val - leftNode.val)
            # print(ret,d1,d2)
            ret = min(ret,d1,d2)

        rightNode = root.right        
        if rightNode != None:        
            d1 = self.minDiffInBST(rightNode)
            # Search for the leftmost leave of right subtree        
            while rightNode.left != None:
                rightNode = rightNode.left
            d2 = abs(root.val - rightNode.val)
            # print(ret,d1,d2)
            ret = min(ret,d1,d2)
        
        return ret
    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()    
    x   = [4,2,6,1,3]
    xBST = BinaryTree(x)    
    print(sln.minDiffInBST(xBST.root))

    x = [1,0,48,None,None,12,49]
    xBST = BinaryTree(x)    
    print(sln.minDiffInBST(xBST.root))    

    x = [90,69,None,49,89,None,52]      
    xBST = BinaryTree(x)    
    print(sln.minDiffInBST(xBST.root))        