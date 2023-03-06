""" 
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 NOTE: This seems the inverse of levelOrderBinaryTree().
"""

import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree
from TreeNode import binTree2Lst

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        nLen = len(nums)
        if nLen == 0:
            return None
        if nLen == 1:
            return TreeNode(nums[0])

        # Pick the median number
        # For odd nLen, pick the center
        # For even nLen, pick the right center
        k    = int(nLen/2)
        root = TreeNode(nums[k])
        leftRoot   = self.sortedArrayToBST(nums[0:k])
        rightRoot  = self.sortedArrayToBST(nums[k+1:])
        root.left  = leftRoot
        root.right = rightRoot

        return root
                
if __name__ == '__main__':

    sln   = Solution()

    # Testcase0 -- Note sure whether it is symmetric...
    print('Testcase0...')
    x   = [-10,-3,0,5,9]
    xBtRoot = sln.sortedArrayToBST(x)
    print(binTree2Lst(xBtRoot))

