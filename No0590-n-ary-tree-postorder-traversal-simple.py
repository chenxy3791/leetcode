# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:13:43 2022

@author: chenxy

590. N 叉树的后序遍历
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]

提示：
节点总数在范围 [0, 10^4] 内
0 <= Node.val <= 10^4
n 叉树的高度小于或等于 1000

进阶：递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
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

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorderRecursion(self, root: 'Node') -> List[int]:
        ans = []
        if root==None:
            return []
        if root.children==None:
            return [root.val]
        
        for child in root.children:
            child_lst = self.postorder(child)
            ans = ans + child_lst
        ans.append(root.val)
        
        return ans

    def postorderIteration(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        ans = []        
        s = deque()  # Used as stack, instead of FIFO
        visited = set()
        s.append(root)
        while len(s)>0:
            node = s.pop()
            for child in node.children:
                if child.children == None:
                    ans.append(node.val)
                    visited.add(node)
                    continue              
                if (child not in visited):
                    s.append(node)
                    s.append(child)
                    continue
            ans.append(node.val)
            visited.add(node)                
        return ans   
