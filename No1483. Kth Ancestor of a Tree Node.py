# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 08:36:53 2023

@author: chenxy

1483. Kth Ancestor of a Tree Node
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

The kth ancestor of a tree node is the kth node in the path from that node to the root node.

Implement the TreeAncestor class:

TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.
 

Example 1:


Input
["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
Output
[null, 1, 0, -1]

Explanation
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor
 

Constraints:

1 <= k <= n <= 5 * 10**4
parent.length == n
parent[0] == -1
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5 * 10**4 queries.
"""
"""
方法一：倍增
思路

倍增的思路类似于动态规划，定义 ancestors[i][j] 表示节点 i 的第 2**j个祖先。此题中，树最多有 
50000 个节点，因此 ancestors 的第二维度的最大值可以设为 16。根据定义，
ancestors[i][0]=parent[i]。状态转移方程是 
ancestors[i][j]=ancestors[ancestors[i][j−1]][j−1]，即当前节点的第 
2 ** j  个祖先，是他的第 2**(j−1)个祖先的第 2 **(j−1)个祖先。当第 2 **j个祖先不存在时，记为 −1。

查询时，需要将 k 的二进制表示从最低位到最高位依次进行判断，如果第 j 位为 1，则节点 node 需要进行转移到 
ancestors[node][j]，表示 node 向祖先方向移动了 2**j  次。直至遍历完 k 所有位或者 node 变为 −1。

复杂度分析

时间复杂度：初始化的时间复杂度是 O(n×logn)，单次查询的时间复杂度是 O(logn)。

空间复杂度：初始化的空间复杂度是 O(n×logn)，单次查询的空间复杂度是 O(1)。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/solution/shu-jie-dian-de-di-k-ge-zu-xian-by-leetc-hdxd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
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
from utils.BinaryTree import TreeNode, binTree2Lst, lst2bintree
from functools import reduce

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.log = 16
        self.ancestors = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.log):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]   

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.log):
            if (k>>j) & 1: 
                node = self.ancestors[node][j]
                if node == -1:
                    return -1
        return node



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)