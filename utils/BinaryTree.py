# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:01:04 2019
2020-01-21 Add BinaryTree class
2020-01-22 Add BinaryTree.binTree2Lst()
2021-07-29 Rename to BinaryTree

@author: chenxy
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None

class BinaryTree:
    def __init__(self, x):
        """ 
        Assuming that the input list represents a valid binary tree
        """
        if len(x) == 0: # []
            self.root = None
        if x[0] == None: # [None]
            self.root = None

        x.reverse() # For the convenience of utilizing x.pop()
        nodeLoL = []        
        self.root = TreeNode(x.pop())
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
                        newNode = TreeNode(tmp)
                        node.left = newNode
                        newLayer.append(newNode)

                    if len(x) == 0:
                        break
                    tmp = x.pop()
                    if tmp != None:
                        newNode = TreeNode(tmp)
                        node.right = newNode
                        newLayer.append(newNode)

            if len(x) == 0:
                break
            nodeLoL.append(newLayer)
            k += 1

def binTree2Lst(root):
    """ 
        An inverse of the BinaryTree constructor. 
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

    return valLst

if __name__ == '__main__':    

    x   = [3,9,20,None,None,15,7]
    xBT = BinaryTree(x)
    print(xBT.root.val)
    print(xBT.root.left.val)
    print(xBT.root.right.val)
    print(xBT.root.left.left)
    print(xBT.root.left.right)    
    print(xBT.root.right.left.val)
    print(xBT.root.right.right.val)    

    print(binTree2Lst(xBT.root))