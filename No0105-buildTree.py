""" 
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../utilfunc')

import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree
from TreeNode import binTree2Lst

class Solution:
    #def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 0:
            return TreeNode(inorder[0])

        rootVal = preorder[0]
        k = inorder.index(rootVal)
        leftInorder   = inorder[0:k]
        rightInorder  = inorder[k+1:]
        leftPreorder  = preorder[1:k+1]
        rightPreorder = preorder[k+1:]
        root = TreeNode(rootVal)
        root.left = self.buildTree(leftPreorder,leftInorder)
        root.right = self.buildTree(rightPreorder,rightInorder)

        return root

if __name__ == '__main__':

    sln   = Solution()

    print('Testcase0...')
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    bt = sln.buildTree(preorder,inorder)
    
    print(binTree2Lst(bt))


    
