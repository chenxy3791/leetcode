# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:01:04 2019
2020-1-21 Add BinaryTree class

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
            print('k = {0}, {1}'.format(k, x))
            newLayer = []
            for node in nodeLoL[k]:
                print(node.val)
                if node == None:
                    pass
                else:
                    if len(x) == 0:
                        break
                    newNode = TreeNode(x.pop())
                    node.left = newNode
                    newLayer.append(newNode)

                    if len(x) == 0:
                        break
                    newNode = TreeNode(x.pop())
                    node.right = newNode
                    newLayer.append(newNode)

            if len(x) == 0:
                break
            nodeLoL.append(newLayer)
            k += 1

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