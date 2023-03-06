""" 
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    #def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 0:
            return TreeNode(inorder[0])

        rootVal = postorder.pop()
        k = inorder.index(rootVal)
        leftInorder    = inorder[0:k]
        rightInorder   = inorder[k+1:]
        leftPostorder  = postorder[0:k]
        rightPostorder = postorder[k:]
        root = TreeNode(rootVal)
        root.left = self.buildTree(leftInorder,leftPostorder)
        root.right = self.buildTree(rightInorder,rightPostorder)

        return root

if __name__ == '__main__':

    sln   = Solution()

    print('Testcase0...')
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    bt = sln.buildTree(inorder,postorder)
    
    print(binTree2Lst(bt))


    
