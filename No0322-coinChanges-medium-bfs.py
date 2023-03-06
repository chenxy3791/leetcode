""" 
322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0
 
提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
""" 
解题思路
最小路径问题-->广度优先搜索
一个巨大的教训是：visited用set()与用list有巨大的速度之差
一开始用list实现visited。。。超出时间限制
后来参考评论区的改用set,同一个超时的case在本机上执行的用时为1.77s vs 0.016s，竟然有100倍之巨！！！

执行用时 :664 ms, 在所有 Python3 提交中击败了94.06%的用户
内存消耗 :14.4 MB, 在所有 Python3 提交中击败了10.06%的用户
 """
# import math
import sys
import time
import random
from   collections import deque
from   typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        assert(amount >= 0)
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1

        q = deque([amount])
        visited = set()
        layer = 1
        while q:            
            # print('layer = {0}, q.len = {1}'.format(layer,len(q)))
            n = len(q)
            for _ in range(n): # Traverse the current layer
                a = q.pop()
                if a in coins:
                    return layer
                # Add a's neighbours into q
                for c in coins:
                    b = a - c
                    if b > 0 and b not in visited:
                        visited.add(b)                        
                        q.appendleft(b)               
            layer = layer + 1
        return -1

class Solution1:
    #def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount: int) -> int:
        assert(amount >= 0)
        if amount == 0:
            return 0
        if amount < min(coins):
            return -1

        q = [amount]
        visited = [amount]
        layer = -1
        while len(q) > 0:
            qSize = len(q)
            layer = layer + 1
            # print('layer = {0}'.format(layer))
            # print('layer = {0}, q = {1}'.format(layer,q))
            # print(q, visited)
            for k in range(qSize):
                a = q.pop(0)                
                if a in coins:
                    return layer + 1
                else: # Add a's neighbours into q
                    for c in coins:
                        if c < a and (a-c) not in visited:
                            q.append((a-c)) # No other choices except 1
                            visited.append((a-c)) # Instead of add to visited when pop.
        return -1

if __name__ == '__main__':

    import time
    sln   = Solution()

    # # testcase0    
    # print('sln.numSquares(1)  = {0}'.format(sln.numSquares(1)))
    # print('sln.numSquares(4)  = {0}'.format(sln.numSquares(4)))
    # print('sln.numSquares(9)  = {0}'.format(sln.numSquares(9)))
    # print('sln.numSquares(16) = {0}'.format(sln.numSquares(16)))

    # testcase1
    coins = [1, 2, 5] 
    amount = 11
    print(sln.coinChange(coins, amount))

    # testcase2
    coins = [2] 
    amount = 3
    print(sln.coinChange(coins, amount))

    # testcase3
    coins = [1, 2, 5, 10, 20,50, 100] 
    amount = 1001
    tStart= time.time()
    print(sln.coinChange(coins, amount))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    # testcase3
    coins = [470,35,120,81,121]
    amount = 9825
    tStart= time.time()
    print(sln.coinChange(coins, amount))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
