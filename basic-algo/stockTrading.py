""" 
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum trade. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), trade = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), trade = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), trade = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max trade = 0.

[NOTE]
Considering a finite state machine:

start-->"bear-position"  --price[today]<price[tomorrow]/buy--> "fully-invested"--price[tomorrow]<price[today]/sell-->"bear-position"

For the final day, if state is "fully-invested", then must sell.

"""

import time

class Solution:
    def maxTrade(self, prices) -> int:    
        if len(prices) <= 1:
            return 0

        state  = 0
        trade = []
        for k in range(0,len(prices)-1):
            if prices[k] < prices[k+1] and state == 0:
                trade.append(-prices[k])
                state = 1
            
            if prices[k] > prices[k+1] and state == 1:
                trade.append(prices[k])
                state = 0
        if state == 1:
            trade.append(prices[-1])

        #print(trade)
        return sum(trade)
                
if __name__ == '__main__':

    sln   = Solution()

    #Testcase0
    print('\nTestcase0...')
    prices = []
    print(prices, '--> ', sln.maxTrade(prices))

    #Testcase1
    print('\nTestcase1...')
    prices = [7,1,5,3,6,4]
    print(prices, '--> ', sln.maxTrade(prices))
    
    #Testcase2
    print('\nTestcase2...')
    prices = [1,2,3,4,5]
    print(prices, '--> ', sln.maxTrade(prices))
    
    #Testcase2
    print('\nTestcase2...')
    prices = [7,6,4,3,1]
    print(prices, '--> ', sln.maxTrade(prices))    

