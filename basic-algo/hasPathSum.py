"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../utilfunc')

# import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree
from TreeNode import binTree2Lst

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(root):            
            if root == None:
                return False

            pathlist.append(root.val)
            #print(root.val, root.left, root.right)
            #print(pathlist)
            if sum(pathlist) == targetSum and root.left == None and root.right == None:
                return True
            if root.left != None:
                if dfs(root.left) is True:
                    return True
            if root.right != None:
                if dfs(root.right) is True:
                    return True

            pathlist.pop()
            return False

        pathlist = []
        return dfs(root)

if __name__ == '__main__':    
    sln   = Solution()

    print('Testcase1...')
    x   = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    xBT = BinaryTree(x)
    print(binTree2Lst(xBT.root))
    #print(xBT.root.left.right)
    print(sln.hasPathSum(xBT.root, 17))

    print('Testcase2...')
    xBT = TreeNode(5)
    print(sln.hasPathSum(xBT, 5))    

    print('Testcase3...')
    x   = [1,2]
    xBT = BinaryTree(x)
    print(binTree2Lst(xBT.root))
    #print(xBT.root.left.right)
    print(sln.hasPathSum(xBT.root, 1))    