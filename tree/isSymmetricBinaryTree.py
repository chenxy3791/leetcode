""" 
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,None,3,None,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.

NOTE(chenxy): The subtree is not necessarily symmetric

The first solution gets Time-Out for the following input:
    [6,82,82,None,53,53,None,-58,None,None,-58,None,-85,-85,None,-9,None,None,-9,None,48,48,None,33,None,None,33,81,None,None,81,5,None,None,5,61,None,None,61,None,9,9,None,91,None,None,91,72,7,7,72,89,None,94,None,None,94,None,89,-27,None,-30,36,36,-30,None,-27,50,36,None,-80,34,None,None,34,-80,None,36,50,18,None,None,91,77,None,None,95,95,None,None,77,91,None,None,18,-19,65,None,94,None,-53,None,-29,-29,None,-53,None,94,None,65,-19,-62,-15,-35,None,None,-19,43,None,-21,None,None,-21,None,43,-19,None,None,-35,-15,-62,86,None,None,-70,None,19,None,55,-79,None,None,-96,-96,None,None,-79,55,None,19,None,-70,None,None,86,49,None,25,None,-19,None,None,8,30,None,82,-47,-47,82,None,30,8,None,None,-19,None,25,None,49]
"""

import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree

class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        if root == None:
            return True

        nodeLst = [root]        
        k = 0
        while 1:
            # Judge whether layer#k is symmetric
            if k > 0:
                for j in range(2**k-1,2**k-1+2**(k-1)):
                    idx1 = j
                    idx2 = 3*(2**k-1) - j #2**k-1+2**k-1 - (j - (2**k-1))

                    if nodeLst[idx1] == None and nodeLst[idx2] == None:
                        pass
                    elif nodeLst[idx1] == None and nodeLst[idx2] != None:
                        return False
                    elif nodeLst[idx1] != None and nodeLst[idx2] == None:
                        return False
                    elif nodeLst[idx1].val != nodeLst[idx2].val:
                        return False                    

            # Add layer#(k+1) nodes to nodeLst
            # Even all of them are None, it means touching the bottom
            allNone = True
            for j in range(2**k-1,2**k-1+2**k):
                if nodeLst[j] != None:
                    allNone = False
                    nodeLst.append(nodeLst[j].left)
                    nodeLst.append(nodeLst[j].right)
                else: # Add None as placeholder
                    nodeLst.append(None)
                    nodeLst.append(None)

            if allNone == True:
                return True

            k += 1        

    def isSymmetric2(self, root: TreeNode) -> bool:
        """Fail for input: [1,2,2,None,3,None,3] """
        if root == None:
            return True

        nodeLst = [root]        
        cumuNnodePrev = 0 #Cumulative number of nodes up to the previous layer        
        numNode     = 1 #Number of nodes of the current layer
        k = 0
        while 1:
            # Judge whether layer#k is symmetric
            #if k > 0:
            for j in range(cumuNnodePrev,cumuNnodePrev + int(numNode/2) ):
                idx1 = j
                idx2 = 2*cumuNnodePrev + numNode - 1 - j
                print('k = {0}, idx1 = {1}, idx2 = {2}'.format(k, idx1, idx2))

                if nodeLst[idx1] == None and nodeLst[idx2] == None:
                    pass
                elif nodeLst[idx1] == None and nodeLst[idx2] != None:
                    return False
                elif nodeLst[idx1] != None and nodeLst[idx2] == None:
                    return False
                elif nodeLst[idx1].val != nodeLst[idx2].val:
                    return False                    
            
            # Add layer#(k+1) nodes to nodeLst
            # Even all of them are None, it means touching the bottom
            cumuNnode = cumuNnodePrev + numNode
            numNode = 0
            for j in range(cumuNnodePrev,cumuNnode):
                if nodeLst[j] != None:
                    nodeLst.append(nodeLst[j].left)
                    nodeLst.append(nodeLst[j].right)
                    numNode += 2
            if numNode == 0:
                return True

            cumuNnodePrev = cumuNnode
            k += 1        

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0 -- Note sure whether it is symmetric...
    print('Testcase0...')
    x   = [6,82,82,None,53,53,None,-58,None,None,-58,None,-85,-85,None,-9,None,None,-9,None,48,48,None,33,None,None,33,81,None,None,81,5,None,None,5,61,None,None,61,None,9,9,None,91,None,None,91,72,7,7,72,89,None,94,None,None,94,None,89,-27,None,-30,36,36,-30,None,-27,50,36,None,-80,34,None,None,34,-80,None,36,50,18,None,None,91,77,None,None,95,95,None,None,77,91,None,None,18,-19,65,None,94,None,-53,None,-29,-29,None,-53,None,94,None,65,-19,-62,-15,-35,None,None,-19,43,None,-21,None,None,-21,None,43,-19,None,None,-35,-15,-62,86,None,None,-70,None,19,None,55,-79,None,None,-96,-96,None,None,-79,55,None,19,None,-70,None,None,86,49,None,25,None,-19,None,None,8,30,None,82,-47,-47,82,None,30,8,None,None,-19,None,25,None,49]
    xBT = BinaryTree(x)
    print(sln.isSymmetric2(xBT.root))

    # Testcase1
    print('Testcase1...')
    x = [1,2,2,None,3,None,3]
    xBT = BinaryTree(x)
    print(sln.isSymmetric2(xBT.root))

    # Testcase2
    print('Testcase2...')
    x = [1,2,2,None,3,3,None]
    xBT = BinaryTree(x)
    print(sln.isSymmetric2(xBT.root))
