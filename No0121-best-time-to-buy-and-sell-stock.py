""" 
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。 
"""
""" 
解题思路: 
考虑第k天买入，那卖出一定是K+1天后的最高价的某天。
Naive approach: brute-force
扫描每一天作为买入时间，确认对应的profit，最后比较所有profit。
假定找最大值是O(n)，那总的复杂度就是O(n^2).

考虑到max(a[k:]) >= max(a[k+1:]), 可以倒序遍历，这样事实上只需要一次求最大值，
因此总的复杂度就成为O(n)

"""
import math

class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0

        maxPrice = prices[-1]
        maxProfit = 0
        for k in range(len(prices)-2,-1,-1):            
            p = maxPrice - prices[k]
            if p > maxProfit:
                maxProfit = p
            if p < 0: # maxPrice < prices[k]
                maxPrice = prices[k]
            # print('k={0}, maxPrice={1}, maxProfit={2}'.format(k,maxPrice,maxProfit))            

        return maxProfit
        
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()

    # # testcase0    
    # print('sln.numSquares(1)  = {0}'.format(sln.numSquares(1)))
    # print('sln.numSquares(4)  = {0}'.format(sln.numSquares(4)))
    # print('sln.numSquares(9)  = {0}'.format(sln.numSquares(9)))
    # print('sln.numSquares(16) = {0}'.format(sln.numSquares(16)))

    # testcase1
    print('\ntestcase1 ...')
    prices = [7,1,5,3,6,4]    
    tStart= time.time()
    print(sln.maxProfit(prices))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    # testcase2
    print('\ntestcase2 ...')
    prices = [7,6,4,3,1]
    tStart= time.time()
    print(sln.maxProfit(prices))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))

    # testcase3
    print('\ntestcase3 ...')
    n = 100000
    a = np.random.randint(0,1000,(n,))    
    prices  = a.tolist()      
    tStart= time.time()
    print(sln.maxProfit(prices))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))
