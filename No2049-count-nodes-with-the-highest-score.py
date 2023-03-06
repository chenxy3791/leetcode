# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 07:23:11 2022

@author: chenxy

2049. 统计最高分的节点数目
给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。
同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。
由于节点 0 是根，所以 parents[0] == -1 。
一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。
求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。
请你返回有 最高得分 节点的 数目 。

示例 1:
输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。

示例 2：
输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
 
提示：
n == parents.length
2 <= n <= 10^5
parents[0] == -1
对于 i != 0 ，有 0 <= parents[i] <= n - 1
parents 表示一棵二叉树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-nodes-with-the-highest-score
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List	
# import random
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
# import itertools as it
# import numpy as np

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # Construct children. No need of care about the order of left/right children
        children = dict()
        for k in range(len(parents)):
            if parents[k] >= 0:
                if parents[k] in children:
                    children[parents[k]].append(k)
                else:
                    children[parents[k]] = [k]                    
        # print(children)
        # DFS
        N    = len(parents)
        memo = dict() # (leftSubTreeSize, rightSubTreeSize, score)
        def dfs(node): 
            # ret: (leftSubTreeSize, rightSubTreeSize, score)
            if node in memo:
                return memo[node]
            
            if node not in children: 
                # leaf node                
                memo[node] = (0,0,N-1)
                return (0,0,N-1)
            child0_data = dfs(children[node][0])
            subtree0_size = child0_data[0]+child0_data[1]+1
            if len(children[node]) == 2:
                child1_data = dfs(children[node][1])
                subtree1_size = child1_data[0]+child1_data[1]+1
                if node == 0:
                    # Special handling for root node.
                    score = subtree0_size*subtree1_size
                else:
                    score = subtree0_size*subtree1_size*(N-1-subtree0_size-subtree1_size)
            else:
                subtree1_size = 0
                if node == 0:
                    # Special handling for root node.
                    score = subtree0_size
                else:
                    score = subtree0_size*(N-1-subtree0_size)
            memo[node] = (subtree0_size,subtree1_size,score)
            return (subtree0_size,subtree1_size,score)
        
        dfs(0)
        # print(memo)
        maxscore     = -1
        maxscorecnt  = 0
        for node in memo:
            if maxscore < memo[node][2]:
                maxscore = memo[node][2]
                maxscorecnt  = 1
            elif maxscore == memo[node][2]:                
                maxscorecnt  += 1
        return maxscorecnt

if __name__ == '__main__':            
    
    sln = Solution()            

    parents = [-1,2,0,2,0]
    tStart = time.time()     
    ans = sln.countHighestScoreNodes(parents)
    tElapsed = time.time() - tStart        
    print('ans = {0}, tElapsed = {1} (sec)'.format(ans,tElapsed))                  
                
    parents = [-1,2,0]
    tStart = time.time()     
    ans = sln.countHighestScoreNodes(parents)
    tElapsed = time.time() - tStart        
    print('ans = {0}, tElapsed = {1} (sec)'.format(ans,tElapsed))                                  