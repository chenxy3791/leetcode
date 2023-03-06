"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

在不同的二叉搜索树中，我们了解到，需要构建的二叉搜索树的数量实际上满足卡特兰数。   
"""
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../utilfunc')

import time
from TreeNode import TreeNode 
from TreeNode import BinaryTree
from TreeNode import binTree2Lst

class Solution:
    #def generateBSTrees(self, n: int) -> List[TreeNode]:
    def generateBSTreesWoMemo(self, n: int):
        def dp(p,q):
            if p > q:
                return [None]
            if p == q:
                return [TreeNode(p)]
            
            bstList = []
            for k in range(p,q+1):
                leftTrees = dp(p,k-1)
                rightTrees= dp(k+1,q)

                # print('\ndp({0}, {1}), k = {2}: '.format(p,q,k))
                # print('++++leftTrees:')
                # for kk in range(len(leftTrees)):
                #     print(binTree2Lst(leftTrees[kk]))
                # print('++++rightTrees:')
                # for kk in range(len(rightTrees)):
                #     print(binTree2Lst(rightTrees[kk]))

                for i in range(len(leftTrees)):
                    for j in range(len(rightTrees)):
                        root       = TreeNode(k)
                        root.left  = leftTrees[i]
                        root.right = rightTrees[j]
                        bstList.append(root)
            return bstList
        return dp(1,n)

    def generateBSTreesWithMemo(self, n: int):
        # Improvement is not satisfactory.
        # More efficient implementation need further investigation.
        # For example, dp(p+k,q+k) should have the same trees as dp(p,q),
        # only with the constant offset 'k' for each node's value.

        # 执行用时战胜95.41%的python3提交记录
        
        memo = dict()
        def dp(p,q):
            if p > q:
                return [None]
            if p == q:
                return [TreeNode(p)]
            
            if (p,q) in memo:
                return memo[(p,q)]
            bstList = []
            for k in range(p,q+1):
                leftTrees = dp(p,k-1)
                rightTrees= dp(k+1,q)

                # print('\ndp({0}, {1}), k = {2}: '.format(p,q,k))
                # print('++++leftTrees:')
                # for kk in range(len(leftTrees)):
                #     print(binTree2Lst(leftTrees[kk]))
                # print('++++rightTrees:')
                # for kk in range(len(rightTrees)):
                #     print(binTree2Lst(rightTrees[kk]))

                for i in range(len(leftTrees)):
                    for j in range(len(rightTrees)):
                        root       = TreeNode(k)
                        root.left  = leftTrees[i]
                        root.right = rightTrees[j]
                        bstList.append(root)
            memo[(p,q)] = bstList
            return bstList

        if n == 0:
            return []

        return dp(1,n)

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    n = 0
    bstList = sln.generateBSTreesWithMemo(n)
    print(bstList)

    print('Testcase2...')
    n = 2

    tStart = time.time()            
    bstList = sln.generateBSTreesWoMemo(n)
    print('number of unique BSTs = {0}'.format(len(bstList)))
    if len(bstList) <= 20:
        for k in range(len(bstList)):
            print(binTree2Lst(bstList[k]))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')             

    tStart = time.time()            
    bstList = sln.generateBSTreesWithMemo(n)
    print('number of unique BSTs = {0}'.format(len(bstList)))
    if len(bstList) <= 20:
        for k in range(len(bstList)):
            print(binTree2Lst(bstList[k]))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')             


