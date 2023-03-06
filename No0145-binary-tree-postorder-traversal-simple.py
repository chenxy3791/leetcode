# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:24:01 2022

@author: chenxy

145. 二叉树的后序遍历
给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。

示例 1：
输入：root = [1,null,2,3]
输出：[3,2,1]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
 
提示：
树中节点的数目在范围 [0, 100] 内
-100 <= Node.val <= 100
进阶：递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List	
# import random
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
from collections import deque
# import itertools as it
# import numpy as np

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def postorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        
        ans = []
        if root.left != None:
            left_lst = self.postorderTraversal(root.left)
            ans = ans + left_lst
        if root.right != None:
            right_lst = self.postorderTraversal(root.right)
            ans = ans + right_lst
        ans.append(root.val)
        
        return ans        

    def postorderTraversalIteration(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        ans = []        
        s = deque()  # Used as stack, instead of FIFO
        visited = set()
        s.append(root)
        while len(s)>0:
            hasChildrenNotYetProcessed = False
            node = s.pop()
            for child in node.children:   
                if (child not in visited):
                    s.append(node)
                    s.append(child)
                    hasChildrenNotYetProcessed = True
                    break
            if hasChildrenNotYetProcessed:
                continue
            ans.append(node.val)
            visited.add(node)                
        return ans            
                
        