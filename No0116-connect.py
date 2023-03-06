""" 
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:

Refer to No116_sample.png

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: 
Given the above perfect binary tree (Figure A), your function should 
populate each next pointer to point to its next right node, just like in Figure B. 
The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level. 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../utilfunc')

import time
from TreeNode import TreeNode 
from TreeNode import binTree2Lst

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Slight modification based on BinaryTree in TreeNode.py.
# Add next field to each node, but all initialized to None.
# In fact, only replace TreeNode with Node.
class BinaryTree:
    def __init__(self, x):
        """ 
        Assuming that the input list represents a valid binary tree
        """
        if len(x) == 0: # []
            self.root = None
        if x[0] == None: # [None]
            self.root = None

        x.reverse() # For the convenience of utilizing x.pop(). Can use x.pop(0) instead.
        nodeLoL = []        
        self.root = Node(x.pop())
        nodeLoL.append([self.root])
        k = 0
        while(1):
            #print('k = {0}, {1}'.format(k, x))
            newLayer = []
            for node in nodeLoL[k]:
                #print(node.val)
                if node == None:
                    pass
                else:
                    if len(x) == 0:
                        break
                    tmp = x.pop()
                    if tmp != None:
                        newNode = Node(tmp)
                        node.left = newNode
                        newLayer.append(newNode)

                    if len(x) == 0:
                        break
                    tmp = x.pop()
                    if tmp != None:
                        newNode = Node(tmp)
                        node.right = newNode
                        newLayer.append(newNode)

            if len(x) == 0:
                break
            nodeLoL.append(newLayer)
            k += 1

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None

        lNode = []
        lNode.append(root)
        layerCnt = 0
        while len(lNode) > 0:
            #print(layerCnt)

            # Traverse the current layer for proper connection
            for k in range(len(lNode)-1):
                lNode[k].next = lNode[k+1]
            lNode[-1].next = None
            # Traverse the current layer to add the next layer while remove the current layer at the same time
            for k in range(len(lNode)):
                curNode = lNode.pop(0)
                if curNode.left != None:
                    lNode.append(curNode.left)
                if curNode.right != None:    
                    lNode.append(curNode.right)
            layerCnt += 1
        return root

if __name__ == '__main__':

    sln   = Solution()

    print('Testcase0...')
    nums = [1,2,3,4,5,6,7]    
    bTree = BinaryTree(nums) # NOTE, nums has been changed inside BinaryTree
    # Change the root of bTree to one 'Node' object    
    root = Node(bTree.root.val, bTree.root.left, bTree.root.right, None)
    root = sln.connect(root)
    
    print(binTree2Lst(root))

    # Serialized the tree in level order
    print('Serialize the tree in level order')
    lVal  = []
    lNode = []
    lNode.append(root)    
    layerCnt = 0
    while len(lNode)>0:
        print(layerCnt)
        # Traverse the current layer to add the next layer while remove the current layer at the same time
        for k in range(len(lNode)):
            curNode = lNode.pop(0)
            lVal.append(curNode.val)
            if curNode.next == None:
                lVal.append(None)

            if curNode.left != None:
                lNode.append(curNode.left)
            if curNode.right != None:    
                lNode.append(curNode.right)
        layerCnt += 1

    print(lVal)