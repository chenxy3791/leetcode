# -*- coding: utf-8 -*-
"""
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
 
提示:

节点数在 [1, 500] 范围内
0 <= Node.val <= 500
Node.val 中所有值 不同
目标结点 target 是树上的结点。
0 <= k <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 这道题就是先把二叉树转化为图,再用图的bfs,求得解.所以,这道题关键就是如何把树转化成图.
import sys
import time
import random
from   typing import List
from   myPackage.BinaryTree import BinaryTree 
from   myPackage.BinaryTree import TreeNode

class Solution:    
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        :root:   TreeNode
        :target: TreeNode
        :K:      int
        :ret:    List[int]
        """
        from collections import defaultdict
        graph = defaultdict(set)
        # Build the graph via depth first search
        def dfs(root):
            if root.left :
                graph[root.val].add(root.left.val)
                graph[root.left.val].add(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].add(root.right.val)
                graph[root.right.val].add(root.val)
                dfs(root.right)
                
        dfs(root)
        print(graph)
        
        # Breadth first search
        cur = [target.val]
        visited ={target.val}
        while K:
            next_time = []
            while cur:
                tmp = cur.pop()
                for node in graph[tmp]:
                    if node not in visited:
                        visited.add(node)
                        next_time.append(node)
            K -= 1
            cur = next_time
        return cur

    
if __name__ == '__main__':        
    
    sln = Solution()

    binTreeLst = [3,5,1,6,2,0,8,None,None,7,4]
    target = TreeNode(5)
    K = 2
    
    binTree = BinaryTree(binTreeLst)
    print(sln.distanceK(binTree.root, target, K))