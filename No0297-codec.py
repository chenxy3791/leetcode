""" 
Serialization is the process of converting a data structure or object into 
a sequence of bits so that it can be stored in a file or memory buffer, or 
transmitted across a network connection link to be reconstructed later in 
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary 
tree. You do not necessarily need to follow this format, so please be creative 
and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your 
serialize and deserialize algorithms should be stateless.
"""

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../utilfunc')

import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree 
from TreeNode import binTree2Lst

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        The same as binTree2Lst() in TreeNode.py, except that the final output is converted to a string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []

        nodeLst = [root]
        valLst  = []
        
        while len(nodeLst) > 0:
            curNode = nodeLst.pop()
            if curNode != None:
                nodeLst.insert(0,curNode.left)
                nodeLst.insert(0,curNode.right)        
                valLst.append(curNode.val)
            else:
                valLst.append(None)

        # Throw away the trailing 'None'
        while valLst[-1] == None:
            valLst.pop()

        return str(valLst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        Refined based BinaryTree constructor.
        It seems there is no need of maintaining nodeLoL, layered storing of the TreeNodes.
        Only storing the current layer should be enough.

        :type data: str
        :rtype: TreeNode
        """
        if data == []:
            return None

        # lVal = list(map(int,data[1:-1].split(', ')))  # undo str(aList). Don't work. Because there is None in the original list.
        tmp  = data[1:-1].split(', ')
        #print(tmp)
        #print(type(tmp), len(tmp))
        lVal = []        
        for k in range(len(tmp)):
            #print('k = {0}, data[k] = {1}'.format(k, tmp[k]))
            if tmp[k] == 'None':
                lVal.append(None)
            else:
                lVal.append(int(tmp[k]))
        #print(lVal)
        #print(type(lVal))

        if len(lVal) == 0: # []
            root = None
        if lVal[0] == None: # [None]
            root = None

        lVal.reverse() # For the convenience of utilizing data.pop()
        nodeLoL = []        
        root    = TreeNode(lVal.pop())
        nodeLoL.append(root)
        k = 0
        while(1):
            #print('k = {0}, {1}'.format(k, data))
            #newLayer = []
            #for node in nodeLoL:
            while len(nodeLoL) > 0:
                #print(node.val)
                node = nodeLoL.pop(0)
                if node == None:
                    pass
                else:
                    if len(lVal) == 0:
                        break
                    tmp = lVal.pop()
                    if tmp != None:
                        newNode = TreeNode(tmp)
                        node.left = newNode
                        nodeLoL.append(newNode)

                    if len(lVal) == 0:
                        break
                    tmp = lVal.pop()
                    if tmp != None:
                        newNode = TreeNode(tmp)
                        node.right = newNode
                        nodeLoL.append(newNode)

            if len(lVal) == 0:
                break
            k += 1    
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':

    codec = Codec()

    print('\nTestcase1...')
    nodeStr = str([3,5,1,6,2,0,8,None,None,7,4])
    print(nodeStr)
    print(codec.serialize(codec.deserialize(nodeStr)))

    print('\nTestcase2...')
    nodeStr = str([1,2,3,None,None,4,5])    
    print(binTree2Lst(codec.deserialize(nodeStr)))

    print('\nTestcase3...')
    nodeLst = [1,2,3,None,None,4,5]
    binT = BinaryTree(nodeLst) # NOTE, nums has been changed inside BinaryTree
    print(binTree2Lst(codec.deserialize(codec.serialize(binT.root))))

    print('\nTestcase4...')
    nodeStr = [] # Leetcode testcase. But why this is a valid input?
    print(nodeStr)
    print(codec.serialize(codec.deserialize(nodeStr)))
