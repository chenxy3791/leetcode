# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 07:22:09 2022

@author: chenxy

589. N 叉树的前序遍历
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

示例 1：
输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]

示例 2：
输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]

提示：
节点总数在范围 [0, 10^4]内
0 <= Node.val <= 10^4
n 叉树的高度小于或等于 1000
 
进阶：递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List	
# import random
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
# import itertools as it
# import numpy as np

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = [root.val]
        for child in root.children:
            ans = ans + self.preorder(child)
        return ans

# =============================================================================
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         ans = []
#         def dfs(node: 'Node'):
#             if node is None:
#                 return
#             ans.append(node.val)
#             for ch in node.children:
#                 dfs(ch)
#         dfs(root)
#         return ans
# 
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/n-cha-shu-de-qian-xu-bian-li-by-leetcode-bg99/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# =============================================================================


# def buildNaryTreeFromLevelTraverse(nodeList):
#     root = Node(nodeList[0])
    
        
        
if __name__ == '__main__':   
         
    sln = Solution()
    root = [1,null,3,2,4,null,5,6]
    print(sln.preorder(root))

    root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    print(sln.preorder(root))    