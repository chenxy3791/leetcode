""" 
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

NOTE:
The intuitive method is recursive search.

"""

import time
from TreeNode import TreeNode

class Solution:
    def maxBST(self, root: TreeNode):
        """ Assuming the input is not an empty tree. """
        assert(root != None)

        max = root.val
        ptr = root
        while ptr.right != None:
            ptr = ptr.right
            if max < ptr.val:
                max = ptr.val
        return max

    def minBST(self, root: TreeNode):
        """ Assuming the input is not an empty tree. """
        assert(root != None)

        min = root.val
        ptr = root
        while ptr.left != None:
            ptr = ptr.left
            if min > ptr.val:
                min = ptr.val
        return min

    def isValidBST(self, root: TreeNode) -> bool:
        # Trival cases
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True

        # Normal cases
        """ 
        A valid BST has to meet the following three criteria:
        (1) max(leftTree) < root < min(rightTree)
        (2) leftTree is valid BST
        (3) rightTree is valid BST        
        """
        isLeftBST  = True
        isRightBST = True
        if root.left != None:
            isLeftBST = self.isValidBST(root.left)
        if root.right != None:
            isRightBST = self.isValidBST(root.right)

        isValid = isLeftBST and isRightBST
        if root.left != None:
            isValid = isValid and (root.val > self.maxBST(root.left))
        if root.right != None:
            isValid = isValid and (root.val < self.minBST(root.right))

        return isValid
        
if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    trRoot = None
    print(sln.isValidBST(trRoot))
    
