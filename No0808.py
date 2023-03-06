# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:43:52 2022

@author: chenxy

ref1:
    全概率公式 + 记忆化搜索。

由全概率公式可得：P(X) = P(X|Y1)*P(Y1) + P(X|Y2)*P(Y2) + P(X|Y3)*P(Y3) + P(X|Y4)*P(Y4)。全概率公式。

其中，P(X) 为我们所要求的事件发生的概率，P(Yi) 为操作 i 发生的概率，在本题中他们是相等的，P(Y1) = P(Y2) = P(Y3) = P(Y4) = 0.25，P(X|Yi) 为 操作 i 发生的条件下 X 事件发生的概率。

回到程序中，我们用 prob(a, b) 表示汤 A 剩余 a 毫升，汤 B 剩余 b 毫升时的概率。那么由全概率公式：prob(a, b) = prob(a1, b1)*0.25 + prob(a2, b2)*0.25 + prob(a3, b3)*0.25 + prob(a4, b4)*0.25 其中 ai, bi 表示执行操作 i 之后，汤 A 和汤 B 中剩余汤的容量。

可以发现，这是一个递归的过程。我们可以使用记忆化搜索进行优化。然而数据范围实在是太大了。我们观察 4 个操作可以发现，A 先倒完的概率大于等于 B 先倒完的概率，而且随着 n 的增大，A 先倒完的概率会越来越大，B 先倒完的概率会越来越小。那么当 n 足够大的时候，答案趋近于 1。答案要求误差小于 10^-5，我们可以算一下当 n = 5000 时，误差已经小于 10^-5 了，所以当 n >= 5000 时可以直接返回 1。

ref2:
这道“中等”题的rating达到2396，曾经在周赛第三题top1的位置上坐了好几年（直到半年前被第295场周赛赶下去了）。
这道题是浮点数精度和概率论的完美结合，想要通过这道题就必须敢于写这个特判，而不能轻易怀疑二维DP的思路是错误的。
也许用数学期望去分析这个问题并不难，但看到这样的数据范围，又有多少人会坚信O(n^2)的做法是对的呢？
这正如人世间很多事情的成功，既需要足够的实力，也需要强大的内心。
（另外可以直接return 1.的最小n值似乎是4801）

"""
import random

class Solution:
    def soupServings(self, n: int) -> float:
        nRun        = 1000000
        A_first_cnt = 0
        AB_sametime_cnt = 0
        for l in range(int(nRun)):
            nA = nB         = n    
            #A_first_flg     = 0
            #B_first_flg     = 0
            #AB_sametime_flg = 0
            while nA > 0 or nB > 0:
                k = random.randint(0, 3)
                if k == 0:
                    nA = max(0,nA-100)
                elif k == 1:
                    nA = max(0,nA-75)
                    nB = max(0,nB-25)
                elif k == 2:
                    nA = max(0,nA-50)
                    nB = max(0,nB-50)                    
                else:
                    nA = max(0,nA-25)
                    nB = max(0,nB-75)                    
                
                if nA==0 and nB>0:
                    #A_first_flg = 1
                    A_first_cnt += 1
                    break
                elif nA>0 and nB==0:
                    #B_first_flg = 1
                    break                    
                elif nA==0 and nB==0:
                    #AB_sametime_flg = 1       
                    AB_sametime_cnt += 1
                    break
                
            #A_first_cnt += A_first_flg
            #AB_sametime_cnt += AB_sametime_flg
        print(nRun, A_first_cnt, AB_sametime_cnt)
        return A_first_cnt/nRun + AB_sametime_cnt/nRun/2

class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0] = [0.5] + [1.0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] +
                            dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)]) / 4
        return dp[n][n]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/soup-servings/solution/fen-tang-by-leetcode-solution-0yxs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (dfs(a - 4, b) + dfs(a - 3, b - 1) +
                    dfs(a - 2, b - 2) + dfs(a - 1, b - 3)) / 4
        return dfs(n, n)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/soup-servings/solution/fen-tang-by-leetcode-solution-0yxs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
if __name__ == '__main__':     
    
    sln = Solution()
    n = 50
    print('n = {0}, ans = {1}'.format(n,sln.soupServings(n)))

    n = 100
    print('n = {0}, ans = {1}'.format(n,sln.soupServings(n)))    
    
    
            