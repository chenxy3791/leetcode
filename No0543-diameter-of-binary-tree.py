""" 
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 
"""
""" 
解题思路1: 
从root来看，存在最长路径经过自己(case1)和不经过自己(case2)两种情况
case1: 左子树深度+右子树深度+1
case2: max(左子树 diameter, 右子树 diameter)
Hence, the final result is max{左子树深度+右子树深度+1, 左子树 diameter, 右子树 diameter}
Can be solved with recursive method, but seems too costly.

解题思路2: 
很显然，最长的路径的一端必定是树的最深的叶子节点--不仅限于一个。
可以先正向地从root出发找到最深的某个叶子结点，
然后以该叶子节点作为树的根节点逆向搜索求该树的深度。
但是这样要求重构这颗树--因为要以该叶子节点为新的root?这个是不是会比较麻烦。

解题思路3:


"""
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Two slow. Win only 6% python3 delivery!
    def getdepth(self, root: TreeNode):
        # Not exactly the depth of tree, the number of edges from the root to
        # the deepest leaf
        if root == None:
            return 0

        if root.left == None:
            depleft = 0
        else:
            depleft = 1 + self.getdepth(root.left)

        if root.right == None:
            depright = 0
        else:
            depright = 1 + self.getdepth(root.right)

        return max(depleft,depright)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        d0 = 0
        if root.left != None:
            d0 = d0 + self.getdepth(root.left) + 1
        if root.right != None:
            d0 = d0 + self.getdepth(root.right) + 1

        dleft = self.diameterOfBinaryTree(root.left)
        dright= self.diameterOfBinaryTree(root.right)
        #print(d0, dleft, dright)
        return max(d0,max(dleft,dright))
               
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()

    # # testcase1
    # print('\ntestcase1 ...')
    # prices = [7,1,5,3,6,4]    
    # tStart= time.time()
    # print(sln.maxProfit(prices))
    # tStop = time.time()
    # print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    # # testcase2
    # print('\ntestcase2 ...')
    # prices = [7,6,4,3,1]
    # tStart= time.time()
    # print(sln.maxProfit(prices))
    # tStop = time.time()
    # print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))

    # # testcase3
    # print('\ntestcase3 ...')
    # n = 100000
    # a = np.random.randint(0,1000,(n,))    
    # prices  = a.tolist()      
    # tStart= time.time()
    # print(sln.maxProfit(prices))
    # tStop = time.time()
    # print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))
