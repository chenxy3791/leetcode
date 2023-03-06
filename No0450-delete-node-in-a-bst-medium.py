# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:32:25 2022

@author: chenxy
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left==None and root.right==None:
                # 既没有左子树，也没有右子树
                return None
            elif root.left==None and root.right!=None:
                # 只有右子树
                return root.right
            elif root.left!=None and root.right=None:
                # 只有左子树
                return root.left
            else:
                # 既有左子树，也有右子树
                # 搜所根节点的successor，从右子节点出发一直沿着左子树往下寻找直到最后
                # 一个没有左子节点的节点。然后递归地针对root.right调用deleteNode来删
                # 除successor。因为successor 没有左子节点，因此这一步递归调用不会再
                # 次步入这一种情况。然后将successor 更新为新的 root 并返回。
                successor = root.right
                while successor.left:
                    successor = successor.left
                successor.right = self.deleteNode(root.right, successor.val)
                successor.left = root.left
                return successor
        return root

                