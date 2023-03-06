""" 
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

import time
from TreeNode import TreeNode

class Solution:
    #def levelOrder(self, root: TreeNode) -> List[List[int]]:
    def levelOrder(self, root: TreeNode):
        if root == None:
            return []

        nodeLoL  = [[root]]
        valueLoL = [[root.val]]
        k        = 0
        while 1:
            curLayer  = nodeLoL[k]
            newNodeLayer  = []
            newValLayer   = []
            isAllNone = True
            for node in curLayer:
                if node.left != None:
                    newNodeLayer.append(node.left)
                    newValLayer.append(node.left.val)
                    isAllNone = False                    
                if node.right != None:
                    newNodeLayer.append(node.right)                                                         
                    newValLayer.append(node.right.val)
                    isAllNone = False                    

            if isAllNone: # Don't add the all-None layer
                return valueLoL
            nodeLoL.append(newNodeLayer)
            valueLoL.append(newValLayer)         
            
            k += 1

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    trRoot = None
    print(sln.levelOrder(trRoot))
    
