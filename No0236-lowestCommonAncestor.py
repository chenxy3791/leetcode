""" 
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../utilfunc')

import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree 
from TreeNode import binTree2Lst

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target):
            #print('dfs({0}, {1})'.format(root.val, target))
            if root.val == target.val:
                return [target]
            if root.left != None:
                tmp = dfs(root.left, target)
                if tmp != []:
                    return [root] + tmp
            if root.right != None:
                tmp = dfs(root.right, target)
                if tmp != []:
                    return [root] + tmp     
            return []

        if root == None or p == None or q == None:
            return None
        pTmp = dfs(root,p)
        qTmp = dfs(root,q)
        #print(pTmp)
        #print(qTmp)

        k = 0
        while k < len(pTmp) and k < len(qTmp):
            if pTmp[k].val == qTmp[k].val: # Assuming the node value are all unique
                k += 1
            else:
                break
        if k == 0:
            return None
        else:
            return qTmp[k-1]

if __name__ == '__main__':

    sln   = Solution()

    print('Testcase1...')
    nodeLst = [3,5,1,6,2,0,8,None,None,7,4]
    binT = BinaryTree(nodeLst) # NOTE, nums has been changed inside BinaryTree
    p    = TreeNode(5)
    q    = TreeNode(1)        
    lca  = sln.lowestCommonAncestor(binT.root, p, q)
    if lca == None:
        print(None)
    else:
        print(lca.val)

    print('Testcase2...')
    nodeLst = [3,5,1,6,2,0,8,None,None,7,4]
    binT = BinaryTree(nodeLst) # NOTE, nums has been changed inside BinaryTree
    p    = TreeNode(5)
    q    = TreeNode(4)        
    lca  = sln.lowestCommonAncestor(binT.root, p, q)
    if lca == None:
        print(None)
    else:
        print(lca.val)

    print('Testcase3...')
    nodeLst = [3,5,1,6,2,0,8,None,None,7]
    binT = BinaryTree(nodeLst) # NOTE, nums has been changed inside BinaryTree
    p    = TreeNode(5)
    q    = TreeNode(4)        
    lca  = sln.lowestCommonAncestor(binT.root, p, q)    
    if lca == None:
        print(None)
    else:
        print(lca.val)

    print('Testcase4...')
    p    = TreeNode(5)
    q    = TreeNode(4)        
    lca  = sln.lowestCommonAncestor(None, p, q)        
    if lca == None:
        print(None)
    else:
        print(lca.val)

    print('Testcase5...')
    nodeLst = [3,5,1,6,2,0,8,None,None,7]
    binT = BinaryTree(nodeLst) # NOTE, nums has been changed inside BinaryTree
    p    = None
    q    = TreeNode(8)        
    lca  = sln.lowestCommonAncestor(None, p, q)        
    if lca == None:
        print(None)
    else:
        print(lca.val)

    print('Testcase6...')
    nodeLst = [3,5,1,6,2,0,8,None,None,7]
    binT = BinaryTree(nodeLst) # NOTE, nums has been changed inside BinaryTree
    p    = TreeNode(4)        
    q    = TreeNode(9)        
    lca  = sln.lowestCommonAncestor(None, p, q)        
    if lca == None:
        print(None)
    else:
        print(lca.val)